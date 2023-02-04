import os

files = os.listdir(r'D:\Course Videos\AWS Data Engineering')
with open(r'C:\Users\rknav\Downloads\files.txt', 'a') as new_file:
    for i in files:
        if '.txt' not in i:
            file_name = os.listdir('D:\\Course Videos\\AWS Data Engineering\\' + i)
            new_file.writelines(f'{i} no. of files: {len(file_name)}\n')
            for j in file_name:
                if '.mp4' in j:                    
                    new_file.writelines(f'\t{j}\n')


