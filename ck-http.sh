#!/bin/bash
out=$(curl --silent  --max-time 5 --location --head --fail "$1");
if curl --output /dev/null  --max-time 5 --location --silent --head --fail "$1"; then
    echo "$(date +%Y-%m-%d_%H:%M) - [ok] $1";
else
    echo "$(date +%Y-%m-%d/%H:%M) - [err] cmd: $0 $*";
fi