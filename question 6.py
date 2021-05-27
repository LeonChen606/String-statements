#Name: Leon Chen
#Date: May 20
#This program determines how many words are in a string

#input data
string=str(input("Enter the string:"))
index=0
length=len(string)
counter=0

#finding spaces that are in the string and then finding the amount of words
while index<=length-1:
    if string[index]==" ":
        counter=counter+1
    index=index+1
final=counter+1

print("The amount of words in the string is", final)
