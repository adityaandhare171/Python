name="harry"

print(len(name))
print(name.endswith("rry"))
print(name.startswith("Har")) # it is case sensitive
print(name.capitalize())

text = "  Hello, World!  "

# 1. strip() → Removes leading & trailing spaces
print(text.strip())  # "Hello, World!"

# 2. lower() → Converts to lowercase
print(text.lower())  # "  hello, world!  "

# 3. upper() → Converts to uppercase
print(text.upper())  # "  HELLO, WORLD!  "

# 4. replace() → Replaces part of a string
print(text.replace("World", "Python"))  # "  Hello, Python!  "

# 5. split() → Splits string into list
print(text.strip().split(","))  # ['Hello', ' World!']

