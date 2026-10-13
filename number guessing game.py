import random
x="yes"
score=0
while x=="yes":
    print("welcome to number guessing game!")
    print("a:easy")
    print("b:medium")
    print("c:hard")
    level=input("choose a level: ").lower()
    if level not in ["a","b","c"]:
        print("choose a vaild level you stupid doney ")
        continue
    if level =="a":
        limit=50
        chances=10
    elif level=="b":
        limit=100
        chances=7
    else:
        limit=200
        chances=5
    ans=random.randint(1,limit)
    attempts=[]
    won=False
    while len(attempts)<chances:
        try:
            a=int(input(f"enter a number in between 1 and {limit}: "))
        except ValueError:
            print("choose a vaild number you stupid doney ")
            continue
        if a not in range(1,limit+1):
            print("choose a vaild number you stupid doney ")
            continue
        attempts.append(a)
        if a==ans:
            print("correct")
            won=True
            break
        elif a>ans:
            print("too high")
        elif  a<ans:
            print("too low")
    if won==False:
        print("you lost")
        print("the answer was: ",ans)
        print("your score: ",score)
    else:
        print("your attempts",len(attempts))
        print(attempts)
        score+=110-10*len(attempts)
        print("your score: ",score)
    x=input("do you want to play again: ").lower()
    if x=="no":
        print("your final score : ",score)
