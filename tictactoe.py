# -*- coding: utf-8 -*-
"""TicTacToe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R05YB-MknmHN0Eqx0tFl8-CE99U-wZtw
"""

# TicTacToe Game
#This is a basic implementation of Tic Tac Toe
print("Hello, Welcome to my Tic Tac Toe Game! The game starts now!")
n=9
checker = False
gameboard = [["-","-","-"],["-","-","-"],["-","-","-"]]
print("This is the Game Board for Tic Tac Toe")
printGameBoard()
while n>0:
  user_input = input("Input(format: {x or o} pos1 pos2").split(" ")
  while (user_input[0]!="x" and user_input[0]!="o") or (int(user_input[1])>2 or int(user_input[1])<0) or (int(user_input[2])>2 or int(user_input[2])<0) or (gameboard[int(user_input[1])][int(user_input[2])]=="x") or (gameboard[int(user_input[1])][int(user_input[2])]=="o"):
    user_input = input("Please try again, some values you entered are not valid: ").split(" ")
  val = user_input[0]
  x = int(user_input[1])
  y = int(user_input[2])

  gameboard[x][y] = val
  printGameBoard()
  out = gameWinner()
  if out=="x":
    checker = True
    print("The winner is X!")
    break
  if out=="o":
    checker = True
    print("The winner is O!")
    break
  n-=1
if n==0 and checker==False:
  print("Good Game! It was a draw!")

def printGameBoard():
  for row in gameboard:
    temp = ""
    for position in row:
      temp = temp+position+" "
    print(temp)

def gameWinner():
  #------------------------------------------------------------------------#
  if gameboard[0][0]=="x" and gameboard[1][0]=="x" and gameboard[2][0]=="x":
    return "x"
  if gameboard[0][0]=="o" and gameboard[1][0]=="o" and gameboard[2][0]=="o":
    return "o"
  if gameboard[0][1]=="x" and gameboard[1][1]=="x" and gameboard[2][1]=="x":
    return "x"
  if gameboard[0][1]=="o" and gameboard[1][1]=="o" and gameboard[2][1]=="o":
    return "o"
  if gameboard[0][2]=="x" and gameboard[1][2]=="x" and gameboard[2][2]=="x":
    return "x"
  if gameboard[0][2]=="o" and gameboard[1][2]=="o" and gameboard[2][2]=="o":
    return "o"
  #-------------------------------------------------------------------------#
  if gameboard[0][0]=="x" and gameboard[0][1]=="x" and gameboard[0][2]=="x":
    return "x"
  if gameboard[0][0]=="o" and gameboard[0][1]=="o" and gameboard[0][2]=="o":
    return "o"
  if gameboard[1][0]=="x" and gameboard[1][1]=="x" and gameboard[1][2]=="x":
    return "x"
  if gameboard[1][0]=="o" and gameboard[1][1]=="o" and gameboard[1][2]=="o":
    return "o"
  if gameboard[2][0]=="x" and gameboard[2][1]=="x" and gameboard[2][2]=="x":
    return "x"
  if gameboard[2][0]=="o" and gameboard[2][1]=="o" and gameboard[2][2]=="o":
    return "o"
  #-------------------------------------------------------------------------#
  if gameboard[0][0]=="x" and gameboard[1][1]=="x" and gameboard[2][2]=="x":
    return "x"
  if gameboard[0][0]=="o" and gameboard[1][1]=="o" and gameboard[2][2]=="o":
    return "o"
  if gameboard[2][0]=="x" and gameboard[1][1]=="x" and gameboard[0][2]=="x":
    return "x"
  if gameboard[2][0]=="o" and gameboard[1][1]=="o" and gameboard[0][2]=="o":
    return "o"

  #----------ENDCASE----------#
  return "Game in Progress"