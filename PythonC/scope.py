balance = 3000

def buy_things(item,price):
    global balance
    print('balance inside the function',balance)
    #balance = balance - price     balance komano jacchena cuz local variable 
    

    balance=balance-price
    print('balance after paying',balance)
buy_things('sunglass',1000)
print('global balance after paying',balance)