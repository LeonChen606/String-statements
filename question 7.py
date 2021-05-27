#Name: Leon Chen
#Date: May 20
#This program finds how many vowels there are in a string

string=str(input("Enter the string:"))
index=0
length=len(string)
counter=0

#checking each letter to see if it's a vowel
while index<length:
    if string[index]=="a":
        counter=counter+1
        index=index+1
    elif string[index]=="e":
        counter=counter+1
        index=index+1
    elif string[index]=="i":
        counter=counter+1
        index=index+1
    elif string[index]=="o":
        counter=counter+1
        index=index+1
    elif string[index]=="u":
        counter=counter+1
        index=index+1
    else:
        index=index+1

#output data
print("There are", counter,"vowels in the string")
