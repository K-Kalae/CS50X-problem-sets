my_list = []
while True:
    try:
        item = input().lower()

        my_list.append(item)



    except EOFError:
        print()
        item_freq = {}
        for it in my_list:
            if it in item_freq:
                item_freq[it] +=1
            else:
                item_freq[it]=1
        for item, frequency in sorted(item_freq.items()):
            print(f"{frequency} {item.upper()}")
        break


