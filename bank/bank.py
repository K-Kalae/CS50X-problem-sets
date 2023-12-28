m=input("Greeting:").lower()
p=m.split()
first_word = p[0]


if first_word == "hello" or first_word == "hello,":
    print("$0")
elif first_word[:1].lower() == "h":
    print("$20")
else:
    print("$100")

