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

# Use Cases:
- Python: ML, DL, NLP, Vision, Audio, LLMs
- TypeScript: Tools, Agents, Swarms, Infra
- Rust:Performance-critical systems
- Julia: Math foundations

# Exercises
- Run the verification script and fix any failures
- Create a Python virtual environment and install PyTorch
- Write a "hello world" in all four languages and run each one
