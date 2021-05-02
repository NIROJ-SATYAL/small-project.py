import random
import shutil
import os
while True:
    choice=["khaja set","samosa","pakauda","aaluchop","roti tarkari","chowmin","aalu parautha","milk tea","black tea","egg chowmin","chicken chowmin","buff chowmin","veg mo:mo","buff mo:mo","nothing"]
    set=["1.khaja set=60rs per plate","2.samosa=15rs","3.pakauda=20rs","4.aaluchop=20rs","5.roti tarkari=90rs per plate","6.chowmin=80rs per plate","7.aalu parautha=25rs","8.milk tea=20 rs","9.black tea=15 rs","10.egg chowmin=100rs per plate","11.chicken chowmin=110rs per plate","12.buff chowmin=100rs per plate","13.veg mo:mo=90rs per plate","14.buff mo:mo=120rs per plate","15.nothing"]
    for i in set:
        print(i) 
    player=None
    while player not in choice:
        player=input("enter your choice:  ").lower()
    if player=="nothing".lower():
        print("!!!!!!!!!!THANK YOU FOR YOUR INFORMATION!!!!!!!!!!!1")    
    else:
        print("your choice is",player)
        print("thanks for order!!! please wait for 5 min!!!!!!")
        with open('C:\\Users\\niroj satyal\\Desktop\\python for beg\\practise.txt','a') as file:
             
            file.write(player)
        shutil.copyfile('C:\\Users\\niroj satyal\\Desktop\\python for beg\\practise.txt','C:\\Users\\niroj satyal\\Desktop\\original.txt')
    free=["milk tea","black tea","1 samosa","1 pakauda","1 aaluchop","1000  RS"]
    name=["niroj satyal","sushil gyawali","sudip katwal","prabesh katwal","nishant kumpakha","saini thapa magar","subash kc","ramesh dulal","tilak parazuli","nishnat gaire","santosh kunwar"]
    if player!="nothing":
        
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!OFFER ONLY FOR CSIT 3RD SEM SEC B STUDENT'S!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        a=random.choice(free)
        c=random.choice(name)
        print("congratulation",c, "you win the",a,"for free enjoy your day")
    c=None
    choose=["yes","no"]
    while c  not in choose:
        c=input("do you want to ordered again(yes or no):").lower()
    if c!="yes":
        os.remove('C:\\Users\\niroj satyal\\Desktop\\python for beg\\practise.txt')
        break

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! THANKS FOR VISIT OUR CANTEEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    