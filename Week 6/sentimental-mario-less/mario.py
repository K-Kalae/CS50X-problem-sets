while True:
        try:
            height = int(input("Height: "))

            if height > 0 and height < 9:
                break

        except ValueError as error:
            pass

for line in range(height):
        print(" " * (height - line - 1), end="")
        print("#" * (line + 1))



