#!/bin/bash
set -e;
SERVER=$1;
PATH=$2;

ssh ubuntu@"$SERVER" "bash -s" < "$PATH";