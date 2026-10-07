def add(P,Q):

    return P + Q
def subtact(P,Q):

    return P - Q
def multiply(P,Q):

    return P * Q
def divide(P,Q):

    return P / Q

print ("Please select the operation. ")
print ("Please select the operation. ")
print ("a, Add")
print ("b, subtract")
print ("c, divide")
print ("d, multiply")

choice = input("please enter choice (a/b/c/d): ")
A = int (input("Pleae enter the first number: "))
B = int (input("Pleae enter the second number: "))

if choice == 'a':
    print (A, "+", B, "=", add(A, B))

elif choice == 'b':
    print (A, "-", B, "=", subtract(A, B))

elif choice == 'c':
    print (A, "/", B, "=", divide(A, B))

elif choice == 'd':
    print (A, "*", B, "=", multiply(A, B))

else:
    print ("This is an invalid input")

