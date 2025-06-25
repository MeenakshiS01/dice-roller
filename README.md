# 🎲 Dice Roller Game in Python

This is a simple and beginner-friendly Python project that simulates rolling two dice using the random module. The user can press Y or y to roll the dice again, or N or n to stop. The program also handles invalid inputs with a clear message.

---

## 🧾 Python Code

```python
import random
playing = True
while playing:
    choice = input('Roll the dice? (y/n): ').lower()
    print(choice)  
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thanks for playing..')
        
    else:
        print('Invalid choice..')


## 🧠 What I Learned
- How to use Python's random module
- Writing loops to repeat actions
- Taking user input and converting it to lowercase
- Showing neat output and handling wrong inputs

## 💡 Features
- Simulates rolling two dice with random numbers
- Keeps rolling until user types N or n
- Accepts both Y/y and N/n inputs
- Shows clear messages for wrong input
