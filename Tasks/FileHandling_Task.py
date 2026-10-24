'''1. Count Lines, Words, and Characters
Create a file sample.txt:
Python is easy to learn.
File handling is important.
Python is widely used.
Write a Python program to read the file and print:
Lines: 3
Words: 13
Characters: 75
'''
'''with open("Tasks/sample.txt","r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
character = len(content)

print("Lines : ",len(lines))
print("Words : ",len(words))
print("Character : ",character)'''

'''2. Copy Only Non-Empty Lines
Create input.txt:
Python

Java
     
C++
 
JavaScript
Write a program to copy only the non-empty lines into output.txt.
Expected output.txt:
Python
Java
C++
JavaScript'''

'''with open("Tasks/input.txt", "r") as file:
    lines = file.readlines()
with open("Tasks/output.txt", "w") as file:
    for line in lines:
        if line.strip():
            file.write(line)'''

'''3. Find the Most Frequently Used Word
Create story.txt:
python is easy
python is powerful
python is popular
Write a program to read the file and find the word that occurs most frequently.
Expected output:
Most frequent word: python
Count: 3'''

'''with open ("Tasks/story.txt","r") as file:
    content = file.read()

word = content.lower()
word1 = word.split()
d= {}

for s in word1:
    d[s] = d.get(s,0)+1

lar_count = 0
freq = 0

for s,count in d.items():
    if count > lar_count:
        lar_count = count
        freq = s
print("Most frequent word : ",freq)
print("Count : ",lar_count)'''

'''4. Separate Even and Odd Numbers from a File
Create numbers.txt:
10
25
36
41
50
63
72

Write a Python program to read the numbers from the file and create two files:
even.txt
10
36
50
72
odd.txt
25
41
63'''

'''with open("Tasks/numbers.txt","r") as file:
    content = file.read()
    word = content.split()
    
with open("Tasks/odd.txt","w") as file:
    for i in word:
        num = int(i)  
        if num % 2 != 0:   
            file.write(str(num) + "\n")   

with open("Tasks/even.txt","w") as file:
     for j in word:
        num = int(j)
        if num % 2 == 0:
            file.write(str(num) + "\n")'''  

'''5. Log File Analysis
Create app.log:
INFO: User login successful
ERROR: Database connection failed
INFO: User logout successful
WARNING: Disk space is low
ERROR: File not found
INFO: User login successful
Write a program to:
1.Read the log file.
2.Count INFO, WARNING, and ERROR messages.
3.Store only ERROR messages in errors.log.
Expected output:
INFO: 3
WARNING: 1
ERROR: 2
errors.log:
ERROR: Database connection failed
ERROR: File not found'''

with open("Tasks/app.log","r")as file:
    content = file.readlines()   

info_count = 0
warning_count = 0
error_count = 0

for line in content:
    if line.startswith("INFO:"):
        info_count += 1
    elif line.startswith("WARNING:"):
        warning_count += 1
    elif line.startswith("ERROR:"):
        error_count += 1

print("INFO :",info_count)
print("WARNING :",warning_count)
print("ERROR :",error_count)

with open("Tasks/errors.log","w") as file :
    for line in content :
        if line.startswith("ERROR:"):
            file.write(line)

        
