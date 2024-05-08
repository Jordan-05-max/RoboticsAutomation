import os

f = 'testing.txt'
with open(f, 'w+') as file:
#	file = open(f, 'wt')
	file.write('We are testing! ')
file.close()

file1 = open(f, 'rt')
print(file1.read())
file1.close()

if os.path.exists(f'./{f}'):
	os.remove(f)
