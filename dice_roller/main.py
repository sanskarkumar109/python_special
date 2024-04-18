import random
print("dice is rolling : ")
a=random.randint(1,6)
while True:
    print(a)
    if a==6:
        print("dice is rolling again")
        a=random.randint(1,6)
        print(a)
        if a==6:
            print("dice is rolling one more time")
            a=random.randint(1,6)
            print(a)
            if a==6:
                print("ohhhh three 6's your times up !!!")
                break
            else:
                break
        else:
            break    
    else:
        break;    
