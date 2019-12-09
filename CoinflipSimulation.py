#Coin fliping simulator
import random

#make coin list
coin = ["heads","tails"]
done = False

def coin_flip(number_of_times):
    '''This fucntion flips a coin however many times a user wants
    and then it records the vaules and prints the vaules '''
    #repeat as many times as the user wants
    times = 0
    while True:
        times+=1
        if times <= number_of_times:
            #record vaule in a recoreded vaule list
            recoreded_vaules =[]
        
            #choose a random vaule from coin list ethier heads or tails
            recoreded_vaules.append(random.choice(coin))
        
            #print out recorderd vaules
            print(recoreded_vaules)
        else:
            break
        
#main program loop
done = False
while not done:
    try:
        coin_flip(int(input("how many times do you want to flip the coin? ")))
        done = True
    except ValueError:
        print("Error User inputed an invalid number! all numbers must be in a interger format! ex: 1,2,3 ")
    
    
    

