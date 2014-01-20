#!/usr/bin/env bash
all_questions=$(mktemp)
for i in *.xls; do
    questions=$(mktemp)
    cat $i | \
        sed  '/^$/d' | \
        xml sel -t -v '//_:Row//_:Data[10]' | \
        grep q > \
        $questions
    n_questions=$(wc -l < $questions)
    [[ $n_questions > 0 ]] && echo "$i,$n_questions"
    cat $questions >> $all_questions
    rm $questions
done | column -s, -t | sort -n -r -k 2
echo "------------------------------------"
echo "Total questions answered  $(wc -l < $all_questions)"
echo "Total unique questions    $(cat $all_questions | sort | uniq | wc -l)"
