class Student_List:
    def __init__(self):
        self.list = []
        
    def add_student(self, name, age, mark):
        self.list.append([name, age, mark])
        
    def remove_student(self, name):
        for i, item in enumerate(self.list):
            if item[0] == name:
                del self.list[i]
    
    def the_highest_mark(self):
        highest = 0
        for i in self.list:
            if i[2] > highest:
                highest = i[2]
                student_name = i[0]
                student_age = i[1]
        print(f'Student {student_name}, age {student_age} has the highest mark {highest}')

    def the_average_mark(self):
        total = 0
        for i in self.list:
            total += i[2]
        average = float(total/len(self.list))
        print(f'the average mark is {average:.2}')
        
    def display(self):
        for i in self.list:
            print(f'Student {i[0]}, age {i[1]}, mark {i[2]}')
        print()
        
x = Student_List()
x.add_student('mai',12, 7.5)
x.add_student('huong',14, 8)
x.add_student('giang',16, 10)

x.display()
x.remove_student('mai')
x.display()
x.the_highest_mark()
x.the_average_mark()
