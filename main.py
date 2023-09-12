num1 = 11
num2 = num1

print("before num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("\nnum2 points to:", id(num2))


num2 = 22

print("\nafter num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("\nnum2 points to:", id(num2))

        
