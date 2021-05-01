import shutil
import os

"""
Python os.walk() Method:
    https://www.tutorialspoint.com/python/os_walk.htm
List all the filenames in a directory & print results:
    https://stackoverflow.com/questions/12199120/python-list-all-the-file-names-in-a-directory-and-its-subdirectories-and-then-p
General help:
    https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html
Read the image filenames and create an associated json filename:
    https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
Copy the selected files from the list into the destination folder:
    # https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python/3399299
"""


def move_listed_files():
    """
    Function to read the curated image filenames and extract the associated
    JSON files from the kaggle.com data set and move them to a new folder
    for further work.
    """

    src_images = r"D:\\FashionProductImageDataSet\\fashion-dataset\\curated_images\\"
    src_json = r"D:\\FashionProductImageDataSet\\fashion-dataset\\styles\\"
    dest = r"D:\\FashionProductImageDataSet\\fashion-dataset\\curated_json\\"

    files_count = 0

    for files in os.walk(src_images, topdown=False):
        for filename in files:

            image_filename = os.path.join(filename)
            str = image_filename.split('.')
            json_file = str[0] + '.json'
            full_json_filename = os.path.join(src_json, json_file)

            if os.path.isfile(full_json_filename):
                shutil.copy(full_json_filename, dest)
                files_count += 1

    print("Files copied:", files_count)


move_listed_files()
