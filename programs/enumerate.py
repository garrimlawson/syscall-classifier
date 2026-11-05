import os

count = 0
for folder, subfolders, files in os.walk("/usr/share"):
    for name in files:
        path = os.path.join(folder, name)
        os.lstat(path)
        count = count + 1
print(count)
