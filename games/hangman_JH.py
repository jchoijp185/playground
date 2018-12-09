import random

answer_list = [
    "apple",
    "building",
    "venus",
    "vodka",
    "giraffe",
    "mexico",
    "penguin",
    "america",
    "ant",
    "dolphin",
    "mold"
]
answer = random.choice(answer_list)
status_output = "\n[ " + "_" * len(answer) + " ] (" + str(len(answer)) + " letters)"
tries_left = 10
try_limit = 10

def process_input(input):
    if len(input) == 0:
        print("\nEnter something!")
        return

    if not input.isalpha():
        print ("\nEnter alphabet only!")
        return

    input = input.lower()
    if len(input) == 1:
        print ("Wrong! (" + str(tries_left) + " out of " + str(try_limit) + " tries left)")
    else:
        print input
        

print "\n==== hangman game begins ===="
print status_output
input = raw_input("\nEnter your guess or the answer: ")

process_input(input)

print "\n==== hangman game ended ===="


#exception
#convert capital letters to small letters
#duplicate input