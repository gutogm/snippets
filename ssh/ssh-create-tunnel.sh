#/bin/bash
PORT=$1;
MIDDLE=$2;
KEY=$3;
SERVER=$4;

ssh -N -L $PORT:$SERVER:$PORT -i $KEY ubuntu@$MIDDLE -v;