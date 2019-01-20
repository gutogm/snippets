#! /bin/bash
# nao usar o set -e pois tem tratamento de erro
SERVER=$1;
ping -c2 $SERVER -q > /dev/null;
code=$?;
if [[ ! $code -eq 0 ]]; then
    echo "$(date +%Y-%m-%d/%H:%M) - [err] code: $code - cmd: $0 $*";
else
    echo "$(date +%Y-%m-%d_%H:%M) - [ok] $SERVER";
fi