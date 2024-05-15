import os

file_1 = open('demo.txt', 'r')
# for word in file_1:
#     print(word)

# print(file_1.read(2))
# file_1.close()

print(file_1.readlines())
file_1.close()


