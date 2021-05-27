#Name: Leon Chen
#Date: May 20
#this program determines whether or not a string is a palimdrone or not

#input data
string1=str(input("Enter a string:"))
string2=""
length=len(string1)

#determining the last index
counter=length-1

#flipping the string
while counter>=0:
    letter=str(string1[counter])
    string2=string2+letter
    counter=counter-1
    
if string1 == string2:
    print("This string is a palimdrome!")
else:
    print("This string is not a palimdrome.")







