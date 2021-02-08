import random 

# the user gonna choose a r,p,s 
# computer gonna choose a r,p,s,
# r > s , p > r , s > p



def  play ():
    print("choose rock(r) , paper (p) or scissor (s)" )
    user = input()
    comp_choice = random.choice(['r','p','s'])
    
    if (user == comp_choice):
        print("it's a TIE !! OOPS")
    elif (user == 'r' and  comp_choice == 's') :
        print("You Won , Congratulations =)")
    elif (user == 'p' and comp_choice == 'r') :
        print("You Won wow !!")
    elif (user == 's' and comp_choice == 'p') :
        print("you are the winner")
    elif (comp_choice == 'r' and  user == 's') :
        print("You Won , Congratulations =)")
    elif (comp_choice == 'p' and user == 'r') :
        print("You Won wow !!")
    elif (comp_choice == 's' and user == 'p') :
        print("you are the winner")
    print(f"computer choice was : {comp_choice}")
    
    
play()