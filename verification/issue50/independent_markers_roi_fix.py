#!/usr/bin/env python3
"""Test-only RC1 markör-addendum. Input: four existing genuine Stella PNGs.
The prior analyzer compared each ROI with itself; do not repeat that mistake.
"""
from pathlib import Path
import sys,hashlib,json
import numpy as np
from PIL import Image
def main(argv):
    if len(argv)!=2:
        raise SystemExit("usage: python3 independent_markers_roi_fix.py DIRECTORY_CONTAINING_marker0..3_forced_state_1x.png")
    base=Path(argv[1])
    frames=[np.asarray(Image.open(base/f"marker{i}_forced_state_1x.png").convert("RGB")) for i in range(4)]
    assert all(a.shape==(228,160,3) for a in frames)
    crops=[a[81:89,32:48] for a in frames]
    values=[int(np.any(c!=crops[0],axis=2).sum()) for c in crops]
    sha=[hashlib.sha256(c.tobytes()).hexdigest() for c in crops]
    result={"classification":"PRIOR_GENUINE_STELLA_ORIGINAL_DIAGNOSTIC_PNG_RECALC","same_scene":True,
            "roi_xyxy":[32,81,48,89],"different_from_neutral_pixel_count":values,
            "original_roi_sha256":sha,"distinct_4":len(set(sha))==4}
    print(json.dumps(result,indent=2))
    assert values==[0,14,30,28] and result["distinct_4"]
if __name__=="__main__": main(sys.argv)
