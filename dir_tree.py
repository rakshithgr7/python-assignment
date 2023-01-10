#9. Implement a program dir_tree.py that takes a directory as argument and prints all the files in that directory recursively as a tree. 
#Hint: Use os.listdir and os.path.isdir functions.

    
'''import os
path = os.getcwd()
list=os.listdir(path)
print(list)
print("enter the directory name")
directoryname=input()
for file in os.walk(directoryname):
        print(file)
        if os.path.isdir(file):
            for file in os.walk(file):
                            for f in file:
                             print(f)'''

import os
print("please enter the path")
path=input()
def tree(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            print(file)
        
            

    

    


         

   
    



