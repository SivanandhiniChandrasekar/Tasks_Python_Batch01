#1.Count Lines,words,and characters
#Create a file sample.txt:
#python is easy to learn.
#file handling is important.
#python is widely used.
#write a python program to read the file and print:
#Lines:3
#Words:13
#characters:75



# File Handling 
# 1. Count Lines, Words, and Characters
# Create a file sample.txt:
# Python is easy to learn.
# File handling is important.
# Python is widely used.
# Write a Python program to read the file and print:
# Lines: 3
# Words: 13
# Characters: 75

f = open("sample.txt", "r")
data = f.read()

print("Lines:", len(data.splitlines()))
print("Words:", len(data.split()))
print("Characters:", len(data))

f.close()


#2nd code
#Copy Only Non-Empty Lines
#Create input.txt:
#Python

#Java
     
#C++
 
#JavaScript
#Write a program to copy only the non-empty lines into output.txt.
#Expected output.txt:
#Python
#Java
#C++
#JavaScript

f = open("input.txt", "r")
data = f.readlines()
f.close()

f = open("output.txt", "w")

for line in data:
    if line.strip():
        f.write(line)

f.close()

f = open("output.txt", "r")
print(f.read())
f.close()

#3. Find the Most Frequently Used Word
#Create story.txt:
#python is easy
#python is powerful
#python is popular
#Write a program to read the file and find the word that occurs most frequently.
#Expected output:
#Most frequent word: python
#Count: 3
f = open("../story.txt", "r")
data = f.read().lower()
f.close()

words = data.split()
word = max(set(words), key=words.count)

print("Most frequent word:", word)
print("Count:", words.count(word))

#4. Separate Even and Odd Numbers from a File
#Create numbers.txt:
#10
#25
#36
#41
#50
#63
#72
#Write a Python program to read the numbers from the file and create two files:
#even.txt
#10
#36
#50
#72
#odd.txt
#25
#41
#63

f = open("numbers.txt", "r")
data = f.readlines()
f.close()

even = open("even.txt", "w")
odd = open("odd.txt", "w")

for line in data:
    n = int(line)

    if n % 2 == 0:
        even.write(str(n) + "\n")
    else:
        odd.write(str(n) + "\n")

even.close()
odd.close()

print("Numbers separated successfully")
print("Check even.txt and odd.txt files")

'''
5. Log File Analysis
Create app.log:
INFO: User login successful
ERROR: Database connection failed
INFO: User logout successful
WARNING: Disk space is low
ERROR: File not found
INFO: User login successful
Write a program to:
Read the log file.
Count INFO, WARNING, and ERROR messages.
Store only ERROR messages in errors.log.
Expected output:
INFO: 3
WARNING: 1
ERROR: 2
errors.log:
ERROR: Database connection failed
ERROR: File not found
'''
f = open("app.log", "r")
data = f.readlines()
f.close()

info = 0
warning = 0
error = 0

f = open("errors.log", "w")

for line in data:
    if "INFO:" in line:
        info += 1
    elif "WARNING:" in line:
        warning += 1
    elif "ERROR:" in line:
        error += 1
        f.write(line)

f.close()

print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)


