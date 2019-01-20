#! /bin/bash
set -e;
url="https://api.telegram.org/$1/sendMessage";
chat=$2;
message="$1";

curl -s -X POST $url -d chat_id=$chat -d text="$message" -d parse_mode="markdown";