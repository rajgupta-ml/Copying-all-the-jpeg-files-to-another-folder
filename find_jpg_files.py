import os
import shutil
original_path = "D:/FOTOME/Images"
target_path = "C:/Users/prati/OneDrive/Documents/images"

for x in os.listdir(original_path):
    if x.endswith('.JPG'):
        full_file_name = os.path.join(original_path, x)
        shutil.copy(full_file_name, target_path)

print("copy complete")
