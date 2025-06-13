# Writing data
with open("marks.txt", "w") as file:
    for _ in range(5):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        file.write(f"{name} {marks}\n")

# Reading and filtering
print("\nStudents with marks > 75:")
with open("marks.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split()
        if int(marks) > 75:
            print(name)
