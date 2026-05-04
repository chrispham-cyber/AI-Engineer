# Set up environment

## Install basic tools
```
brew install curl wget git
```

## Python virtual environments with UV

Why should we use `uv`? It's 100x faster than pip and handles virtual environments automatically.

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

```
uv venv
source .venv/bin/activate
uv pip install numpy matplotlib jupyter
```

To verify:
```
import sys
print(f"Python {sys.version}")

import numpy as np
print(f"NumPy {np.__version__}")
a = np.array([1, 2, 3])
print(f"Vector: {a}, dot product with itself: {np.dot(a, a)}")
```

Expect output:
```
Python 3.x.x) 
[Clang x.x.x ]
NumPy 2.x.x
Vector: [1 2 3], dot product with itself: x
```

## Node.js with pnpm
For `TypeScript` lessons (agents, MCP servers, web apps)
```
curl -fsSL https://fnm.vercel.app/install | bash
fnm install 22
fnm use 22

npm install -g pnpm

node -e "console.log('Node', process.version)"
```

Expect output:
```
Node v22.x.x
```

If use get error, add this to the end `.zshrc`:
```
eval "$(fnm env --use-on-cd)"
```

Then restart with `source ~/.zshrc`

## Rust
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

source /Users/fox/.cargo/env

rustc --version
cargo --version
```

Expect output:
```
rustc 1.x.x
cargo 1.x.x
```

## Julia
For heavy Math
```
curl -fsSL https://install.julialang.org | sh

julia -e 'println("Julia ", VERSION)'
```

Expect output:
```
Julia 1.x.x
```

## GPU setup
I don't have NVIDIA so I will use Macbook's GPU instead.
```
# Check system hardware
system_profiler SPDisplaysDataType | grep "Total Number of Cores"

# Install PyTorch with MPS
uv pip install torch torchvision torchaudio
```

To verify:
```
import torch

print(f"MPS available: {torch.backends.mps.is_available()}")

if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("GPU acceleration is active via Metal Performance Shaders.")
    
    x = torch.ones(1, device=device)
    print(f"Test tensor on device: {x.device}")
else:
    print("MPS not found. Ensure you are on macOS 12.3+ and using ARM64 Python.")

```

Expect output:
```
=== AI Engineering from Scratch — Environment Check ===

Core:
  [PASS] Python 3.10+
  [PASS] NumPy
  [PASS] Matplotlib
  [PASS] Jupyter
  [PASS] Git
  [PASS] Node.js
  [PASS] Rust (cargo)

GPU (optional):
  [PASS] PyTorch
  [PASS] MPS (M-Series GPU Active)

Result: 7/7 core checks passed, 2/2 GPU checks passed

You're ready. Start with Phase 1.
```

# Use Cases:
- Python: ML, DL, NLP, Vision, Audio, LLMs
- TypeScript: Tools, Agents, Swarms, Infra
- Rust:Performance-critical systems
- Julia: Math foundations

# Exercises
- Run the [verification script](scripts/verify.py) and fix any failures
- Write a "hello world" in all four languages and run each one

To run to each language:
```
python3 hello.py
julia hello.jl
npx tsx hello.ts
rustc hello.rs 
./hello.rs
```
