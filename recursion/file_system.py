import os

def print_files():

    with open('tempName.txt', 'w') as output:
        for root, dirs, files in os.walk('.'):
            for name in files:
                # if file.endswith("shp"):
                output.write(os.path.join(root, name)+"\n")

#http://pythoncentral.io/recursive-python-function-example-make-list-movies/

def print_files_dfs(root_directory, file_extensions=['txt', 'py', 'mp4', 'dat', 'jpeg', 'png'], files=[]):
    "Print files in root_directory with extensions recursively"

    #Get the absolute path of the root_directory parameter
    root_directory = os.path.abspath(root_directory)

    #Get list of files in root_directory
    root_directory_files = os.listdir(root_directory)

    #Traverse through all files
    for filename in root_directory_files:
        filepath = os.path.join(root_directory, filename)

        #Check if it's a normal file or a direcotyr
        if os.path.isfile(filepath):
            # for file_extension in file_extensions:
            #     if not filepath.endswith(movie_extension):
            #         continue
            files.append(filepath)

        elif os.path.isdir(filepath):
            files = print_files_dfs(filepath)

    if files:
        return files

# Group files by size

import filecmp

def make_file_size_dict(files):
    file_size_dict = {}
    for file_name in files:
        size = len(file_name)
        # size = os.path.getsize(file_name)
        if size in file_size_dict:
            file_size_dict[size].append(file_name)
        else:
            file_size_dict[size] = [file_name]
    print file_size_dict

    duplicate_files = []

    for file_names in file_size_dict.itervalues():
        if len(file_names) > 1:
            for i in range(len(file_names)):
                for j in range(i+1, len(file_names)):
                    # print file_names[i], file_names[j]
                    # if file_names[i] == file_names[j]:
                    if filecmp.cmp(file_names[i], file_names[j]):  # if true, then duplicates
                        duplicate_files.append(file_names[i])

    for duplicate in duplicate_files:
        os.remove(duplicate)

    print file_size_dict


make_file_size_dict(['file1', 'file2', 'file3', 'file45', 'file4', 'file3', 'file6'])

"""
/a/b/foo --> "potato"
/a/b/bar --> "carrot"
/a/c/baz --> "potato"
/a/c/quux --> "turnip"
/a/c/xyzzy --> "turnip"
/d/asdf --> "potato"
"""

def list_dir(path):
    """
    Returns a list of the filenames (both normal files and directories) 
    in the directory referred to by `path`
    list_dir('/a') --> ['b', 'c']
    """
    
    
    
def is_dir(path):
    """
    Returns True if `path` is a directory
    """
    
def get_size(path):
    """
    Returns the size of the file at `path`
    """
    
with open(path) as f:
    # return the next megabyte of bytes in the file, or None if there 
    # are no more bytes
    f.read(1024*1024) 
    
def find_duplicate_files(abs_path, file_list):
    """ Returns a list of lists of relative paths of files that have the 
    same contents"""
    
    file_size_dict = {}
    for file_path in file_list:
        size = os.get_size(file_path)
        if size in file_size_dict:
            file_size_dict[size].append(file_path)
        else:
            file_size_dict[size] = [file_path]
    
    
    

def create_list_of_files(abs_path, file_list=None):
    
    if file_list is None:
        file_list = []
    
    directory_files = os.list_dir(abs_path)
    
    for file_name in directory_files:
        file_path = os.path.join(abs_path, file_name)
        #if file_path is not a directory
        if not os.is_dir(file_path):
            file_list.append(file_path)
        else: #file_path is a directory; recurse
            create_list_of_files(file_path, file_list)
    
    if file_list:
        return file_list
    else:
        return []

        
    
find_duplicate_files("/a") # [["b/foo","c/baz"], ["c/quux", "c/xyzzy"]]










