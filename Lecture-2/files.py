# file = open("hello.txt", "r")
#
#
#
#
#
# # for line in file:
# #     print(line, end="")
# #
# # for line in file:
# #     print(line, end="")
# #
# # file.close()
#
# while True:
#     line = file.read(40)
#     print(line, end="")
#     if len(line)==0 :
#         break



file = open("hello.txt", "w")

file.write("Mai hu khalnayak")

file2 = open("hello.txt", "a")

file2.write("Mai hu khalnayak ka bhai")



