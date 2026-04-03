# Dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    gcc-14 \
    g++-14 \
    gdb \
    cmake \
    ninja-build \
    make \
    python3 \
    python3-pip \
    neovim \
  && rm -rf /var/lib/apt/lists/*

# Make gcc-15/g++-15 the default gcc/g++
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 100 \
 && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100

WORKDIR /work
