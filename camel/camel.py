camel = input("camelCase: ").strip()

snake = ""
for ch in camel:
    if ch.isupper():
        snake += "_" + ch.lower()
    else:
        snake += ch

print("snake_case:", snake)

