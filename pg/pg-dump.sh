# /bin/bash
# bash dump.sh localhost db_teste ./teste.dump testpassword
host=$1;
database=$2;
fpath=$3
export PGPASSWORD=$4;
pg_dump -U postgres -h $host $database > $fpath;