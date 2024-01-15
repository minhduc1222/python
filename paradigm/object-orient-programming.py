# object orient: objects are the key of the paradigm( everything in python revolves around objects and classes concepts). 
    # object: instance of a class, contains data member and method function.
    # the code also relates data member and method, supporting encapsulation with the help of inheritance
        # (encapsulation means data bundling( goi_ghem), hiding data within a class, allows for data organization, protection that enables data visibility and accessibility to be modified)
        
# advantage: relations of real world entities
            # code reusability
            # data hiding

# but it has cons like slow speed, not suitable for all

class emps:
    def __init__(self, name, age):
        self.emp_name = name
        self.emp_age = age
    
    def info(self):
        print(('hello %s, you are %s years old') % (self.emp_name, self.emp_age))
        
# object of classes being made here
employees = [emps('John', 33), emps('Marcus', 22), emps('Joe', 18)]
# object being used
for emp in employees:
    emp.info()
    
