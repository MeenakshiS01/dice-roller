import random
playing = True
while playing:
    choice = input('Roll the dice? (y/n): ').lower()
    print(choice)  # Debug: see what input is captured
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thanks for playing..')
        
    else:
        print('Invalid choice..')


