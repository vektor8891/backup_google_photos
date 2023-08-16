import os
import re
import zipfile
from PIL import Image
import pyheif
import shutil
import subprocess

# year to check
selected_year = '2022'

# path to ZIP file downloaded from Google Takeout
zip_file_path = os.path.expanduser('~/Downloads/takeout-20230809T005049Z-001.zip')

# path to directory where files should be extracted
extract_to_directory = os.path.expanduser('~/Downloads/GooglePhotos/')

# directory to temporarily store files
temp_dir = os.path.expanduser('~/Downloads/GooglePhotos_temp/')

# open ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # loop through each file
    for i, item in enumerate(zip_ref.infolist()[0:1000]):
        file_path = item.filename
        ext = os.path.splitext(file_path)[1].lower()
        file_name_old = os.path.basename(file_path)
        # ignore albums & settings
        # only consider photos for each year
        if file_path.startswith('Takeout/Google Photos/Photos from') and not file_path.endswith('.json'):
            match = re.search(r'Photos from (\d{4})', file_path)
            if match:
                # extract year from path
                year = match.group(1)
                if year == selected_year:
                    item.filename = file_name_old
                    temp_folder = os.path.join(temp_dir, year)
                    # change output file name for HEIC images
                    if ext in ['.heic']:
                        file_name_new = os.path.splitext(file_name_old)[0] + '.jpg'
                    else:
                        file_name_new = file_name_old
                    extract_folder = os.path.join(extract_to_directory, year)
                    extract_file_path = os.path.join(extract_folder, file_name_new)
                    # skip if file already exists
                    if not os.path.exists(extract_file_path):
                        if ext in ['.jpg', '.jpeg', '.png']:
                            # save JPG
                            zip_ref.extract(item, extract_folder)
                            print(f"[SUCCESS] {file_name_new} successfully extracted to {extract_file_path}")
                        elif ext in ['.heic']:
                            # save HEIC to temporary directory
                            zip_ref.extract(item, temp_folder)
                            temp_file_path = os.path.join(temp_folder, item.filename)
                            # convert HEIC to JPG
                            try:
                                heic_image = pyheif.read(temp_file_path)
                                image = Image.frombytes(heic_image.mode, heic_image.size, heic_image.data, "raw",
                                                        heic_image.mode, heic_image.stride)
                                image.save(extract_file_path, format='JPEG')
                                print(
                                    f"[SUCCESS] {file_name_old} successfully converted to JPG & extracted to {extract_file_path}")
                            except ValueError as e:
                                if str(e) == 'Input is not a HEIF/AVIF file':
                                    # try to save original file as JPG
                                    item.filename = file_name_new
                                    zip_ref.extract(item, extract_folder)
                                    print(f"[SUCCESS] {file_name_old} successfully extracted to {extract_file_path}")
                                else:
                                    raise ValueError(e)
                        elif ext in ['.mp4', '.mov']:
                            temp_file_path = os.path.join(temp_folder, item.filename)
                            if not os.path.exists(temp_file_path):
                                # save movie to temporary directory
                                zip_ref.extract(item, temp_folder)
                                # check file size
                                file_size_bytes = os.path.getsize(temp_file_path)
                                file_size_mb = file_size_bytes / (1024 * 1024)
                                if file_size_mb < 99:
                                    # move small file to final directory
                                    shutil.move(temp_file_path, extract_file_path)
                                else:
                                    # split big videos into small parts
                                    script_path = os.path.abspath(__file__)
                                    script_directory = os.path.dirname(script_path)
                                    command = ['bash', 'split-video.sh', temp_file_path, "90000000",
                                               "-c:v libx264 -crf 23 -c:a copy -vf scale=640:-2 -y"]
                                    result = subprocess.run(command, cwd=script_directory, stdout=subprocess.PIPE,
                                                            text=True, check=True)
                                    output = result.stdout.strip()
                                    print(f"[SUCCESS] Large video {file_name_old} split into small parts")

                                    # move new files to final destination
                                    all_files = os.listdir(temp_folder)
                                    matching_files = [f for f in all_files if
                                                      f.startswith(item.filename[:-4]) and f.endswith('.mp4')]
                                    for f in matching_files:
                                        source_path = os.path.join(temp_folder, f)
                                        destination_path = os.path.join(extract_folder, f)
                                        shutil.move(source_path, destination_path)
                                        print(f"[SUCCESS] Small video {f} moved to {extract_folder}")
                            else:
                                print(f"[SKIP] Large video {file_name_old} already processed - skipping...")
                        else:
                            raise ValueError(f'[ERROR] {file_name_old} has unknown extension: {ext}')
                    else:
                        print(f"[SKIP] {file_name_old} already extracted - skipping...")
            else:
                raise ValueError(f"[ERROR] No year found in {file_path}")
        else:
            print(f"[SKIP] {file_name_old} not included - skipping...")
