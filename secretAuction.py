from art import auctionLogo

print(auctionLogo)
userChoice = "yes"


def highestBid(biddingRecord):
    max_bid = 0
    winner = ""
    for bid in biddingRecord:
        new_bid = biddingRecord[bid]
        if new_bid > max_bid:
            max_bid = new_bid
            winner = bid
    print(f"The winner is {winner} with a bid of ${max_bid}")


bids = {}
while userChoice != "no":
    userName = input("What is your name? : ")
    price = int(input("What is your bid : $"))
    bids[userName] = price
    userChoice = input("Are there any other bidders? Type yes or No : ")
highestBid(bids)