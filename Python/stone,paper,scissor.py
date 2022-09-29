import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='St':
        if you=='P':
            return True 
        elif you=='Sc':
            return False
    
    elif comp=='P':
        if you=='Sc':
            return True 
        elif you=='St':
            return False

    elif comp=='Sc':
        if you=='St':
            return True 
        elif you=='P':
            return False




print("Computer  Turn : Stone (S),Paper(P),Scissor(G)")
randNo=random.randint(1,3)
if randNo==1:
    comp='St'
elif randNo==2:
    comp='P'
elif randNo==3:
    comp='Sc'
you=input("Your Turn : Stone (St),Paper(P),Scissor(Sc)??")
a=game(comp,you)
if a==None:
    print("The Game is Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

print("Computer's Choice "+comp)