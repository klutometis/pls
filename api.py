#!/usr/bin/env python

from flask import Flask, request, g
import psycopg2
import psycopg2.extras
import StringIO

app = Flask(__name__)

@app.route("/data")
def data():
    format = request.args.get('format', 'tsv')
    out = StringIO.StringIO()
    db = psycopg2.connect('host=localhost')
    cursor = db.cursor()
    cursor.execute('select question_id, student_id, outcome from data')
    for question_id, student_id, outcome in cursor.fetchall():
        out.write('%s\t%s\t%s\n' % (question_id, student_id, outcome))
    cursor.close()
    db.close()
    return out.getvalue()

@app.route("/stats")
def stats():
    start_date = request.args.get('start-date', None)
    end_date = request.args.get('end-date', None)
    db = psycopg2.connect('host=localhost')
    cursor = db.cursor()
    if start_date and end_date:
        cursor.execute('select date, imported from stats where date >= %s and date < %s',
                       start_date,
                       end_date)
    elif start_date:
        cursor.execute('select date, imported from stats where date >= %s',
                       start_date)
    elif end_date:
        cursor.execute('select date, imported from stats where date < %s',
                       end_date)
    else:
        cursor.execute('select date, imported from stats')
    out = StringIO.StringIO()
    for date, imported in cursor.fetchall():
        out.write('%s\t%s\n' % (date, imported))
    cursor.close()
    db.close()
    return out.getvalue()

if __name__ == "__main__":
    app.run(debug=True)
