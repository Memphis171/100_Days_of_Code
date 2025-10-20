import pandas as pd

#read  the data  with pandas
data = pd.read_csv("nato_phonetic_alphabet.csv")

#create a new dictionary from the dataframe
letter_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#get a word from the user and make sure it is upper case to match the new dictionary
word = input("Enter a word: ").upper()

#create a new list using the nato alphabet iterating off the word
letter_code = [letter_dict[letter] for letter in word]

print(letter_code)

#data frame iteration - {new_key:new_value for (index,row) in df.iterrows()}
#list/string - [new_item for n in list]
#dictionary - {new_key:new_value for (key,value) in dictionary}


#HERE is  the python console where I learned how  to iterate through dataframes, lists, strings, and dictionaries

# /Users/johnmckissack/PycharmProjects/100_Days_of_Code/.venv/bin/python /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py --mode=client --host=127.0.0.1 --port=65420
# import sys; print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['/Users/johnmckissack/PycharmProjects/100_Days_of_Code', '/Users/johnmckissack/PycharmProjects/100_Days_of_Code/Day_24_Snake_Game_with_Files', '/Users/johnmckissack/PycharmProjects/Day_25_Pandas'])
# PyDev console: starting.
# Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# name = "john"
# letters = [letter for letter in name]
# doubled_numbers = [n*2 for n in range(1,5)]
# names = ['john','erick','alexandria','peter','james','bliss']
# longnames = [name for name in names if len(name) > 4]
# all_caps = [n.upper() for n in longnames]
# import random
# student_scores = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
# import pandas as pd
# students_df = pd.DataFrame(student_scores)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "/Users/johnmckissack/PycharmProjects/100_Days_of_Code/.venv/lib/python3.13/site-packages/pandas/core/frame.py", line 782, in __init__
#     mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
#   File "/Users/johnmckissack/PycharmProjects/100_Days_of_Code/.venv/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 503, in dict_to_mgr
#     return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)
#   File "/Users/johnmckissack/PycharmProjects/100_Days_of_Code/.venv/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 114, in arrays_to_mgr
#     index = _extract_index(arrays)
#   File "/Users/johnmckissack/PycharmProjects/100_Days_of_Code/.venv/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 667, in _extract_index
#     raise ValueError("If using all scalar values, you must pass an index")
# ValueError: If using all scalar values, you must pass an index
# students_df = {'Name': names,}
# scores_only = [score for (name,score) in student_scores.items()]
# students_df = pd.DataFrame({'Name':names,'Score':scores_only})
# print(students_df)
#          Name  Score
# 0        john     56
# 1       erick     13
# 2  alexandria     90
# 3       peter     77
# 4       james     43
# 5       bliss     96
#


