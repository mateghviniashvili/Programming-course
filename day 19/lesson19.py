Games = [
    'Soccer',
    'Tic Tac Toe',
    'Snake',
    'Puzzle',
    'Rally',
]
choice = int(input("Enter the game number 0-4: "))

if choice in range(len(Games)):
    print(Games[choice])
else:
    False


















