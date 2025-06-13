with open("student.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter name of student {i + 1}: ")
        file.write(name + "\n")
