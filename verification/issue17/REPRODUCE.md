# Reproduction recipe — MELLANRUM Independent Verification #17

**Immutable object:** PR #16 `56d70c316031bf55a5260e1fbbe0fe187c55f297`; `candidate.bin` SHA-256 `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7` (exactly 4096 bytes).

Required GitHub Actions ZIP downloads, from [Actions run 45090981800](https://github.com/Odourman/mellanrum/actions/runs/45090981800):
- ROM/natively compiled listing artifact ID **14781417357**.
- Gopher2600 pinned executable artifact ID **14780574047** (source revision `74c544203378c1448a33c29bc8b4586079b050f4`).
- Frame-indexed developer controller witness artifact ID **14781244035** (its `commands.txt` contains 11,548 `STEP FRAME` and 166 `TV FRAME` commands).

## Example on Linux

After downloading those ZIPs, named `native.zip`, `gopher.zip` and `campaign.zip`:

```bash
set -eu
mkdir -p v17/native v17/gopher v17/trace v17/retest/shots
unzip -q native.zip -d v17/native
unzip -q gopher.zip -d v17/gopher
unzip -q campaign.zip -d v17/trace
chmod +x v17/gopher/gopher2600
test "$(wc -c < v17/native/candidate.bin)" -eq 4096
echo '45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7  v17/native/candidate.bin' | sha256sum -c -
cmp v17/native/candidate.bin v17/native/issue15_native/local_subset.bin

# Only redirect screenshot destinations; preserve all original input commands.
sed "s|/home/runner/work/mellanrum/mellanrum/build/issue15_campaign/attempt1/|$(pwd)/v17/retest/shots/|g" v17/trace/commands.txt > v17/retest/replay.txt
v17/gopher/gopher2600 HEADLESS v17/native/candidate.bin < v17/retest/replay.txt > v17/retest/trace.log
grep -c 'total: 262' v17/retest/trace.log
# Expected sampled TV count: 166. Also parse read-only mode/room RAM, do not infer wins merely from the command list.
```

This reproduces **one known input witness with independent emulator execution**, not an independent newly solved route. Consult the independent Verification chat evidence ZIP (SHA-256 `a8787178600aff57a3ae9f598b2cd1e8e39443b52f9a4163feed1a0dad1490ae`) for actual executed seeds 23017 and 51723, source scripts, logs and screenshots. That ZIP is not hosted on GitHub.

Stop on any ROM hash mismatch. Do not alter the frozen PR #4 or the candidate PR #16.
