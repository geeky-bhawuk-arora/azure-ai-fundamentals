# -----------------------------------------------
# Local Vs Global variables in Python Functions
# -----------------------------------------------

# Function

def myFunction():
    var1 = 10
    print("var1 inside myFunction:", var1)
    print("var2 inside myFunction:", var2)

var2 = 20

myFunction()

print("var1 outside myFunction:" var1)
print("var2 outside myFunction:", var2)
