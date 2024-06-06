name = input("Name: ")
surname1 = input("First surname: ")
surname2 = input("Second surname: ")

initials = name[0]
initials += surname1[0]
initials += surname2[0]

print("Initial name: ", initials)
print("Initial capital name: ", initials.upper())