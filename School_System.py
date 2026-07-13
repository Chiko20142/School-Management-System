class Person:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        print("Student:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print("Teacher:", self.name)
        print("Age:", self.name)
        print("Subject:", self.subject)
people = []

while True:
    print("\n School System")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. View Everyone")
    print("4. Count people")
    print("5. Search Person:")
    print("6. Exit")

    choice = input("Enter choice:")

    if choice == "1":
        name = input("Enter student's name:")
        age = int(input("Enter student's age:"))
        course = input("Enter course:")

        student = Student(name, age, course)

        people.append(student)

        print("Student successfully added!")

    elif choice == "2":
        name = input("Enter teacher's name:")
        age = int(input("Enter teacher's age:"))
        subject = input("Enter subject:")

        teacher = Teacher(name, age, subject)

        people.append(teacher)

        print("Teacher successfully added!")

    elif choice == "3":

        if len(people) == 0:
            print("No people found!")
            
        else:
            
            for person in people:
                person.introduce()
                print()

    elif choice == "4":
        print("Total people:", len(people))

    elif choice == "5":
        search_name = input("Enter name to search:")

        found = False

        for person in people:

            if person.name.lower() == search_name.lower():

                person.introduce()
                found = True
                break
            
        if not found:
            print("Person not found.")
            
    elif choice == "4":
        break
    



            
