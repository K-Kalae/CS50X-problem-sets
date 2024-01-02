import re

def main():
    pat_amex =re.compile(r'^3[47][0-9]{13}$')

    pat_visa = re.compile(r'^4[0-9]{15}$')

    pat_master = re.compile(r'^5[1-5][0-9]{14}$')

    card_number = input("Number: ")

    if pat_amex.match(card_number):
        print("AMEX\n")
    elif pat_visa.match(card_number):
        print("VISA\n")
    elif pat_master.match(card_number):
        print("MASTERCARD\n")
    else:
        print("INVALID\n")

if __name__ == "__main__":
    main()







