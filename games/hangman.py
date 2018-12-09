import random
life = 10

print ("Hello! Lets play hangman!")
name = input("Please write down your name : ")
print("Hello, "+name)
answer_list = ["apple","banana","cup","station","car","movie","coffee","telephone"]
current_answer = answer_list[random.randint(0,len(answer_list))-1]
print("current answer is "+str(current_answer))
underbar = "_"
start = underbar*len(current_answer)
print("You have " +str(life)+ " chances")
print("Here goes with the first question! Please answer the quiz below")
print(start)
x = input("please input your alphabet or answer : ")
x == current_answer
if len(x) == 1: #alphabet
    print("x")
else: #word
    if x == current_answer:
        print("correct!!!")
    else:
        print("wrong!!!")
        life -= 1
        print("You have " +str(life)+ " chances. Cheer up!")