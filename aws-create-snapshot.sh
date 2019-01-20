#!/bin/bash
set -e;

# /bin/bash create-snapshot.sh sa-east-1 vol-asdfasdfasdfasd "description";

region=$1;
volId=$2;
server=$3;

result=$(aws --region "$region" ec2 create-snapshot --volume-id "$volId" --description "$(date +%Y-%m-%d.%H)/snap:$server");
echo "$result";

snapId=$(echo "$result" | jq -r '.SnapshotId')

state="pending";
progress="0%";

while [[ "$state" != "completed" ]]; 
do
    sleep 45;
    result=$(aws --region "$region" ec2 describe-snapshots --filters Name=snapshot-id,Values="$snapId");
    progress=$(echo "$result"| jq -r '.Snapshots | .[0].Progress');
    state="$(echo "$result"| jq -r '.Snapshots | .[0].State')";
    echo "Progress: $progress, State: $state"
done

echo "$result";
exit 0;