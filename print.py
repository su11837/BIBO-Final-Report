import os

def print_directory_files(path):
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            print("'"+'images/'+ file_name +"'")

# 使用範例
directory_path = r"C:\Users\shuping\Desktop\page\static\images"
print_directory_files(directory_path)