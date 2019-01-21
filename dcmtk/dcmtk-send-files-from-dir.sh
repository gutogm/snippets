DIRECTORY=$1;
AETITLE=$2;
SERVER=$3;
PORT=$4;

cd $DIRECTORY;
find -type f -name '*.dcm' | sort | xargs -I{} bash -c "dcmsend -v -aet $AETITLE -aec $AETITLE $SERVER $PORT {} > /dev/null; echo {}";