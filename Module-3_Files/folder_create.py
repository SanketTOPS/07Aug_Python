import os

#os.mkdir('Myfolder')  # for folder create

#os.chdir('Newfolder')
#os.mkdir("Subfolder")


#os.chdir("Newfolder/Subfolder")
#os.mkdir("myfolder")

"""os.chdir("Newfolder/Subfolder/myfolder")
open("test.txt","w")"""

#os.remove('hello.txt')

"""os.chdir("Newfolder/Subfolder/myfolder")
os.remove('test.txt')"""

#os.removedirs('Myfolder')

os.chdir("Newfolder")
os.removedirs('Subfolder')
