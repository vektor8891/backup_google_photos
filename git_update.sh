#!/bin/bash

selected_year='2022'
backup_folder='/media/vszabo/Backup'
git_folder="$backup_folder/backup_$selected_year"

output=$(git -C "$git_folder" status)
if [[ -e "$git_folder/.git/index.lock" ]]; then
    rm "$git_folder/.git/index.lock"
fi
if [[ -e "$git_folder/.git/HEAD.lock" ]]; then
    rm "$git_folder/.git/HEAD.lock"
fi
if [[ -e "$git_folder/.git/refs/heads/main.lock" ]]; then
    rm "$git_folder/.git/refs/heads/main.lock"
fi
if [[ $output == *"modified:   "* ]]; then
    file_names=$(echo "$output" | sed -n '/Changes not staged for commit/,$p' | sed -n 's/.*modified:   //p')
    IFS=$'\n'
    total_files=$(echo "$file_names" | wc -l)
    current_file=0
    commit_count=0
    for f in $file_names; do
        ((current_file++))
        ((commit_count++))
        percentage=$((current_file * 100 / total_files))
        echo "Processing $f ($current_file/$total_files - $percentage%)"
        if [[ "$f" != *"\\30"* ]] || [[ "$f" != *" "* ]]; then
            git -C "$git_folder" add "$f"
            git -C "$git_folder" commit -m "add $f"
            echo "Commit $commit_count/$total_files"
            if ((commit_count % 15 == 0)); then
                git -C "$git_folder" push
                echo "Pushed after $commit_count commits"
            fi
            while [[ -e "$git_folder/.git/index.lock" ]]; do
                sleep 1
            done
        fi
    done
fi
