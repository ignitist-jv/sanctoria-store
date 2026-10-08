#!/bin/sh
# The local preview of the back end, on http://localhost:4174/prayer-song/ , with the demo orders in
# prayer-song/demo-data. Real keys from .env, a test ClickBank secret, and the preview admin password.
cd "$(dirname "$0")/../.." || exit 1
pkill -f "[p]hp -S localhost:4174" 2>/dev/null
env PS_DATA_DIR="$PWD/prayer-song/demo-data" PS_MOCK=0 PS_BASE_URL="http://localhost:4174/prayer-song" PS_CB_SECRET="TESTSECRETKEY123" \
    PS_ELEVENLABS_KEY="$(sed -n 's/^ELEVENLABS_API_KEY=//p' .env)" PS_ANTHROPIC_KEY="$(sed -n 's/^ANTHROPIC_API_KEY=//p' .env)" \
    PS_ADMIN_HASH="$(cat prayer-song/demo-data/admin-hash.txt 2>/dev/null)" \
    php -S localhost:4174 -t site
