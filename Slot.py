import random

def main():
    current_amt = 100
    while True:
        print("#######################################")
        print("Welcome to PMM's SLOT Machine!")
        print(f"Your Current Balance is Rs.{current_amt} ")
        print("#######################################")
        try:
            bet = int(input("Enter the Bet Amount: "))
        except ValueError :
            print("Try Again!") 
            break
        except  UnboundLocalError:
            print("Try Again!") 
            break
        if bet > 0:
            print(f"Current Holding >--------->>> Rs. {current_amt}")
            print("                                              Spinning!!!")
            random_slot = slot_generator(3)
            for char in random_slot:
                print(char, end=" | ")
            print("")
            if random_slot[0] == random_slot[1] == random_slot[2]:
                if random_slot[0] == '🧡':
                    payout = bet * 25
                    print(f"You won! Rs.{payout}")
                    current_amt += payout
                elif random_slot[0] == '💛':
                    payout = bet * 15
                    print(f"You won! Rs.{payout}")
                    current_amt += payout
                elif random_slot[0] == '💚':
                    payout = bet * 10
                    print(f"You won! Rs.{payout}")
                    current_amt += payout
                elif random_slot[0] == '💜':
                    payout = bet * 8
                    print(f"You won! Rs.{payout}")
                    current_amt += payout
                elif random_slot[0] == '🤍':
                    payout = bet * 5
                    print(f"You won! Rs.{payout}")
                    current_amt += payout
                print(f"Current Holding >--------->>> Rs. {current_amt}")
            else:
                print("Sorry! You lost")
                current_amt = current_amt - bet
                resp = input("To play again(P); To Quit(Q): ").upper()
                if resp == "Q":
                    break
        else:
            print("Stop kidding! I am Mature!!!")
            break
            
def slot_generator(size):
        slot_set = ['🧡','💛','💚','💜','🤍']
        random_slot = []
        for _ in range(size): random_slot.append(random.choice(slot_set)) 
        return random_slot

main()
