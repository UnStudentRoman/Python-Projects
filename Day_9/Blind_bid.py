logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

blind_bids = {}
still_bids = True

print(logo)

def add_new_bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? : $"))
    blind_bids[name] = bid

def bid_winner():
    print(f"The winner of the bid is {max(blind_bids, key=blind_bids.get)} with a bid of ${max(blind_bids.values())}.")

while still_bids == True:
    add_new_bid()
    if input("Are there more people to bid? Type 'yes' for the next bid or 'no' to close the bid.\n") == "no":
        still_bids = False
bid_winner()