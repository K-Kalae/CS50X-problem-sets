import csv
import sys


def main():

    # TODO: Check for command-line usage
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".txt") or not len(sys.argv)==3:
        sys.exit("Invalid arguments!")

    # TODO: Read database file into a variable
    dna_database = []
    with open(sys.argv[1]) as db:
        reader = csv.DictReader(db)
        for row in reader:
            dna_database.append(row)
    # print(dna_database)
            #  for names in name:
            #      print(names)


    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as textfile:
        text_content = textfile.readline().strip()

    st = []
    # TODO: Find longest match of each STR in DNA sequence
    for r in range(len(dna_database)):
        strr = dna_database[r].keys()

    st = list(strr)[1:]
    # print(st)
    longest_matc = []

    for p in range(len(st)):
         longest_matc.append(longest_match(text_content, st[p]))
    # print(longest_matc)
    found = None
# TODO: Check database for matching profiles
    for r in range(len(dna_database)):
        match = list(dna_database[r].values())[1:]
        # print(match)
        int_match = [int(element) for element in match]

    # Check if the longest match is in the list of matches
        if longest_matc == int_match:
            found =  list(dna_database[r].values())[0]
            break
    if not found == None:
        print(found)
    else:
        print("No match")



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
