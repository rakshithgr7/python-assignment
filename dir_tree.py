#9. Implement a program dir_tree.py that takes a directory as argument and prints all the files in that directory recursively as a tree. 
#Hint: Use os.listdir and os.path.isdir functions.

    
import os
#path = os.getcwd()
#list=os.listdir(path)
directoryname=(r"Downloads")
def rec(directoryname):
    print("|--"+directoryname)
    for file in os.listdir(directoryname):
        print('      |--%s' %file)
        if os.path.isdir(directoryname+"/"+file):
            rec(directoryname+"/"+file)
        
        
        
rec(directoryname)
        
                        

