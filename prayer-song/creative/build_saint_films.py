#!/usr/bin/env python3
"""The saint films of 2026-10-19: five more cuts of the Saint Cecilia recipe, the only Prayer Song ad
that had made a sale by then (5 animated oil-painting clips, top headline, chant, 3s end card).

Reuses build_oil_motion_film.build() unchanged and only points it at a new clip folder. Each film has
three new clips of its own figure and two of the generic 2026-10-16 clips (M1 to M7). Every film has its
own music track, and none of them is a track an earlier ad used (those were chant_B_drone and
bed_B_choirpad).

    python3 prayer-song/creative/build_saint_films.py [slug]
"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_oil_motion_film as base

ROOT = os.path.dirname(os.path.dirname(HERE))
NEW = os.path.join(ROOT, "output/ads/2026-10-19-saint-films")
OLD_CLIPS = base.CLIPS
base.CLIPS = os.path.join(NEW, "motion")
base.OUT = os.path.join(NEW, "films")
base.WORK = os.path.join(NEW, "_work")

CTA = "Create Your Prayer Song Now"
END_CTA = "Create your prayer song"
FILMS = [
    {"slug": "SB1_SaintGregory_28s", "audio": "chant_A_monks",
     "headline": "The Chant That Bears His Name", "end_head": "A name, kept in a song.",
     "clips": ["G1_GregoryDove", "M7_MonksChanting", "G2_GregoryChoirBook", "M3_MaryCrowned", "G3_GregoryPrayer"]},
    {"slug": "SB2_SaintHildegard_28s", "audio": "sung_B_choir",
     "headline": "She Wrote Songs For God", "end_head": "Her name, set to music.",
     "clips": ["H3_HildegardLivingLight", "M2_AngelChoir", "H1_HildegardTablet", "M5_MaryListening", "H2_HildegardChapel"]},
    {"slug": "SB3_SaintFrancis_28s", "audio": "sung_A_congregation",
     "headline": "He Sang To Brother Sun", "end_head": "A prayer made to be sung.",
     "clips": ["F1_FrancisBrotherSun", "M1_MaryInPrayer", "F2_FrancisBirds", "M2_AngelChoir", "F3_FrancisSunlitFace"]},
    {"slug": "SB4_KingDavid_28s", "audio": "bed_A_strings",
     "headline": "The King Who Prayed In Song", "end_head": "A psalm with a name in it.",
     "clips": ["D2_DavidCrownedPsalmist", "M7_MonksChanting", "D1_DavidBeforeSaul", "M1_MaryInPrayer", "D3_DavidHarpHands"]},
    {"slug": "SB5_Magnificat_28s", "audio": "chant_C_mixed",
     "headline": "My Soul Doth Magnify The Lord", "end_head": "A song of praise, by name.",
     "clips": ["MG3_MaryInSong", "M2_AngelChoir", "MG1_Visitation", "M3_MaryCrowned", "MG2_MaryArmsLifted"]},
]
for f in FILMS:
    f["cta"], f["end_cta"] = CTA, END_CTA

if __name__ == "__main__":
    tracks = [f["audio"] for f in FILMS]
    assert len(tracks) == len(set(tracks)), "a music track repeats across the films"
    assert not {"chant_B_drone", "bed_B_choirpad"} & set(tracks), "a track an earlier ad used"
    os.makedirs(base.CLIPS, exist_ok=True)
    os.makedirs(base.OUT, exist_ok=True)
    # the generic 2026-10-16 clips, copied next to the new ones so build() finds every clip in one folder
    for name in {c for f in FILMS for c in f["clips"] if c.startswith("M")}:
        dst = os.path.join(base.CLIPS, name + "_raw.mp4")
        if not os.path.exists(dst):
            shutil.copy(os.path.join(OLD_CLIPS, name + "_raw.mp4"), dst)
    want = sys.argv[1] if len(sys.argv) > 1 else None
    for f in FILMS:
        if not want or f["slug"] == want:
            base.build(f)
