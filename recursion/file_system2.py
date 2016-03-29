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