import os
import sys
import re
from os import listdir
from os.path import isfile, join

if sys.argv[1] is None or sys.argv[2] is None:
    print("param error")
    sys.exit(0)

file_mock =  sys.argv[1]
column_value = int(sys.argv[2])
column_value -= 1
column_end_value = 0
column_end_value = ((column_value) + 8)
file_split = file_mock.split("/")
new_file_list = []
same_file_rewriting = []
path_files = ""

for is_file in file_split:
    search_file_name = re.search('.txt', is_file)
    if (hasattr(search_file_name, 'pos')):
        print(search_file_name)
        new_file = "new-file" + search_file_name.string
    else:
        path_files = path_files + is_file + "/"

if isfile(file_mock):
    print("open file => "+file_mock)
    with open(file_mock, "r") as read:
        for file_line in read:
            print(file_line)
            print("\n")
            print(file_line[column_value:column_end_value])

            line_data = file_line[column_value:column_end_value]
            search_data_1  = re.search('20181001', line_data)
            search_data_2  = re.search('20181002', line_data)
            search_data_3  = re.search('20181003', line_data)
            search_data_4  = re.search('20181004', line_data)
            search_data_5  = re.search('20181005', line_data)
            search_data_6  = re.search('01102018', line_data)
            search_data_7  = re.search('02102018', line_data)
            search_data_8  = re.search('03102018', line_data)
            search_data_9  = re.search('04102018', line_data)
            search_data_10 = re.search('05102018', line_data)

            if ((hasattr(search_data_1, 'pos')) or (hasattr(search_data_2, 'pos')) 
                or (hasattr(search_data_3, 'pos')) or (hasattr(search_data_4, 'pos')) 
                or (hasattr(search_data_5, 'pos')) or (hasattr(search_data_6, 'pos'))
                or (hasattr(search_data_7, 'pos')) or (hasattr(search_data_8, 'pos'))
                or (hasattr(search_data_9, 'pos')) or (hasattr(search_data_10, 'pos'))):
                print("return true ===>>>")
                new_file_list.append(file_line)
            else:
                same_file_rewriting.append(file_line)
        read.close()

    rewriting = open(file_mock, "w")
    rewriting.writelines(same_file_rewriting)
    rewriting.close()

    if(new_file_list != []):
        new_file_writing = open(path_files + new_file, "w")
        new_file_writing.writelines(new_file_list)
        new_file_writing.close()

else:
    print("is not a valid file")



