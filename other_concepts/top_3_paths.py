#Coding Challenge
#Read & parse through a log file of timestamps, user_ids, and their paths & return the top 3 paths visited

import sys
from sys import argv  # this allows you to not need to hardcode the file's name


class Top3Paths(object):

    def make_paths_dict(self, filename):
        """Given a file, makes a dictionary with userid as the key and array of that user's paths"""

        script, filename = argv
        self.paths_dict = {}
        with open(filename) as f:
            for line in f:
                line_array = line.rsplit()
                for i in range(1,len(line_array)-1):
                    user = line_array[i]
                    path = line_array[i+1]
                    if user in self.paths_dict:
                        self.paths_dict[user].append(path)
                    else:
                        self.paths_dict[user] = [path]

        self.make_count_dict(self.paths_dict)


    def make_count_dict(self, paths_dict):
        """Takes the paths dictionary and creates a dictionary of count of user's paths"""

        self.count_dict = {}
        for user, full_path_array in paths_dict.iteritems():
            for i in range(len(full_path_array)):
                if (i+2) > (len(full_path_array)-1):
                    break
                sub_path_array = []
                sub_path_array = full_path_array[i:i+3]
                sub_path_tuple = tuple(sub_path_array)  # dictionary keys must be immutable
                self.count_dict[sub_path_tuple] = self.count_dict.get(sub_path_tuple, 0) + 1
        
        self.find_top_3_paths(self.count_dict)


    def find_top_3_paths(self, count_dict):
        ascending_paths_array = sorted(count_dict, key=count_dict.__getitem__, reverse=True)
        top_3_paths = ascending_paths_array[0:3]
        return top_3_paths


if __name__ == "__main__":
    filename = sys.argv[1]
    generator = Top3Paths()
    generator.make_paths_dict(filename)
