class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_information(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Opeyemi", 24)
student2 = Student("Ayman", 3)

student1.student_information()
student2.student_information()