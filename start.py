import sys
import os
from subprocess import call

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

#print call("ls -ls".split())

def insert(contents, index, value):
    contents.insert(index, value)

def replace(contents, index, value):
    contents[index] = value;

def append(contents, index, value):
    contents[index] = contents[index].replace('\n', value) 



#Makefile
call("git clone https://gist.github.com/fa9e22597b7303894be20882d9dfef73.git tmpMakefile".split())
call("mv ./tmpMakefile/Makefile ./Makefile".split())
call("rm -rf tmpMakefile".split())
f = open("./Makefile", "r")
makefileContents = f.readlines()
f.close()

#Name Project
projectName = "noNome"
for argv in sys.argv[1:]:
    if argv[0] != '-':
        projectName = argv
        break
print (projectName);
replace(makefileContents, 15, "NAME = " + projectName + '\n')
replace(makefileContents, 17, "SRC = " + projectName+".c\\\n")
replace(makefileContents, 20, "INCLUDES = includes/" + projectName + ".h\n")
#Directory src
try:
    os.mkdir("./src")
except FileExistsError:
    print("Directory src already exist")
mainFile = open("src/" + projectName + ".c", "w")
mainFile.write('#include "libft.h"\n#include "get_next_line.h"\nint main(void)\n{\nchar **line = NULL;\n\tif(get_next_line(-1, line) == -1)\n\t\tft_putendl("coucou");\n\treturn (0);\n}')
mainFile.close()

#Directory includes
try:
    os.mkdir("./includes")
except FileExistsError:
    print("Directory includes already exist")
includesFile = open("includes/" + projectName + ".h", "w")
includesFile.write("#ifndef " + projectName.upper() + "_H\n# define "+ projectName.upper() + "_H\n#endif")
includesFile.close()

#libft
def libft():
    call("git clone https://github.com/tlesven/libft ./libft".split())
    call("rm -rf ./libft/.git".split()) #Use remove
    print("Libft .git delete")
    append(makefileContents, 33, " $(LIBFIFLAGS)\n")
    append(makefileContents, 29, " $(LIBFFLAGS)\n")
    insert(makefileContents, 29, "\t\t$(MLIB)\n")
    insert(makefileContents, 26, "MLIB = make -C ./libft\n\n") 
    insert(makefileContents, 26, "LIBFIFLAGS = -I ./libft/includes\n")
    insert(makefileContents, 26, "LIBFFLAGS = -L ./libft -lft\n")
    insert(makefileContents, 43, "\t\tmake fclean -C ./libft\n")


#get_next_line
def gnll():
    call("git clone https://github.com/tlesven/get_next_line.git ./gnl".split())
    os.rename("./gnl/get_next_line.c", "./src/get_next_line.c")
    os.rename("./gnl/get_next_line.h", "./includes/get_next_line.h")
    insert(makefileContents, 18, "\t\tget_next_line.c\n\n")
    #call("rm -rf ./gnl/.git".split()) #Use remove
    #print ("gnl .git delete")
    #append(makefileContents, 25, "\\")
    #insert(makefileContents, 26, "\n\t./gnl/get_next_line.c")
    #insert(makefileContents, 19, "GNLIFLAGS = -I ./gnl\n")
    #append(makefileContents, 38, " $(GNLIFLAGS) \n")

if "-gnl" in sys.argv:
    libft()
    gnll()
elif "-libft" in sys.argv:
    libft()

#Gitignore
fileGitignore = open(".gitignore", "w")
fileGitignore.write("a.out\n")
fileGitignore.write("*.o\n")
fileGitignore.close()

#write makefile
f = open("Makefile", "w")
makefileContents = "".join(makefileContents)
f.write(makefileContents)
f.close()
