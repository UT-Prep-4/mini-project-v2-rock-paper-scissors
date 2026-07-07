#Name:
#Mini-Project - Build Your Own Game!
'''
This is YOUR game. You are the designer. There are only two requirements:

  1. Your game must use USER INPUT — typed answers, key strokes, mouse clicks, etc.
  2. Your game must keep track of and DISPLAY A SCORE.

You have everything you need from Modules 1-6: variables, input(), if/elif/else,
while loops, for loops, lists, random, and turtle graphics.

======================= NEED AN IDEA? PICK ONE OF THESE =======================

  TERMINAL GAMES (use input(), great with while loops + random):
    - Number guessing: score points for guessing in fewer tries, play 5 rounds
    - Math quiz: random questions, +1 per right answer, show the final score
    - Rock, paper, scissors: first to 3 wins, show the running score
    - Trivia: store questions and answers in lists, loop through them

  TURTLE GAMES (use the mouse or keyboard, see the reminder below):
    - Click the turtle: it jumps to a random spot every time you click it
    - Turtle race: press a key to make your turtle dash to the finish line
    - Falling catch: move a paddle with the arrow keys to catch a falling dot

  ...or invent something completely new. Weird ideas are welcome.

============================ HELPFUL SNIPPETS ================================

  Typed input:
      guess = int(input("Your guess: "))

  Turtle keyboard input:
      screen = turtle.Screen()
      screen.onkey(move_left, "Left")     # calls move_left() on the left arrow
      screen.listen()

  Turtle mouse input:
      screen.onclick(jump)                # calls jump(x, y) on every click
      my_turtle.onclick(caught)           # only when the turtle itself is clicked

  Keeping and showing a score:
      score = 0
      score = score + 1                   # when the player earns a point
      print("Score:", score)              # terminal
      pen.write("Score: " + str(score))   # turtle (use a separate pen turtle)

  REMINDER for turtle games — to see your game in Codespaces: run it, open the
  PORTS tab, click port 6080 ("Turtle Desktop"), Connect, password: vscode

========================== LEVEL-UP IDEAS (optional) ==========================

  - Add lives: the game ends after 3 misses
  - Add difficulty: harder questions or a faster game as the score goes up
  - Add a high score: remember the best score across rounds with a variable
  - Add sound-off flair: ASCII art title screens, victory messages, emoji

==============================================================================
Build your game below. Delete this line and start coding!
'''
import random
play = input("Do You Want To Play A Game? (y/n): ")
bot = ""
if play == "y":
  print("Get Best 3/5 To Win")
while play == "y":
  pscore = 0
  bscore = 0
  while bscore < 3 and pscore < 3 or pscore < 3 and bscore < 3:
    p1 = input("Rock Paper Scissors!(r,p,s): ")
    rand = random.randint(1,3)
    if rand == 1:
      bot = "r"
      print("I Chose Rock")
    elif rand == 2:
      bot = "p"
      print("I Chose Paper")
    elif rand == 3:
      bot = "s"
      print("I Chose Scissors")

    if p1 == "r":
      if bot == "r":
        print("Tie")
      elif bot == "p":
        print("You Lose")
        bscore += 1
      elif bot == "s":
        print("You Win")
        pscore += 1

    elif p1 == "p":
      if bot == "p":
        print("Tie")
      elif bot == "s":
        print("You Lose")
        bscore += 1
      elif bot == "r":
        print("You Win")
        pscore += 1

    elif p1 == "s":
      if bot == "s":
        print("Tie")
      elif bot == "r":
        print("You Lose")
        bscore += 1
      elif bot == "p":
        print("You Win")
        pscore += 1
    else:
      print("Invalid Input")
    print("Your Score:",pscore,"      My Score:",bscore)
  if bscore >= 3:
    print("You Lost The Game")
    play = input("Do You Wanna Play Again (y/n): ")
  else:
    print("You Won The Game")
    play = input("Do You Wanna Play Again (y/n): ")