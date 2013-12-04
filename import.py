#!/usr/bin/env python

import sys
import csv
import psycopg2
import os

with psycopg2.connect(dbname='pls') as db:
    with db.cursor() as cursor:
        cursor.execute('insert into stats (imported) select 0 where not exists (select 1 from stats where date = current_date)')

    reader = csv.DictReader(sys.stdin)
    for row in reader:
        question_id = row['ExQbId']
        student_id = row['Name/ID']
        outcome = 1 if row['Correct?'] == 'Yes' else 0

        with db.cursor() as cursor:
            cursor.execute('update stats set imported = imported + 1 where date = current_date and not exists (select 1 from data where question_id = %s and student_id = %s)', (question_id, student_id))
            cursor.execute('insert into data (question_id, student_id, outcome) select %s, %s, %s where not exists (select 1 from data where question_id = %s and student_id = %s)', (question_id, student_id, outcome, question_id, student_id))
