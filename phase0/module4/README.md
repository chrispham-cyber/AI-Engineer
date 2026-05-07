# Docker

## Why?

If you have tools' version different from your colleague, your model crashes on their machine. Your Dockerfile works on both.

And why AI projects need Docker:
- GPU drivers are fragile
- Model weights are large
- Multi-service architectures are common

## Key vocab

| Term | What it means |
|------|---------------|
| Image | A read-only template. Your recipe. Built from a Dockerfile. |
| Container | A running instance of an image. Your kitchen. |
| Dockerfile | Instructions to build an image. Layer by layer. |
| Volume | Persistent storage that survives container restarts. |
| docker-compose | A tool for defining multi-container applications in YAML. |

## Install
```
brew install --cask docker
open /Applications/Docker.app

docker --version
docker run hello-world
```

Expect output:
```
Docker version 29.x.x

Hello from Docker!
This message shows that your installation appears to be working correctly.
```
