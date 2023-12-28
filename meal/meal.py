def main():
    tim=input("What time is it? ")
    time = convert(tim)
    

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")



def convert(time):
    time = time.split(":")
    return (int(time[0]) + int(time[-1])/60)


if __name__ == "__main__":
    main()
