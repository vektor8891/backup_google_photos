import subprocess

selected_year = '2021'

backup_folder = '/media/vszabo/Backup'

git_folder = f'{backup_folder}/backup_{selected_year}'
result = subprocess.run(['git', 'status'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True)
output = result.stdout.strip()
if "\n\tmodified:   " in output:
    file_names = output.split("\n\tmodified:   ")[1:]
    for f in file_names[0:100]:
        print(f)
        subprocess.run(['git', 'add', f], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
        subprocess.run(['git', 'commit', '-m', f'"add {f}"'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                       check=True).stdout.strip()
        subprocess.run(['git', 'push'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
        print(f"Success: {f} uploaded to github")
