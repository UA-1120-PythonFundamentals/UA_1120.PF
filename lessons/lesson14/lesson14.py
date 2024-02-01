# file = open("lessons/lesson14/data/users.txt")

# text = file.read()
# print(text)
# file = open("lessons/lesson14/data/users.txt")
# text = file.readlines()
# print(text)

# file = open("lessons/lesson14/data/users.txt")
# text = file.readline()
# print(text)
# file.write("text")

# file = open("lessons/lesson14/data/users3.txt", "w")

# for i in range(10):
#     file.write(f"text_{i}\n")
# file.close()

# file = open("lessons/lesson14/data/users3.txt", "a")

# for i in range(5):
#     file.write(f"text_{i}{i}\n")
# file.close()

# try:
#     file = open("lessons/lesson14/data/users3.txt", "a")
#     for i in range(5):
#         file.write(f"text_{i}{i}\n")
# except FileNotFoundError as err:
#     print(err)
# finally:
#     file.close()


# with open("lessons/lesson14/data/users3.txt", "a") as file:
#     for i in range(5):
#         file.write(f"text_{i}{i}\n")

# with open("lessons/lesson14/data/users.txt") as file:

#     text = file.read()
#     print(text)

#     file.seek(0)
#     text = file.readlines()
#     print(text)

#     file.seek(0)
#     text = file.readline()
#     print(text)