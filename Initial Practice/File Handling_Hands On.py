
# file = open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt') #since Test.txt is present in this path..hence we can put the name directly...OR else we have to give the path of the file
# print (file.read())
# file.close() # We should always close the file

# OUTPUT::::
# All the data is displayed

##################################################################################################################################

# file = open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt')
# print (file.read(5)) #Number 5 represents 5 characters from the file
# file.close()
#
# OUTPUT:::: #space/next line is considered a character
# abc
# 1
###################################################################################################################################

# file = open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt')
# print (file.readline()) # .readline() reads the file line by line.....3 readline means 3 rows will be displayed
# print (file.readline())
# print (file.readline())
# file.close()
#
# OUTPUT::::
# abc
# 123zxc
# def
###########################################################################################################################
# Q. Print all the data in the file line by line by readline method:
#
# file = open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt')
# line = file.readline()
#
# while line!="":         # when line is not blank, then only it will enter this while loop
#     print (line)
#     line = file.readline()
#
# file.close()
#
# OUTPUT:::::
# abc
# 123zxc
# def
# 456
# ghi
# 789
# jkl
############################################################################################################################


# file = open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt')
# print(file.readlines()) ### ['abc\n', '123zxc\n', 'def\n', '456\n', 'ghi\n', '789\n', 'jkl']
# print(file.read().splitlines()) ### it will do the same function as file.readlines()....since in readline extra '\n' was coming hence using this..
# file.close()
###############################################################################################################################

# file = open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt')
#
# for line in file.readlines(): ###this will make the data in LIST in the file
#     print (line)
# file.close()
#
# # OUTPUT:::::
# # abc
# # 123zxc
# # def
# # 456
# # ghi
# # 789
# # jkl
#############################################################################################################################

### WRITE METHOD::::::::::
# Read the file
# Reverse the data in file
# Write the list back

with open('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt', 'r') as reader: #'r' is for read mode
    content = reader.readlines() ### this is converting the data in file to list
    reversed(content)  #### this is reversing the list

    with open ('C:\\Users\gaura\Desktop\Selenium with PYTHON\Test1.txt', 'w') as writer: #'w' is for write mode
        for line in reversed(content):
            new_content = writer.write(line)
