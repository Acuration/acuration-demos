def modify_folder_path(folder_path):
    #correcting the folder_path
    for c in folder_path:
        if c == '\\':
            folder_path = folder_path.replace('\\', '/')
    
    return folder_path