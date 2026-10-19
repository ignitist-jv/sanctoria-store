#!/usr/bin/env python3
"""Sanctoria social publisher. Posts an approved queue to the Facebook Page
and Instagram, one day at a time.

    python3 social/publish.py --check        verify the token, scopes and IDs
    python3 social/publish.py --dry-run      show what today would post
    python3 social/publish.py                publish today's approved item
    python3 social/publish.py --date 2026-10-10

Needs FB_SOCIAL_TOKEN in .env, from a Business System User with:
    pages_manage_posts  pages_read_engagement  pages_manage_engagement
    pages_show_list  instagram_basic  instagram_content_publish
    instagram_manage_comments
See social/SETUP.md Phase 1.

Only items marked "approved" in social/queue.json are ever posted, so nothing
reaches a public page without a human having read it first.
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error
from datetime import date

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, 'social', 'queue.json')
LOG   = os.path.join(ROOT, 'social', 'publish_log.txt')
GRAPH = 'https://graph.facebook.com/v23.0'
PAGE_ID   = '292317240635888'
IMAGE_BASE = 'https://sanctoriastore.com/social'

SCOPES = ['pages_manage_posts', 'pages_read_engagement', 'pages_manage_engagement',
          'pages_show_list', 'instagram_basic', 'instagram_content_publish',
          'instagram_manage_comments']


def env(key):
    for line in open(os.path.join(ROOT, '.env'), encoding='utf-8'):
        line = line.strip()
        if line.startswith(key + '='):
            return line.split('=', 1)[1].strip().strip('"').strip("'")
    return None


def api(path, params=None, post=False):
    params = dict(params or {})
    url = f'{GRAPH}/{path}'
    if post:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(params).encode(),
                                     method='POST')
    else:
        req = urllib.request.Request(url + '?' + urllib.parse.urlencode(params))
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        raise SystemExit(f'Graph API {e.code} on {path}\n{body}')


def log(line):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(f'{time.strftime("%Y-%m-%dT%H:%M:%S%z")} {line}\n')
    print(line)


def resolve(token):
    """System user token -> Page access token and Instagram user id."""
    page = api(PAGE_ID, {'fields': 'name,access_token,instagram_business_account',
                         'access_token': token})
    page_token = page.get('access_token')
    ig = (page.get('instagram_business_account') or {}).get('id')
    return page['name'], page_token, ig


def post_facebook(page_token, caption, image_url):
    r = api(f'{PAGE_ID}/photos', {'url': image_url, 'caption': caption,
                                  'published': 'true', 'access_token': page_token}, post=True)
    return r.get('post_id') or r.get('id')


def post_instagram(ig_id, page_token, caption, image_url):
    """Two steps: build a media container, then publish it."""
    c = api(f'{ig_id}/media', {'image_url': image_url, 'caption': caption,
                               'access_token': page_token}, post=True)
    for _ in range(30):                      # containers are not instantly ready
        s = api(c['id'], {'fields': 'status_code', 'access_token': page_token})
        if s.get('status_code') == 'FINISHED':
            break
        if s.get('status_code') == 'ERROR':
            raise SystemExit(f'Instagram container failed: {s}')
        time.sleep(2)
    r = api(f'{ig_id}/media_publish', {'creation_id': c['id'],
                                       'access_token': page_token}, post=True)
    return r.get('id')


def need_token():
    token = env('FB_SOCIAL_TOKEN')
    if not token:
        raise SystemExit('No FB_SOCIAL_TOKEN in .env. See social/SETUP.md Phase 1.')
    return token


def main():
    # --dry-run and the queue listing work offline, on purpose: you should be able
    # to see exactly what is scheduled before any credential exists.
    if '--check' in sys.argv:
        token = need_token()
        got = {p['permission'] for p in api('me/permissions',
               {'access_token': token}).get('data', []) if p.get('status') == 'granted'}
        print('Granted scopes:')
        for s in SCOPES:
            print(f'  {"OK " if s in got else "MISSING"}  {s}')
        name, page_token, ig = resolve(token)
        print(f'\nPage      : {name} ({PAGE_ID})')
        print(f'Page token: {"resolved" if page_token else "NOT RESOLVED, check asset assignment"}')
        print(f'Instagram : {ig or "NOT LINKED to the Page"}')
        missing = [s for s in SCOPES if s not in got]
        print('\nReady.' if not missing and page_token and ig
              else '\nNot ready yet. Fix the lines above.')
        return

    queue = json.load(open(QUEUE, encoding='utf-8'))
    when = sys.argv[sys.argv.index('--date') + 1] if '--date' in sys.argv \
        else date.today().isoformat()
    items = [i for i in queue['posts'] if i['date'] == when]
    if not items:
        print(f'Nothing queued for {when}. The week holds:')
        for i in queue['posts']:
            mark = 'posted' if i.get('posted') else i['status']
            print(f"  {i['date']}  {i['image']:<26} {mark}")
        return
    item = items[0]

    image_url = f'{IMAGE_BASE}/{item["image"]}'

    # Preview first, and regardless of status: reading a draft is how you decide
    # whether to approve it.
    if '--dry-run' in sys.argv:
        print(f'{when}  slot {item["slot"]}  status: {item["status"]}'
              + ('  ALREADY POSTED' if item.get('posted') else ''))
        print(f'image: {image_url}\n')
        print('--- FACEBOOK ---');  print(item['facebook'])
        print('\n--- INSTAGRAM ---'); print(item['instagram'])
        if item['status'] != 'approved':
            print(f'\nNot approved, so a real run would post nothing.'
                  f'\nTo approve: change "status" to "approved" for {when} in social/queue.json')
        return

    if item['status'] != 'approved':
        print(f'{when} is "{item["status"]}", not approved. Nothing posted.')
        return
    if item.get('posted'):
        print(f'{when} already posted: {item["posted"]}')
        return

    token = need_token()
    name, page_token, ig = resolve(token)
    fb_id = post_facebook(page_token, item['facebook'], image_url)
    log(f'FACEBOOK {when} -> {fb_id}')
    ig_id = post_instagram(ig, page_token, item['instagram'], image_url) if ig else None
    log(f'INSTAGRAM {when} -> {ig_id}' if ig_id else f'INSTAGRAM {when} -> skipped, not linked')

    item['posted'] = {'facebook': fb_id, 'instagram': ig_id, 'at': time.strftime('%Y-%m-%dT%H:%M:%S%z')}
    json.dump(queue, open(QUEUE, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
