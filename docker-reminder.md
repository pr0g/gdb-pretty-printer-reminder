# Docker commands

## docker classic

```bash
docker run --rm -it \
  -v $(pwd):/work \
  -w /work \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  test bash
```

## docker compose

```bash
docker compose run --rm app bash
```
