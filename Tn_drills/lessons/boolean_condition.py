if 0:
    print("Zero is truthy")
else:
    print("Zero is falsey")

print(int(True))
print(int(False))

if 10:
    print("Ten is truthy")
else:
    print("Ten is falsey")

if "":
    print("Empty string is truthy")
else:
    print("Empty string is falsey")

if "Lagos":
    print("Non-empty string is truthy")

print()
print("########################################################################")
print()

name = input("Enter your name: ")

if name:
    print("Hello,", name)
else:
    print("You did not enter a name")

print()
print("########################################################################")
print()


print(bool(0))
print(bool(0.01))
print(bool(-0.01))
print(bool(""))
print(bool(" "))
print(bool(None))
print(bool(False))
print(bool(True))
print(bool(" Lagos "))