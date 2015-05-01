#! /usr/bin/python3

import os, re
from pprint import pprint
import doctest


def count_files_by_keywords(root_dir, keyword):
    '''
    >>> pprint(count_files_by_keywords('.', r'\d{3}-\d{3}-\d{4}'))
    {'.': 1, './test1': 1}

    :param root_dir:
    :param keyword:
    :return:
    '''
    out_put = {}
    for dir_name, dir_list, file_list in os.walk(root_dir):
        if file_list:
            file_count_with_keyword = 0

            for file in file_list:
                file_path = dir_name + '/' + file
                if check_file(file_path, keyword):
                    file_count_with_keyword += 1
            out_put[dir_name] = file_count_with_keyword

    return out_put

def check_file(file_name, keyword):
    '''
    >>> check_file('./to_test.txt', r'\d{3}-\d{3}-\d{4}')
    True

    :param file_name:
    :param keyword:
    :return:
    '''
    with open(file_name) as f:
        for line in f:
            search = re.search(keyword, line)
            if search:
                return True
    return False


file_name = 'to_test.txt'
keyword = r'\d{3}-\d{3}-\d{4}'
# print(check_file(file_name, keyword))
# test_walk()


# pprint(count_files_by_keywords(os.getcwd(), keyword))
# check_file(file_name, keyword)
#
f = open('./to_test.txt', 'r+')
for line in f:
    print(line)
f.close()


if __name__ == '__main__':
    doctest.testmod()