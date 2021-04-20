# VARIABLES ---------------------------------------------------------
# name, age = "Istiak", 21
# age = 21
# numbers = [1, 2, 3, 4]
# pi = 3.14
# print(name, age, pi, number)
# print(type(name))


# DYNAMICALLY TYPE ---------------------------------------------------------
# name: str = "Istiak"
# isAdult: bool = True

# STRINGS ---------------------------------------------------------
# brand = "Acryntix"
# print(brand.upper())  # convert to uppercase
# print(brand.replace('A', 'a'))  # replace A with lowercase a
# print(len(brand))  # length of brand
# print("tix" in brand)  # returns true
# print("tix" not in brand)  # returns false

# MULTIPLE LINE FORMATTING ---------------------------------------------------------
# comment = """
# Yo
# My
# name
# is Istiak
# """
#
# print(comment)

# FORMATTING STRINGS ---------------------------------------------------------
# name = "Istiak"
# email = f"""
# hello {name}, how are you?
# age {19+2}
# """
# print(email)

# ARITHMETIC OPERATORS ---------------------------------------------------------
# print(5 + 5)
# print(10 - 5)
# print(5 * 5)
# print(25/5)
# print(10 % 3)  # modulus, gives remainder
# print(5 ** 5)  # to the power of

# LOGICAL OPERATORS ---------------------------------------------------------
# print(10 > 5)
# print(10 >= 10)
# print(10 < 10)
# print(10 <= 10)
# print(10 != 10)
# print(10 == 10)

# LOGICAL OPERATIONS ---------------------------------------------------------
# print((10 > 5) and (1 > 3))
# print((10 > 5) or ("A" == "A"))
# print("Me" == "I")
# print(not("Me" == "I"))  # reverses

# ASSIGNMENT OPERATORS ---------------------------------------------------------
# number = 0
# number +=1
# number -=1
# number *=1
# number /=1
# number **=1
# print(number)

# IF STATEMENTS ---------------------------------------------------------
# number = 15
#
# if number > 0:
#     print(f"number {number} is positive")
# elif number == 0:
#     print(f"{number} is zero")
# else:
#     print(f"{number} is negative")

# LISTS ---------------------------------------------------------
# numbers = [1, 2, 3, 4, -1, -20, ["A", "B"]]
# print(numbers[0])
# print(numbers[6][0])

# TERNARY IF STATEMENTS ---------------------------------------------------------
# number = -1
# message = "positive" if number > 0 else "0 or negative"
# print(message)

# LIST METHODS ---------------------------------------------------------
# numbers = [1, 2, 3, 4, -1, -20, ["A", "B"]]
# numbers.sort()  # sorts in order
# numbers.reverse()  # reverse order
# numbers.append(1000)  # adds onto
# numbers.remove(1)  # removes
# numbers.pop()  # removes last element
# numbers.clear()  # clears numbers list
# del numbers[0]  # removes at index 0
# del numbers[0:3]  # removes everything from index 0 to 3 (3 is exclusive)

# print(-20 in numbers)
# print(numbers)

# numbersList = [1, 1]
# numbersSet = {1, 1}  # duplicates not allowed in sets
# sets have same functions as lists e.g. clear, remove, pop etc
# sets are unordered

# print(numbersList, numbersSet)
# print(person)

# UNION ---------------------------------------------------------
# union takes everything from both sets and puts it inside another set
# lettersA = {"A", "B", "C", "D"}
# lettersB = {"A", "E", "F"}
# union = lettersA | lettersB
# print(f"Union = {union}")

# INTERSECTION ---------------------------------------------------------
# intersection is whatever occurs in both sets
# intersection = lettersA & lettersB
# print(f"Intersection = {intersection}")

# DIFFERENCE ---------------------------------------------------------
# everything which is in lettersA but not in lettersB
# difference = lettersA - lettersB
# differenceB = lettersB - lettersA
# print(f"Difference = {difference}")
# print(f"DifferenceB = {differenceB}")

# DICTIONARIES ---------------------------------------------------------

# person = {
#     "name": "Istiak",
#     "age": 21,
#     "country": "UK"
# }
#
# #  e.g.
# #  name = key
# #  value = Istiak
#
#
# # keys have to be unique, cannot be duplicates
# print(person["name"])  # gets name "Istiak"
# print(person["age"])
# print(person["country"])
# print(person.keys())  # returns all the keys
# print(person.values())  # returns all the values
# print(person.get("age"))  # gets age
#
# person["age"] = 20
# print(person.get("age"))

# LOOPS ---------------------------------------------------------

# names = ["Istiak", "Taseen", "Tahmed", "Ilan"]  # list
# names = {"Istiak", "Taseen", "Tahmed", "Ilan"}  # set

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# For loop ---------------------------------------------------------
# for name in names:
#     print(name)

# person = {
#     "name": "Istiak",
#     "age": 21,
#     "country": "UK"
# }

# for key in person:
#     # print(key)
#     print(f"key:{key} value: {person[key]}")

# better format
# for key, value in person.items():
#         print(f"key:{key} value: {value}")


# Loop Exercise ---------------------------------------------------------

# addedNumbers = 0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# # loops through all numbers and adds them together
# for number in numbers:
#     addedNumbers += number
#
#
# print(f"Result = {addedNumbers}")

# While loop ---------------------------------------------------------

# number = 0
#
# while number < 10:
#     print(number)
#     number+=1
# else:
#     print("Else in while loop")

# Break ---------------------------------------------------------

# number = 0
#
# while number < 10:
#     if number == 5:  # when number reaches 5, break out of the loop
#         break
#     number+=1
#     print(number)

# Continue ---------------------------------------------------------

# number = 0
#
# while number < 10:
#     number += 1
#     if number < 5:  # if number is less than 5, continues
#         continue
#     print(number)

# For Loop break and continue example ---------------------------------------------------------

# number = 0
#
# for n in [1, 2, 3, 4, 5, 6, 7]:
#     # if n < 5:
#     #     continue
#     # print(n)
#     if n == 5:
#         break
#     print(n)

# FUNCTIONS ---------------------------------------------------------

# def greet():
#     print("Hello, how are you?")
#
#
# greet()

# PARAMETERS AND ARGUMENTS ---------------------------------------------------------

# def greet(name, age):
#     print(f"Hello {name}, how are you?")
#     print(f"I know you are {age} years old")
#
#
# greet("Istiak", 21)
# greet("Taseen", 12)
# greet("Tahmed", 10)
# greet("Ilan", 8)

# def greet(name, age=0): sets default age as 0

# RETURN VALUES FROM FUNCTIONS ---------------------------------------------------------

# def is_adult(age):
#     # if age >= 18:
#     #     # print("Adult :)")
#     #     return True
#     #
#     # else:
#     #     # print("Not yet an adult :(")
#     #     return False
#     return age >= 18
#
#
# result = is_adult(50)  # returns boolean value, can be true or false
# print(result)

# def convertGender(gender="unknown"):
#     if gender.upper() == "M":
#         return "Male"
#     elif gender.upper() == "F":
#         return "Female"
#     else:
#         return f"Gender {gender} is unknown"
#
#
# print(convertGender("F"))
# print(convertGender("f"))
# print(convertGender("M"))
# print(convertGender("m"))
# print(convertGender("yo"))

# BUILT IN FUNCTIONS AND IMPORT STATEMENT ---------------------------------------------------------

# import math
#
# print(math.pi)
# print(math.isqrt(25))

# ONLY IMPORT ISQRT
# from math import isqrt


# CREATING MODULES ---------------------------------------------------------

# import calculator
#
# print(calculator.add(5,5))
# print(calculator.subtract(5,5))
# print(calculator.multiply(5,5))
# print(calculator.divide(5,5))

# ONLY IMPORT SPECIFIC METHOD/FUNCTION
# from calculator import add
# from calculator import subtract
# from calculator import multiply
# from calculator import divide
# print(divide(5,5))


# CLASSES AND OBJECTS ---------------------------------------------------------

# # class is just a blueprint for creating objects, its just a template
# class Phone:
#     def __init__(self, brand, price):  # constructor
#         self.brand = brand
#         self.price = price
#
#     # Call Behaviour
#     def call(self, phoneNumber):  # refers to current instance of current class
#         print(f"{self.brand} is calling {phoneNumber}")
#
# OnePlus7TPro = Phone("OnePlus 7T Pro", 800)
# iPhone = Phone("Apple iPhone 7 Plus", 720)
#
# # Properties
# print(OnePlus7TPro.brand)
# print(OnePlus7TPro.price)
# print(iPhone.brand)
# print(iPhone.price)
#
# # Behaviour
# OnePlus7TPro.call("999")
# iPhone.call("999")


# Printing Objects ---------------------------------------------------------

# class is just a blueprint for creating objects, its just a template
# class Phone:
#     def __init__(self, brand, price):  # constructor
#         self.brand = brand
#         self.price = price
#
#     # Call Behaviour
#     def call(self, phoneNumber):  # refers to current instance of current class
#         print(f"{self.brand} is calling {phoneNumber}")
#
#     # CHANGES MADE HERE TO PRINT OBJECT
#     # OVERRIDE STR METHOD
#     def __str__(self) -> str:  # -> str signifies that this returns string
#         return f"Brand {self.brand} \nPrice = {self.price}"
#
#
# OnePlus7TPro = Phone("OnePlus 7T Pro", 800)
# iPhone = Phone("Apple iPhone 7 Plus", 720)
#
# print(OnePlus7TPro)
# print(iPhone)


# WORKING WITH DATES ---------------------------------------------------------

# import datetime
#
# print(datetime.datetime.now())  # current date and time
# print(datetime.date.today())  # today's date
# print(datetime.datetime.now().time())  # time only


# IMPROVED VERSION
# from datetime import datetime
# from datetime import date
#
# print(datetime.now())  # current date and time
# print(datetime.now().day)  # current day
# print(datetime.now().month)  # current month
# print(datetime.now().year)  # current year
# print(date.today())  # today's date
# print(datetime.now().time())  # time only


# Formatting dates
# from datetime import datetime
# from datetime import date
#
# now = datetime.now()
# print(now)
#
# print(now.strftime("%d/%m/%Y %H:%M:%S"))  # Date/Month/Year Hour:Minute:Second
# print(now.strftime("%d-%m-%Y %H:%M:%S"))  # Date-Month-Year Hour:Minute:Second
# print(now.strftime("%d-%B-%Y %H:%M:%S"))  # B -> month name in full text format
# print(now.strftime("%d-%b-%Y %H:%M:%S"))  # b -> month name in abbreviation text format
# print(date.today().strftime("%d-%m-%Y"))
# print(date.today().strftime("%d-%B-%Y"))

# CREATING FILES ---------------------------------------------------------

# DIFFERENT FUNCTIONS
# w = write
# r = read only
# r+ = reading and writing
# a = append

# VARIABLE 'file' CREATES FILE CALLED 'data.csv'
# file = open("./data.csv", "w")


# file = open("./data.csv", "a")
# # file.write("id,name,email\n")
# # file.write("1,Istiak,isti@gmail.com\n")
# # file.write("2,Acryntix,acryntix@gmail.com\n")
# file.write("3,Ruddro,ruddro@gmail.com\n")
# file.close()

# READING FROM FILES ---------------------------------------------------------

# file = open("./data.csv", "r")
#
# # print(file.read())  # reads entire file
#
# # Reads line by line
# # for line in file:
# #     print(line)
#
# # List with each line
# print(file.readlines())
# file.close()

# BETTER WAY TO WORK WITH FILES ---------------------------------------------------------

#
# with open("./data.csv", "r") as file:
#     print(file.read())


# Check if file exists
# import os.path
#
# filename = 'data.csv'
#
# if os.path.isfile(filename):  # returns boolean, if file exists
#     with open(filename, "r") as file:
#         print(file.read())
# else:
#     print(f"file {filename} does not exist")


# FETCHING DATA FROM INTERNET ---------------------------------------------------------

# from urllib import request
#
# r = request.urlopen("http://www.google.com")
# print(r.getcode())  # returns status code
# print(r.read())

# FETCHING JOKES FROM INTERNET ---------------------------------------------------------

# from urllib import request
# import json
#
# url = "http://official-joke-api.appspot.com/random_joke"
# r = request.urlopen(url)
# print(r.getcode())  # returns status code
# data = r.read()
# jsonData = json.loads(data)
# print(jsonData)
#
# class Joke:
#
#     def __init__(self, setup, punchline) -> None:
#         self.setup = setup
#         self.punchline = punchline
#
#     def __str__(self) -> str:
#         return f"setup {self.setup} punchline {self.punchline}"
#
#
# jokes = []
#
# for j in jsonData:
#     setup = j["setup"]
#     punchline = j["punchline"]
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(f"Got {len(jokes)} jokes")
#
# for joke in jokes:
#     print(joke)


# PIP AND MODULES ---------------------------------------------------------

# Requests module

# import requests
# import json
#
# url = "http://official-joke-api.appspot.com/random_joke"
# response = requests.get(url)
# print(response.status_code)  # returns status code
# jsonData = json.loads(response.text)
# print(jsonData)
#
# class Joke:
#
#     def __init__(self, setup, punchline) -> None:
#         self.setup = setup
#         self.punchline = punchline
#
#     def __str__(self) -> str:
#         return f"setup {self.setup} punchline {self.punchline}"
#
#
# jokes = []
#
# for j in jsonData:
#     setup = j["setup"]
#     punchline = j["punchline"]
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(f"Got {len(jokes)} jokes")
#
# for joke in jokes:
#     print(joke)


# TEXT TO SPEECH ---------------------------------------------------------
# import pyttsx3
# import requests
# import json
#
# url = "http://official-joke-api.appspot.com/random_joke"
# response = requests.get(url)
# print(response.status_code)  # returns status code
# jsonData = json.loads(response.text)
# print(jsonData)
#
# class Joke:
#
#     def __init__(self, setup, punchline) -> None:
#         self.setup = setup
#         self.punchline = punchline
#
#     def __str__(self) -> str:
#         return f"setup {self.setup} punchline {self.punchline}"
#
#
# jokes = []
#
# for j in jsonData:
#     setup = j["setup"]
#     punchline = j["punchline"]
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(f"Got {len(jokes)} jokes")
#
# for joke in jokes:
#     print(joke)
#     pyttsx3.speak("Setup")
#     pyttsx3.speak(joke.setup)
#     pyttsx3.speak("The Punchline")
#     pyttsx3.speak(joke.punchline)
#

# END ---------------------------------------------------------



