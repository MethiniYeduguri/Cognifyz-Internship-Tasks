import random

def guessing_game():
    given_num=random.randint(1,100)
    print("Number is alloted between 1 to 100")
    count=0
    while True:
        try:
            gamer_num = int(input("Your guess: "))
            count+=1
        except ValueError:
            print("Please enter a valid number!")
            continue
        if(gamer_num==given_num):
            print(f"Correct,the number is {given_num}")
            print(f"You've guessed in {count} turns")
            break
        elif(gamer_num>given_num):
            if((gamer_num-given_num)>=40):
                print("Too High")
            elif((gamer_num-given_num)>=10):
                print("High")
            else:
                print("A bit high, very close!")
        elif(gamer_num<given_num):
            if(abs(gamer_num-given_num)>=40):
                print("Too Low")
            elif(abs(gamer_num-given_num)>=10):
                print("Low")
            else:
                print("A bit low, very close!")

entry=input("Shall we start the game?(Yes/No)=")
if(entry.lower()=="yes"):
    guessing_game()
else:
    print("Bye!...We can play later.no")