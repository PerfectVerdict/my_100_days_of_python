bids = {}

is_on = True
while is_on:
    print("\n" * 100)
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    more_bidders = input("Are there more bidders?: ").lower()

    bids[name] = bid
    if more_bidders == "no":
        is_on = False
        bids[name] = bid
        highest_bid = max(bids, key=bids.get)
        print(f"The winner is {highest_bid}, with a bid of {bids[highest_bid]}")
    else:
        print("\n" * 100)
        pass





