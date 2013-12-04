#!/usr/bin/env sh

psql pls < data.sql && \
    ./import.py < data.csv && \
    ./stats.py && \
    pg_dump pls
