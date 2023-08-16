import subprocess
import time
import os

selected_year = '2022'

backup_folder = '/media/vszabo/Backup'

git_folder = f'{backup_folder}/backup_{selected_year}'

file_names = [
'20221230_083142.mp4',
'32EA6788-48D5-4644-BD03-E1E8A570FB6A-38649-0000.mov',
'C25E2FDB-5BD9-4904-9FBB-D803E4416F27-38649-0000.mov',
'D98A215E-84DE-4061-A84F-BA9520679EEA-918-000000.mov',
'Driveway-2022-11-30--1127638784f4e1096509bf5fb1.MOV',
'IMG_2004.MOV',
'IMG_2031.MOV',
'IMG_2052.MOV',
'IMG_2055.MOV',
'IMG_2056.MOV',
'IMG_2058.MOV',
'IMG_2059.MOV',
'IMG_2060.MOV',
'IMG_2071.MOV',
'IMG_2072.MOV',
'IMG_2076.MOV',
'IMG_2077.MOV',
'IMG_2079.MOV',
'IMG_2080.MOV',
'IMG_2081.MOV',
'IMG_2083.MOV',
'IMG_2084.MOV',
'IMG_2087.MOV',
'IMG_2092.MOV',
'IMG_2093.MOV',
'IMG_2094.MOV',
'IMG_2095.MOV',
'IMG_2096.MOV',
'IMG_2097.MOV',
'IMG_2098.MOV',
'IMG_2099.MOV',
'IMG_2100.MOV',
'IMG_2101.MOV',
'IMG_2102.MOV',
'IMG_2103.MOV',
'IMG_2104.MOV',
'IMG_2105.MOV',
'IMG_2106.MOV',
'IMG_2107.MOV',
'IMG_2108.MOV',
'IMG_2109.MOV',
'IMG_2110.MOV',
'IMG_2111.MOV',
'IMG_2112.MOV',
'IMG_2113.MOV',
'IMG_2114.MOV',
'IMG_2115.MOV',
'IMG_2116.MOV',
'IMG_2117.MOV',
'IMG_2120.MOV',
'IMG_2122.MOV',
'IMG_2123.MOV',
'IMG_2125.MOV',
'IMG_2127.MOV',
'IMG_2142.MOV',
'IMG_2143.MOV',
'IMG_2147.MOV',
'IMG_2150.MOV',
'IMG_2156.MOV',
'IMG_2157.MOV',
'IMG_2158.MOV',
'IMG_2162.MOV',
'IMG_2165.MOV',
'IMG_2166.MOV',
'IMG_2167.MOV',
'IMG_2168.MOV',
'IMG_2169.MOV',
'IMG_2170.MOV',
'IMG_2176.MOV',
'IMG_2177.MOV',
'IMG_2178.MOV',
'IMG_2179.MOV',
'IMG_2180.MOV',
'IMG_2181.MOV',
'IMG_2182.MOV',
'IMG_2183.MOV',
'IMG_2185.MOV',
'IMG_2186.MOV',
'IMG_2188.MOV',
'IMG_2189.MOV',
'IMG_2190.MOV',
'IMG_2193.MOV',
'IMG_2198.MOV',
'IMG_2200.MOV',
'IMG_2204.MOV',
'IMG_2206.MOV',
'IMG_2207.MOV',
'IMG_2208.MOV',
'IMG_2209.MOV',
'IMG_2212.MOV',
'IMG_2213.MOV',
'IMG_2214.MOV',
'IMG_2223.MOV',
'IMG_2225.MOV',
'IMG_2250.MOV',
'viktor_zoldkartya_eleje.jpg',
'viktor_zoldkartya_hatulja.jpg'
]
# output = subprocess.run(['git', 'status'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
# if os.path.exists(os.path.join(git_folder, '.git', 'index.lock')):
#     subprocess.run(['rm', '.git/index.lock'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
#                    check=True).stdout.strip()
# if "\n\tmodified:   " in output:
#     file_names = output.split("Changes not staged for commit")[1].split("\n\tmodified:   ")[1:]
for i, f in enumerate(file_names):
    subprocess.run(['rm', f], cwd=git_folder, stdout=subprocess.PIPE, text=True,
                                      check=True).stdout.strip()
    # print(f'{f} ({i}/{len(file_names)})')
    # # print('running git add')
    # output = subprocess.run(['git', 'add', f], cwd=git_folder, stdout=subprocess.PIPE, text=True,
    #                         check=True).stdout.strip()
    # print(output)
    # # print('running git commit')
    # subprocess.run(['git', 'commit', '-m', f'add {f}'], cwd=git_folder, stdout=subprocess.PIPE, text=True,
    #                check=True).stdout.strip()
    # subprocess.run(['git', 'push'], cwd=git_folder, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
    # print(f"Success: {f} uploaded to github")
    # while os.path.exists(os.path.join(git_folder, '.git', 'index.lock')):
    #     time.sleep(1)
