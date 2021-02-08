import random
def computer_guess(x):
    print("Hey Guess the number Computer : ")
    
    low = 1
    high = x
    inp = ''
    while (inp  != 'c') :
        rand_num = random.randint(low, high)
        
        inp = input(f'Is {rand_num} too high (H), too low (L), or correct (C)?? ').lower()
        
        if (inp == 'l') :
            rand_num = rand_num + 1
        elif (inp == 'h') :
            rand_num = rand_num - 1
            
    print("Bravo you guessed it Right !!")  
    
    
    
    
    
    
computer_guess(10)