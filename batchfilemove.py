#write on 17/04/2020
import os
import shutil
import sys

def batchfilemove(name_list, suffix, in_dir, out_dir):
    '''
    move images according to image name list
    :param name_list: name list of images without suffix to move, suggest '.txt' file
    :param suffix: suffix of images
    :param in_dir: directory for input
    :param out_dir: directory to store selected images
    :return:
    '''
    with open(name_list, "r") as f1:
        for name in f1:
            name = name.split('\n')[0] + suffix # can be adjusted, name without suffix
            shutil.copyfile(in_dir + name, out_dir + name)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('3 auguments are need.')
        exit(1)

    batchfilemove(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
