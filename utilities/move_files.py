import shutil, os

src = r"D:\\FashionProductImageDataSet\\fashion-dataset\\styles\\"
dest = r"D:\\FashionProductImageDataSet\\fashion-dataset\\curated_json\\"

# read list of filenames to copy
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
with open(r"D:\FashionProductImageDataSet\fashion-dataset\file_list.txt","r") as f:
    src_files = [line.rstrip('\n') for line in f]

files_count = 0

# Copy the selected files from the list into the destination folder
# https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python/3399299
for file_name in src_files:
    full_filename = os.path.join(src, file_name)
    print(full_filename)
    if os.path.isfile(full_filename):
        shutil.copy(full_filename, dest)
        files_count += 1

    # shutil.copy(file, r"D:\FashionProductImageDataSet\fashion-dataset\curated_json")

print("Files copied:",files_count)
