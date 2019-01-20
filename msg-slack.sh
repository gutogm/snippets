#! /bin/bash
url=$1;
chat=$2;
username=$3;
message=$4;

curl -s -X POST --data-urlencode "payload={\"channel\": \"#$chat\", 
    \"username\": \"$username\", 
    \"text\": \"$message\"
     }" $url > /dev/null;