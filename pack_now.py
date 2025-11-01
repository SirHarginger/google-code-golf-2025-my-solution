# pack_now.py  — build a Kaggle-ready submission.zip (3/400 solved is fine)
import os, zipfile, pathlib

ROOT = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(ROOT, "code")
OUT  = os.path.join(ROOT, "submission.zip")

# Tiny fallback for unsolved tasks (defines p() + stdin path)
STUB = (
    b"def p(g):\n"
    b"    return g\n"
    b"if __name__=='__main__':\n"
    b"    import sys,json;print(p(json.loads(sys.stdin.read())))"
)

def norm_bytes(b: bytes) -> bytes:
    # scoreboard-style normalization: drop BOM, CRLF->LF, strip trailing ws
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
    b = b.replace(b"\r\n", b"\n")
    return b.rstrip()

sizes = {}
real, stubs = [], []

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for i in range(1, 401):
        p = pathlib.Path(CODE, f"task{i:03}.py")
        if p.exists():
            b = norm_bytes(p.read_bytes())
            z.writestr(f"task{i:03}.py", b)
            sizes[i] = len(b)
            real.append(i)
        else:
            b = norm_bytes(STUB)
            z.writestr(f"task{i:03}.py", b)
            sizes[i] = len(b)
            stubs.append(i)

est = sum(max(1, 2500 - sizes.get(i, 2500)) for i in range(1, 401))
print("Wrote:", OUT)
print("Estimated total score:", est)
print(f"Real tasks ({len(real)}):", ", ".join(f"{i:03}" for i in real[:30]), "..." if len(real)>30 else "")
print(f"Stub tasks ({len(stubs)}): first few:", ", ".join(f"{i:03}" for i in stubs[:10]), "...")
print("Heaviest solved files (top 10):")
for k in sorted(real, key=lambda k: sizes[k], reverse=True)[:10]:
    print(f"  task{k:03}.py  {sizes[k]} bytes")
