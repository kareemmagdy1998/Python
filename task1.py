#task 1 / counting vowls:

test_string= "ahmed or aliaa"
vowls=["a","e","o","i","u"]

#function takes a string and vowls and returns occurences of each vowl
def occur(t,v):

    occure=[]
    for x in v:
        count=0
        for char in t :
            if char==x:
                count+=1

        occure.append(count) 

    print(f" a = {occure[0]}  , e = {occure[1]} , o = {occure[2]} , i = {occure[3]} , u = {occure[4]}")

occur(test_string,vowls)    

print("------------------------------------------------------------------------------------------")

#task 2 /sort (bubble sort):

#function takes type of sort(ascending or descending or both) and manually lets the user to fill the list and return sorted list

def sorting(asc='none',des='none'):

    arr=[]
    for x in range(5):
        int_input=int(input("enter a num\n"))
        arr.append(int_input)

    n=len(arr) 

    if des=="des":
        for i in range(n):
            for j in range(n-i-1)  :
                if arr[j] < arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        print(arr) 

    if asc=="asc":
        for i in range(n):
            for j in range(n-i-1)  :
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        print(arr) 


sorting("","des")    

print("------------------------------------------------------------------------------------------")


#task 3 / iti substring :

# function takes a string and a substring and returns how many times this substring appeard into that string

test_str="iti is my favourite inistitute it belongs to  our government thanks iti"


def substring(test,substring):

    count=0
    spilited_string=test.split()

    for word in spilited_string:
        if substring in word:
            count+=1

    print(f'{substring} appeared {count} times in this string')

substring(test_str,"iti")    

print("------------------------------------------------------------------------------------------")

#task 4 / remove vowls :

#function takes list of vowles charactares and remove this vowls from user input :

def remove_vowles(v):

   t_str= input("enter your string\n")

   for x in v:
    for char in t_str:
        if x==char:
            t_str= t_str.replace(char,"")

   print(t_str)   
  
remove_vowles(vowls)

print("-----------------------------------------------------------------------")

#task5/ location of i :

def locate_i(t_str):
    counter=0
    count_i=0
    for x in t_str:
        
        if x=="i":
            print(f'i is located at index {counter}') 
            count_i+=1
        counter+=1

    if count_i==0:
        print("i is not found")

locate_i("ikea")       

print("-----------------------------------------------------------------------")

#task 6 / multiplication :

#function takes a number and returns list of lists of it's multiplication numbers

def mult(num):

    sub_arr=[]
    res=[]
    i=1
    j=1
#this loop to append inner lists to our main list and clear inner list to the next number 
    while i<=num:
# this loop to append the numbers to the inner list of every number
        while j<=i:
            sub_arr.append(i*j) 
            j+=1

        res.append(sub_arr)
        sub_arr=[]
        i+=1
        j=1

    print(res)        
            
mult(4)
    
print("-----------------------------------------------------------------------")

#task 7 / pyramid :

#function takes number and builds mario pyramid has layers equal to that number

def pyramid(num):

    for x  in range(0,num):

        print(" "*(num-x)+"*" * x +"\n") 

pyramid(5)