# Python Environments

## Set up

```
cd your-project
uv venv
source .venv/bin/activate

uv init ai-projects
cd ai-projects
uv add torch numpy matplotlib jupyter ollama scikit-learn
```

## pyproject.toml

Add these lines to the end of `pyproject.toml`
```
torch = ["torch>=2.11.0", "torchvision>=0.18"]
llm = ["anthropic>=0.39", "openai>=1.50"]
```

Install:
```
uv pip install -e ".[torch]"    # base + PyTorch
uv pip install -e ".[llm]"     # base + LLM SDKs
uv pip install -e ".[torch,llm]" # everything
```

## Lockfiles

A lockfile pins every dependency to exact versions. This guarantees reproducibility: anyone who installs from the lockfile gets exactly the same packages.

```
uv pip compile pyproject.toml -o requirements.lock
uv pip install -r requirements.lock
```

Commit your lockfile to git. When someone clones the repo, they install from the lockfile and get identical versions.

To verify: [test.sh](../../ai-projects/test.sh)
```
bash test.sh
```

Expect output:
```
=== AI Engineering from Scratch: Python Environment Setup ===

[PASS] uv found: uv 0.11.8 
[PASS] Python: Python 3.12.13
[WARN] Existing .venv found. Reusing it.
[PASS] Activated virtual environment
[PASS] Python path: AI-Engineer/ai-projects/.venv/bin/python
[PASS] Installed: numpy matplotlib jupyter scikit-learn pandas
[PASS] NumPy operations working
[PASS] PyTorch 2.11.0 
[PASS] All checks passed
```

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|----------------------|
| Virtual environment | "A venv" | An isolated directory containing a Python interpreter and packages, separate from the system Python |
| Lockfile | "Pinned dependencies" | A file listing every package and its exact version, guaranteeing identical installs across machines |
| pyproject.toml | "The new setup.py" | The standard Python project configuration file, replacing setup.py/setup.cfg/requirements.txt |
| Transitive dependency | "A dependency of a dependency" | Package B depends on C; if you install A which depends on B, C is a transitive dependency of A |
| MPS mismatch | "My GPU isn't working" | PyTorch was compiled for a different MPS version than what your GPU driver supports |
