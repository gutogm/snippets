#!/bin/bash
set -e;

if [[ ! -f ~/.ssh/id_rsa ]]; then
    ssh-keygen -f ~/.ssh/id_rsa -t rsa -N '';
fi
cat ~/.ssh/id_rsa.pub;