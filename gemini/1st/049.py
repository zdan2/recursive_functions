import os

def all_file(file_path, r=None):
    if r is None:
        r = []

    try:
        file_list = os.listdir(file_path)
    except PermissionError:
        return r  # アクセス権限がない場合スキップ

    for e in file_list:
        full_path = os.path.join(file_path, e)
        if os.path.isdir(full_path):
            all_file(full_path, r)
        else:
            r.append(full_path)
    
    return r

file_path = r'E:\Python'
result = all_file(file_path)
print(len(result))
