drop table if exists data;

create table data (
        question_id varchar(255),
        student_id varchar(255),
        outcome integer,
        primary key(question_id, student_id)
);

drop table if exists stats;

create table stats (
        date date primary key default now(),
        imported integer
);
