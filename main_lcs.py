print(str.upper("WELCOME TO LCS...\n This program will be available soon"))

import os
folder_path = "src"

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path)
    
    if os.path.isfile(file_path):
       print(f"--- reading {file_name}---")
       with open(file_path, "r") as f:
           contents = f.read()
           print(contents)
    