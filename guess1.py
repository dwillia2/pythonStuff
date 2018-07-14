# This is a guess the number game.

import random

 

  guessesTaken = 0

 

  print('Hello! What is your name?')

  myName = input()

 

  number = random.randint(1, 20)

 print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')



  while guessesTaken < 6:

     print('Take a guess.') # There are four spaces in front of print.

     guess = input()

     guess = int(guess)



     guessesTaken = guessesTaken + 1



     if guess < number:

         print('Your guess is too low.') # There are eight spaces in front of print.



     if guess > number:

         print('Your guess is too high.')



     if guess == number:

         break



 if guess == number:

     guessesTaken = str(guessesTaken)

30.     print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

31.

32. if guess != number:

33.     number = str(number)

34.     print('Nope. The number I was thinking of was ' + number)