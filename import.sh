#!/usr/bin/env bash

file=$1
provider=${2-ost}
date=$(date -I)
hash=$(sha1sum $file | cut -d ' ' -f 1)
put=/pls/$provider/$date

hadoop fs -mkdir -p /pls/$provider/$date
hadoop fs -put -f $file $put/$hash
hadoop fs -ls -R /pls

