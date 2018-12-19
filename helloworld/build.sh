#!/bin/bash

image="xezpeleta/helloworld"
version="1.1"

# Register handlers
# Register qemu-*-static for all supported processors except the current one
# https://github.com/multiarch/qemu-user-static
#docker run --rm --privileged multiarch/qemu-user-static:register --reset

# Build and push images
for arch in amd64 arm32v7; do
  docker build -f Dockerfile.${arch} -t ${image}:${arch}-${version} .
  docker push ${image}:${arch}-${version}
done


# Build a multi-arch manifest
docker manifest create ${image}:${version} ${image}:amd64-${version} ${image}:arm32v7-${version}
docker manifest create ${image}:latest ${image}:amd64-${version} ${image}:arm32v7-${version}

docker manifest push ${image}:${version}
docker manifest push --purge ${image}:latest