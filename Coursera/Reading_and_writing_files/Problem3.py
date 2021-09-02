# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:03:46 2021

@author: Toan Thang
"""

#%%
def problem3_1(txtfilename):
    infile = open(txtfilename)
    sum = 0
    for line in infile:
        sum = sum + len(line)
        print(line, end="") # the file has "\n" at the end of each line already
    print("\n\nThere are", sum, "letters in the file.")
    infile.close()
    
#%%
def problem3_2(collection):
    for i in collection:
        print(i)
    
nlis = [23,64,23,46,12,24]          # list
atup = ("c","e","a","d","b")        # tuple
str1 = "Rumplestilskin"             # string


#%%
def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    pass # replace this pass (a do-nothing) statement with your code
    tup_month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    print(str(tup_month[month-1]), str(day) + ",", str(year))
    
#%%
def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    dic = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July":7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    print(str(dic[mon]) + "/" + str(day) + "/" + str(year))
    
#%%

def problem3_5(name):
    """ Looks up the phone number of the person whose name is name """
    
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241", \
                      "james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    pass # replace this pass (a do-nothing) statement with your code
    
    if name not in phone_numbers:
        return
    else: print(phone_numbers[name])

#%%
def problem3_7(csv_pricefile, flower):
    pass # replace this pass (a do-nothing) statement with your code
    import csv
    fin = open(csv_pricefile)
    read = csv.reader(fin)
    for row in read:
        if (row[0]==flower):
            print(row[1])
    