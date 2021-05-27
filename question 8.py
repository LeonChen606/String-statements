#Name: Leon Chen
#Date: May 20
#This program combines 2 strings

#input data
string1=str(input("Enter the first string:"))
string2=str(input("Enter the second string:"))
stringMix=""
length=len(string1)
index=0

#finding each individual character and combining the words
while index<length:
    stringMix=stringMix + string1[index] + string2[index]
    index=index+1
print("The final string is "+stringMix)
