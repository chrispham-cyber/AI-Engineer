import sys
import shutil
import subprocess

CHECKS = [
    ("Python 3.10+", lambda: sys.version_info >= (3, 10), f"Python {sys.version}"),
    ("NumPy", lambda: __import__("numpy"), None),
    ("Matplotlib", lambda: __import__("matplotlib"), None),
    ("Jupyter", lambda: __import__("jupyter"), None),
    ("Git", lambda: shutil.which("git") is not None, None),
    ("Node.js", lambda: shutil.which("node") is not None, None),
    ("Rust (cargo)", lambda: shutil.which("cargo") is not None, None),
]

def run_check(name, check_fn, detail_fn=None):
    try:
        result = check_fn()
        if result is False:
            raise Exception("Check returned False")
        detail = ""
        if detail_fn:
            if callable(detail_fn):
                detail = f" ({detail_fn()})"
            else:
                detail = f" ({detail_fn})"
        print(f"  [PASS] {name}{detail}")
        return True
    except Exception:
        print(f"  [FAIL] {name}")
        return False


def main():
    print("\n=== AI Engineering from Scratch — Environment Check ===\n")

    print("Core:")
    passed = sum(run_check(name, fn, detail) for name, fn, detail in CHECKS)
    total = len(CHECKS)

    print(f"\nResult: {passed}/{total} core checks passed", end="")

    if passed == total:
        print("\nYou're ready. Start with Phase 1.\n")
    else:
        print("\nFix the failed checks above, then run this script again.\n")

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
