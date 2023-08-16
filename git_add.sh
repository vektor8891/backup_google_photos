#!/bin/bash

selected_year='2022'
backup_folder='/media/vszabo/Backup'

files=$(ls "$backup_folder/$selected_year")
git_folder="$backup_folder/backup_$selected_year"

for f in $files; do
    if [ -e "$git_folder/$f" ]; then
        echo "[SKIP] $f already exists in $git_folder - skipping..."
    else
        output=$(mv "$backup_folder/$selected_year/$f" "$git_folder/$f" 2>&1)
        echo "$output"
        echo "[MOVE] $f moved to $git_folder"

        if [ -e "$git_folder/.git/index.lock" ]; then
            rm "$git_folder/.git/index.lock"
        fi
        if [ -e "$git_folder/.git/HEAD.lock" ]; then
            rm "$git_folder/.git/HEAD.lock"
        fi
        if [ -e "$git_folder/.git/refs/heads/main.lock" ]; then
            rm "$git_folder/.git/refs/heads/main.lock"
        fi

        output=$(git -C "$git_folder" add "$f" 2>&1)
        # echo "$output"
        git -C "$git_folder" commit -m "add $f"
        git -C "$git_folder" push

        echo "[SUCCESS] $f uploaded to GitHub"

        while [ -e "$git_folder/.git/index.lock" ]; do
            sleep 1
        done
    fi
done
