#!/usr/bin/env python

import sys
import csv
import psycopg2
import os
import random


with psycopg2.connect(dbname='pls') as db:
    with db.cursor() as cursor:
        cursor.execute('select imported from stats')
        imported = cursor.fetchone()[0]
        delta = 0
        
        while imported > 0:
            cursor.execute('insert into stats (date, imported) select current_date - %s, %s where not exists (select 1 from stats where date = current_date - %s)',
                           (delta, imported, delta))
            if random.random() < 0.2:
                imported = imported - random.randrange(100)
            delta = delta + 1
