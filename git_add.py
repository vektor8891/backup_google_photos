import os
import subprocess
import time

selected_year = '2022'

backup_folder = '/media/vszabo/Backup'

files = os.listdir(os.path.join(backup_folder, selected_year))
git_folder = f'{backup_folder}/backup_{selected_year}'

for i, f in enumerate(files):
    if os.path.exists(os.path.join(git_folder, f)):
        print(f"[SKIP] {f} already exists in {git_folder} - skipping...")
    else:
        output = subprocess.run(['mv', f'{backup_folder}/{selected_year}/{f}', f'{git_folder}/{f}'], cwd=backup_folder,
                       stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
        print(output)
        print(f"[MOVE] {f} moved to {git_folder}")
        if os.path.exists(os.path.join(git_folder, '.git', 'index.lock')):
            subprocess.run(['rm', '.git/index.lock'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                           check=True).stdout.strip()
        if os.path.exists(os.path.join(git_folder, '.git', 'HEAD.lock')):
            subprocess.run(['rm', '.git/HEAD.lock'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                           check=True).stdout.strip()
        if os.path.exists(os.path.join(git_folder, '.git', 'refs/heads/main.lock')):
            subprocess.run(['rm', '.git/refs/heads/main.lock'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                           check=True).stdout.strip()

        output = subprocess.run(['git', 'add', f], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                                check=True).stdout.strip()
        # print(output)
        subprocess.run(['git', 'commit', '-m', f'add {f}'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                       check=True).stdout.strip()
        subprocess.run(['git', 'push'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
        print(f"[SUCCESS] {f} uploaded to github")
        while os.path.exists(os.path.join(git_folder, '.git', 'index.lock')):
            time.sleep(1)
