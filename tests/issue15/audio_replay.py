#!/usr/bin/env python3
"""Genuine Gopher2600 TIA-WAV captures from normal, no-POKE, frame-stepped inputs.
Emulator source is pinned; one CLI flag exposing existing native WavWriter added at build.
No product code, state or synthesizer modifications.
"""
import argparse,hashlib,json,re,subprocess,sys,platform
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument("--emulator",required=True)
ap.add_argument("--rom",required=True)
ap.add_argument("--out",required=True)
args=ap.parse_args()
exe=Path(args.emulator).resolve();rom=Path(args.rom).resolve();root=Path(args.out).resolve()
root.mkdir(parents=True,exist_ok=True)
expected="45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7"
assert len(rom.read_bytes())==4096 and hashlib.sha256(rom.read_bytes()).hexdigest()==expected
for mode in ("TITLE","CAMPAIGN","FRI_SKOG"):
    out=root/mode;out.mkdir(exist_ok=True)
    commands=["VERSION","CARTRIDGE HASH","PERIPHERAL LEFT STICK","PANEL SET P1PRO","PANEL SET P0AM" if mode=="FRI_SKOG" else "PANEL SET P0PRO"]
    events=[{"frame":0,"input":"LEFT_DIFFICULTY_B" if mode=="FRI_SKOG" else "LEFT_DIFFICULTY_A"}]
    frames=800 if mode=="TITLE" else 1300
    for frame in range(frames):
        if mode!="TITLE" and frame in (8,150,310,512,722,980):
            commands.append("STICK LEFT FIRE");events.append({"frame":frame,"input":"FIRE_DOWN"})
        if mode!="TITLE" and frame in (12,154,314,516,726,984):
            commands.append("STICK LEFT NOFIRE");events.append({"frame":frame,"input":"FIRE_UP"})
        if mode!="TITLE" and frame in (90,270,690):
            commands.append("STICK LEFT RIGHT");events.append({"frame":frame,"input":"RIGHT_DOWN"})
        if mode!="TITLE" and frame in (95,275,695):
            commands.append("STICK LEFT NORIGHT");events.append({"frame":frame,"input":"RIGHT_UP"})
        commands.append("STEP FRAME")
        if frame%150==0:
            commands.extend(("TV FRAME","AUDIO","PEEK 0x00b8 0x00b9 0x00c6"))
    commands.extend(("SCREENSHOT "+str(out/"final.png"),"QUIT"))
    (out/"commands.txt").write_text("\n".join(commands)+"\n")
    (out/"events.json").write_text(json.dumps(events,indent=2)+"\n")
    with (out/"native_tia_stdout.log").open("w") as log:
        proc=subprocess.run([str(exe),"HEADLESS","-wav",str(rom)],input="\n".join(commands)+"\n",text=True,cwd=out,stdout=log,stderr=subprocess.STDOUT,timeout=180)
    wav=list(out.rglob("*.wav"))
    result={"mode":mode,"emulator_returncode":proc.returncode,"native_audio_wav_files":len(wav),"frames":frames,"wav_bytes":[p.stat().st_size for p in wav],"rom_sha256":expected,"wav_status":"CAPTURED" if wav and proc.returncode==0 else "INCONCLUSIVE","classification":"REAL_NATIVE_TIA_AUDIO_FRAME_STEPPED_NO_STATE_INJECTION"}
    (out/"capture.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))
