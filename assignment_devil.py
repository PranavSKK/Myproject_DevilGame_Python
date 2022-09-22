start_state='''
              |t|d|
              |_|p|
            '''
losing_state='''
              |t|d|
              | | |
            '''            
mid_state='''
              |t|d|
              |p| |
            '''
win_state='''
              |p|d|
              | | |
            '''
# move=input("enter key u,l,r,d\n")
# if move=='l':
#     print(mid_state)
#     print("1st stage reached")
#     move=input("enter key u,l,r,d\n")
    
#     if move=='u':
#         print(win_state)
#         print("you have won thw game")
#     else:
#         print("invalid")
# elif move=='u':
#     print(losing_state)
#     print("you have lost the game")
# else:
#     print("invalid") 


move=input("enter key u,l,r,d\n")
while move=='d' or move=='r':
    print(start_state)
    print("invalid move")
    move=input("enter key\n")
if move=='l':
    print(mid_state)
    print("you have reached next stage")
    move=input("enter next move\n")
    while True:
        if move=='r':
            print(start_state)
            print("moved initial position")
            move=input("enter key u,l\n")
            while move=='r' or move=='d':
                print(start_state)
                print("invalid move")
                move=input("enter key\n")
            if move=='l':
                print(mid_state)
                print("Again you have reched next stage")
                move=input("enter key\n")  
            else:
                print(losing_state)
                print("Devil has eaten you and you lost")
                break  
        elif move=='d' or move=='l':
            print(mid_state)
            print("invalid move")
            move=input("enter key\n")
                    
        elif move=='u':
            print(win_state)
            print("Hurray! you won the game")
            break
else:
    print(losing_state)
    print("Devil has eaten you and you lost")