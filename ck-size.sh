#! /bin/bash
set -e;
user=$1
server=$2;

resultado=$( ssh $user@$server 'df -hT | grep -E "(/dev/.*ext|.*Filesystem.*|.*Sist.*)"' );

valores=($(echo "$resultado" | tail -1 | grep -E '[,0-9]*[M|G|\%]' -o));

size=$(echo ${valores[0]} | grep -Eo '[0-9,M|G\%]*');
used=$(echo ${valores[1]} | grep -Eo '[0-9,M|G\%]*');
avail=$(echo ${valores[2]} | grep -Eo '[0-9,M|G\%]*');
usedp=$(echo ${valores[3]} | grep -Eo '[0-9,M|G\%]*');

/bin/bash /app/ci/tools/alerts.sh "$(date +%Y-%m-%d/%H:%M) *$server* :: avail: $avail, used%: $usedp " > /dev/null;
