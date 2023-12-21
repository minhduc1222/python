#information passed into function are called arguments
#specified after function name, inside parentheses
def my_function(fname): # has same function as parameter, only different in function's perspective( value that is sent to the function when it is called)
    print(fname + "john")
my_function("harry")
my_function("david")
my_function("rosie")


#number of argument
#the number of argument passed into upon being called must be set relative to the number of argument set up
def my_fucntion_1(fname1, fname2):
    print(fname1 + ' ' + fname2)
    
my_fucntion_1("tacker", "stacker") # must be 2



#arbitrary argument *args
#if not sure about the number of argument ll be passed into, use "*"
def my_fucntion_2(*kid_number):
    print("youngest kid is " + kid_number[2])
    
my_fucntion_2("tacker", "stacker", "landas") # must be 2


#arbitrary keyword argument **kwargs
#if you do not know how many keyword being passed into arguments
#this way, the function receive a dictionary of arguments, and can be accessed accordingly

def my_function_3(**toy_number):
    print(f"the last toy name is " + toy_number["box_3"])
    
my_function_3(box_1 = "teddy bear", box_2 = "cars" ,box_3 = "playstation")
