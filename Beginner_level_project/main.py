import time, random
from QandA import *


def start():

    n = int(input("Enter the no. of Questions you like to answer?: "))
    all_correct = int()
    sequence = int()
    no_of_seq = int()
    half_question = int()

    if 6 < n < 16:

        count = 0
        ques = [i for i in range(n)]

        print("About to start the Game. r u ready!")

        while count < n:
            time.sleep(3)
            i = random.choice(ques)
            ques.remove(i)
            ans = input(f"{count + 1} Q:\n{questions[i]}")
            if answers[i] == ans.strip().lower():
                half_question += 1
                all_correct += 1
                sequence += 1
                if sequence == 3:
                    no_of_seq += 1
                    sequence = 0
            else:
                sequence = 0

            count += 1

        print("Submitting answers...")
        time.sleep(3)
        print("verifying...")
        time.sleep(5)
        if all_correct == n:
            print("Congrats, you won $100,00,000 cash prize!\nwould you like to contribute for game charity minimum "
                  "deposit $100,00,000. just kidding!")

        elif no_of_seq*3 >= n // 2:
            print("Congrats, you won $50,00,000 cash prize!")

        elif half_question >= n // 2:
            print("Congrats, you won $25,00,000 cash prize!")

        else:
            print("Better luck next time..")

    else:
        print("no of question not met the constraints! Try again..")


def main():
    print(">Welcome to the GAME [you would win one core] ! ")
    time.sleep(2)
    welcome = "\nyou will have to choose the number of question you" \
              "would answer it should > 6 and < 16 questions.\nIf you answer all the question correctly you win $100," \
              "00,000 cash prize\nor if you would answered 3 question sequentially and no. of. questions in " \
              "sequential attempt greater half of total questions you will get $50,00,000]\nor if the no. of. " \
              "question answered (*not in sequential) is greater half of questions you will get $ 25,00,000 or else " \
              "you will be executed.\nHappy SQUID'S "

    print(welcome)

    time.sleep(6)

    proceed = input(">you would like to CONTINUE [Yes/No]: ").strip().lower()
    time.sleep(2)

    if proceed == "yes":
        start()
    elif proceed == "no":
        print("See you next time...")
    else:
        print("Invalid response! ")


if __name__ == "__main__":
    main()