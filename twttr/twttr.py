original = input("Input: ")
modified =""

for ch in original:
    if ch.lower() not in ['a','e','i','o','u']:
        modified+=ch

print("Output: ",modified)

