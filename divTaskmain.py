import numpy as np
import random as rnd
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def dicprint(dic):
    for i, a in dic.items(): print(i,a)
def divide_tasks(ls_P,nr_ofA,PpA = None):
    erg = False
    while erg == False:
        dic = {}
        lsas = []
        for i in range(nr_ofA): 
            for l in range(PpA):
                lsas.append(i+1)
        for p in ls_P:
            tmp_ls = []
            x = int((PpA*nr_ofA)/len(ls_P))
            for i in range(x):
                tryy = 0
                while True:
                    rndassnr = lsas[rnd.randint(0,len(lsas)-1)]
                    if not rndassnr in tmp_ls: break
                    tryy +=1
                    if tryy == 15: break
                lsas.remove(rndassnr)
                tmp_ls.append(rndassnr)
                tmp_ls.sort()
            dic[p] = tmp_ls
        if len(tmp_ls) == len(set(tmp_ls)): erg=True
    return dic

#Input section
clear()
try:
    number_people = int(input("How many are in the group? "))
except ValueError: 
    print("Error! Put in integer number!")
    exit()
clear()
ls_people = []
for i in range(number_people):
    ls_people.append(str(input("name of Person " +str(i+1)+ ": ")))
    clear()
try:
    number_tasks= int(input("How many tasks are to do? "))
except ValueError: 
    print("put in integer number")
    exit()
clear()
try:
    sol_tasks= int(input("How many solutions per task? "))
except ValueError: 
    print("put in integer number")
    exit()
clear()

dicprint(divide_tasks(ls_people,number_tasks,sol_tasks))
print()
input(">press ENTER to exit<")
clear()
