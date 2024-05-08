"""f = open("C:/Users/jorda/Pictures/IMG-20221007-WA0026.jpg", "rb")
print(f.read())

f.close()

f2 = open("abv.jpg", 'w')
f2.write("b")
f2.close()
"""
import os

file = open('handling_file.txt', 'w+')
# msg = "Jordan"
for i in range(0, 100):
	file.write("Jordan\n")
file.close()

file1 = open('handling_file.txt', 'rt+')

for each in enumerate(file1):
	print(f'{file1.read()}')
file1.close()

os.remove('./handling_file.txt')
