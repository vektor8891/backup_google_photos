import subprocess
import time
import os

selected_year = '2021'

backup_folder = '/media/vszabo/Backup'

git_folder = f'{backup_folder}/backup_{selected_year}'
output = subprocess.run(['git', 'status'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
if os.path.exists(os.path.join(git_folder, '.git', 'index.lock')):
    subprocess.run(['rm', '.git/index.lock'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                   check=True).stdout.strip()
if "\n\tmodified:   " in output:
    file_names = output.split("Changes not staged for commit")[1].split("\n\tmodified:   ")[1:]
    for i, f in enumerate(file_names):
        print(f'{f} ({i}/{len(file_names)})')
        # print('running git add')
        output = subprocess.run(['git', 'add', f], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                                check=True).stdout.strip()
        print(output)
        # print('running git commit')
        subprocess.run(['git', 'commit', '-m', f'add {f}'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                       check=True).stdout.strip()
        subprocess.run(['git', 'push'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
        print(f"Success: {f} uploaded to github")
        while os.path.exists(os.path.join(git_folder, '.git', 'index.lock')):
            time.sleep(1)
