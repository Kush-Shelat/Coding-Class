base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

if exponent == 0:
    print(1)
else:
    for i in range(exponent):
        result = result * base
    print(result)