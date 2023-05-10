
print("------------------------------------------------------------------------------------------------\n\n\n")
# function takes length and start and generates an array

def gen_arr(len,start):
    arr=[]
    for i in range(len):
        arr.append(start)
        start+=1
    return arr
print(gen_arr(6,2))

print("------------------------------------------------------------------------------------------------\n\n\n")
# fizz buzz function takes number as argument and return fizz if divisible by 3 and buzz if divisible by 5

def fizz(number):
    if number%3==0 and number%5==0:
        print("fizz buzz")
    elif number%3==0 :
        print("fizz") 
    elif number%5==0 :
        print("buzz")
    else:
         print(f"{number} is not divisible by neither 3 nor 5\n")   
fizz(7)                         

print("-----------------------------------------------------------------------------------------------\n\n\n")
#function takes a string and returns if it is a balindrome or not and print the string reversed

def palind(string):
    if string==string[::-1]:
        print(f"{string} is a palindrome\n")
        print(string[::-1])
    else:
        print(f"{string} is not a palindrome\n") 
        print(string[::-1])   
palind("ibrahim")
palind("madam")

print("-----------------------------------------------------------------------------------------------\n\n\n")
#function check if the name is not empty and has no numerical values

def validate():
    user_name = input("enter your name\n")

    while user_name.isalpha()==False or len(user_name)==0:
        print(f"{user_name} is not a valid name")
        user_name = input("enter your name\n")
    
    email=input("Enter your email address\n")
    print(f"your email address is {email}\nyour name is {user_name}")

validate()    

print("-----------------------------------------------------------------------------------------------\n\n\n")
# program which repeatedly reads numbers until the user enters “done”.

list_num=[]
num=input('enter a number')
while num!="done":
    if num.isnumeric()==True:
        num=int(num)
        list_num.append(num)
        num=input('enter a number')
    else:
        print("Please enter a number")

print(f"you entered {len(list_num)} numbers and the average is {sum(list_num)/len(list_num)}")

print("-----------------------------------------------------------------------------------------------\n\n\n")
#function return the longest ordered substring

def longest_alpha_substring(s):
    longest = ""
    current = ""
    for i in range(len(s)):
        if i == 0 or s[i] >= s[i-1]:
            current += s[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = s[i]

    if len(current) > len(longest):
        longest = current

    print("Longest substring in alphabetical order is:", longest)


longest_alpha_substring("abcdeabcdefg")
print("-----------------------------------------------------------------------------------------------\n\n\n")
#hangman
import random

def hangman():
    list=["kareem","hashem","iti","python","dev","web"]
    choice=random.choice(list)
    res=[]
    dashed=[]
# compare string    
    str_dashed="" 
# creat two lists of my random word list with actual characters of word and list with dashes equal to number of characters
    for i in choice:
        res.append(i)
        dashed.append("-")
        
    nam=input("enter your name please\n\n")
    count = 0

    while count!=7:
# check if the user has already won the game
        if str_dashed==choice:
            print(f"you won , the word is {str_dashed}\n\n")
            break;
# check if the user entered right guessing     
        else:  
            str_dashed=""  
            x=input(f"Enter your guess {nam}\n\n")
            #if the guess is right then append the letter in same index as the list and replace it with "-" to avoid errors when the letter is rebeated
            if x in res:
                dashed[res.index(x)]=x
                res[res.index(x)]="-"
            #loop on the guess list and turn it to a string
                for i in dashed:
                    str_dashed+=i
                print(f"right guess,{str_dashed}\n\n")
# if the guess is wrong print number of guesses left                
            else:
                count+=1 
                print(f"wrong guessing ,you have {7-count} turns left\n")
                
    if count==7:
        print("You have lost the game ")            

hangman()

