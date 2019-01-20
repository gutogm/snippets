#!/bin/bash
set -e;
start=`date +%s`

region="$1";
instanceId="$2";

aws --region "$region" ec2 start-instances --instance-ids "$instanceId";

state="pending";

while [[ "$state" != "running" ]]; 
do
    sleep 45;
    result="$(aws --region $region ec2 describe-instance-status --instance-ids $instanceId)";
    state=$(echo "$result"| | jq -r '.InstanceStatuses[0].InstanceState.Name');
    echo "State: $state"
done

echo "done."