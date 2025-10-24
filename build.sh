#!/usr/bin/env bash

[[ ! -f "action.yml" ]] && echo "Wrong Directory" && exit 1
_image=$(grep -o 'ghcr.io/.*' action.yml | sed 's/".*//')
echo "Using image: ${_image}"
docker build --tag "${_image}" --build-arg VERSION="Local Build" .
act -j test -e event.json --env image=true --action-offline-mode "$@"
