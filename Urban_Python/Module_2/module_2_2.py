first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))

if first == second and first == third:
    print("3")
elif (first == second or first == third) or (second == third or second == first):
    print("2")
else:
    print("0")