from random import randint
for play in range (5) :
  player = input('rock(r),paper(p)scissors(s)')

  print(player, 'vs', end =' ') 

  chosen = randint(1,3)
  #print(chosen)

  if chosen == 1:
    computer = 'r'

  elif chosen == 2:
    computer = 'p'
  elif chosen == 3:
    computer = 's'

  print(computer)

  if player == computer:
      print('DRAW!!!!!')

  elif player == 'r'and computer == 's':
          print ('Player wins!!!!!')

  elif computer == 'p' and player == 'r':
          print ('Computer wins!!!!')

  elif player == 'p' and computer == 'r':

  elif computer == 's'and player == 'p':
           print('Computer wins!!!!')

  elif player == 's' and computer == 'p':
           print('Player wins!!!!')

  elif computer == 's'and player == 'p':
           print('Computer wins!!!!')



 
