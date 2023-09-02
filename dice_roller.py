import random
def rolldice():
        num=int(input("How many dice do the user want to roll? [1-6] "))
        if(num>6):
            print("please enter between 1 to 6")
            rolldice()
        while(num<=6):
            result=[]
            print("[",end="")
            for i in range(num):
                dice=random.randint(1,6)
                print(dice,end=" ")
            print("]\n")
            num=9
        input1=input("do u want to play again then enter y else enter n to quit")
        if(input1=='n'):
            print("thank you visit again")
            exit()
        else:
            rolldice()
print("welcome to the dice roller app")
rolldice()

         
