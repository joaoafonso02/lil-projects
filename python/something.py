#function that returns max and min number o 3 input numbers
def maxNumb(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: return num1
    elif num2 >= num1 and num2 >= num3: return num2
    else: return num3

def minNumb(num1, num2, num3):
   if num1 <= num2 and num1 <= num3: return num1
   elif num2 <= num1 and num2 <= num3: return num2
   else: return num3

print("MAX NUMBER:")
print(maxNumb(int(input("number 1: ")),int(input("number 2: ")),int(input("number 3: "))))
print("\nMIN NUMBER:")
print(minNumb(int(input("number 1: ")),int(input("number 2: ")),int(input("number 3: "))))

#Converts a month shortcut to his month in extense 
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions[input("Enter: ")])

#triangle
i = 0
n = 5
while i <= 5:
    print(" " * (n-i) + "* " * i
    i += 1
#small game --> The Guesser
secretWord = "bruh"
guess = ""
while guess != secretWord:
    guess = input("Guess the word: ")
    if guess != secretWord: print("Wrong word! Try again!")
print("\nCONGRATS!!!  Well done!")

#returns a valid name
name = input("Your name: ")

if(name.isalpha or name.isspace):
    print(name)

#factorial
numero = int(input("Factorial of: ") )
resultado=1
fact=1

while count <= numero:
    resultado *= count
    fact += 1

print(resultado)

#function that returns the number of times in a certain interval that's divisable by 3
def smth(a, b) :
    counter = 0
    i = a
    while i < b:
        if i % 3 == 0: 
            counter += 1
        i +=1
    return counter

print(smth(a = int(input("from: ")), b = int(input("to: "))))

#returns the number of lines, words and characters of a given text file
file = open("sample.txt", "r")

lines, words, characters = 0, 0, 0

for line in file:
    lines += 1
    somth = line.strip("\n")
    words += len(somth.split())
    characters += len(line)

print("Number of lines: ", lines)

print("Number of words: ", words)

print("Number of characters: ", characters)

#checks if "fname" exists, is a directory or is a file
import os.path
import sys

fname = input("file name: ")
f = open(fname,"r") #reads the file if it exists
          
if not os.path.exists(fname):
    print("Doesn't exist")
if os.path.exists(fname):
    print("Exist")
if os.path.isdir(fname):
    print("It's a directory")
if not os.path.isfile(fname):
    sys.exit("It's a file")

#function that returns if a given number is prime or not
def primo(n): 
    if(n > 0):
        isPrime = True
        if(n == 1): isPrime = False
        for i in range(2,n):
            if(n % i == 0):
                isPrime = False
                break
        if(isPrime): print("Prime!\n")
        else: print("Not prime!\n")
    else: print("Negative numbers are not prime numbers\n")
while True:
   primo(int(input("number: ")))

#returns list read from the keyboard, sum, average
lista = list()
sumOf, average, count = 0, 0, 1
for i in range(0,50): 
    n = int(input("number: "))
    if(n == 0): break
    else: lista.append(n)
    sumOf += n
    average +=1
average = sumOf / (average-1)
print(lista, sumOf, average) 

#fuction that returns your list but the first and the last element are switched
def swaplist(newList1):
    print("Your list: ", newList1) 
    size = len(newList1)

    first = newList1[0]
    newList1[0] = newList1[size - 1]
    newList1[size - 1] = first

    print("Your new list below: ") 
    return newList1
newList1  = [1,2,3,4,5,6,7]

print(swaplist(newList1))

#fuction that returns your list properly orderded (w and w/ using the sort() function by python)
def orderlist(newList):
    size = len(newList)
    for i in range(0, size):
        for j in range(i+1, size):
            if(newList[j] < newList[i]):
                first = newList[i]
                newList[i] = newList[j]
                newList[j] = first
    #newList.sort() THIS IS THE EASIEST WAY
    #print(newList)
    print("Your list in crescent order:", newList)

    for i in range(0, size):
        for j in range(i+1, size):
            if(newList[j] > newList[i]):
                first = newList[i]
                newList[i] = newList[j]
                newList[j] = first
    #newList.sort(reverse  = True) THIS IS THE EASIEST WAY
    #print(newList)
    print("\nYour list in decrescent order:")
    return newList

newList  = [2,1,5,34,7,4,9,3,10]

print(orderlist(newList))
