#!/usr/bin/env bash

echo "Action runs using Dockerfile."
echo "act -j test -e event.json --use-gitignore=false --insecure-secrets --env RUNNER_DEBUG=1"

#[[ ! -f "action.yml" ]] && echo "Wrong Directory" && exit 1
#_image=$(grep -o 'ghcr.io/.*' action.yml | sed 's/".*//')
#echo "Using image: ${_image}"
#docker build --tag "${_image}" --build-arg VERSION="Local Build" .
#act -j test -e event.json --env image=true --action-offline-mode "$@"
