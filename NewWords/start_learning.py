import os
from datetime import date

# get file name. I need to learn new words at today.
today = date.today()
# new_file_name = today.strftime("%Y_%m_%d_new_words.txt")
new_file_name = today.strftime("user/%Y_%m_%d_new_words.txt")

# Creates the specified file, but return an error if the file exists.
if not os.path.exists(new_file_name):
    f = open(new_file_name, "x")
    f.close()
