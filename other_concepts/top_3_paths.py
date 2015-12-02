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
        """Takes the csv formatted file and makes a dictionary with userid as the key and array of that user's paths"""

        
        line = csv_text.split('/n')
        for element in line[1:]:
            pass
   

    # def find_top_3_sites(filename):
    #     pass

if __name__ == "__main__":
    filename = sys.argv[1]
    generator = Top3Paths()
    a = generator.make_paths_dict(filename)


