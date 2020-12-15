import numpy as np
import pandas as pd
from tkinter import *
import os

board = pd.DataFrame({'0' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'1' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'2' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'3' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'4' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'5' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'6' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'7' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'8' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'9' : np.array(['--','--','--','--','--','--','--','--','--','--'])},
						index = [0,1,2,3,4,5,6,7,8,9])

	
position = {}

position['currow'] = 0
position['curcol'] = 0

position['prevrow'] = 0
position['prevcol'] = 0

board.iloc[position['currow']][position['curcol']] = '#'

def right(position):
	if position['curcol']==9:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['curcol'] = position['curcol']+1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	os.system("cls")
	print("{}\n\nCurrent position: {},{}".format(board,position['currow'],position['curcol']))
	
def left(position):
	if position['curcol']==0:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['curcol'] = position['curcol']-1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	os.system("cls")
	print("{}\n\nCurrent position: {},{}".format(board,position['currow'],position['curcol']))
	
def up(position):
	if position['currow']==0:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['currow'] = position['currow']-1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	os.system("cls")
	print("{}\n\nCurrent position: {},{}".format(board,position['currow'],position['curcol']))
	
def down(position):
	if position['currow']==9:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['currow'] = position['currow']+1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	os.system("cls")
	print("{}\n\nCurrent position: {},{}".format(board,position['currow'],position['curcol']))

os.system("cls")
print("{}\n\nCurrent position: {},{}".format(board,position['currow'],position['curcol']))

root = Tk()
root.geometry("250x100+500+200")
root.title("Controls")

UP = Button(root,text="UP",command = lambda : up(position))
UP.grid(row=0,column=1)

DOWN = Button(root,text="DOWN",command = lambda : down(position))
DOWN.grid(row=1,column=1)

LEFT = Button(root,text="LEFT",command = lambda : left(position))
LEFT.grid(row=1,column=0)

RIGHT = Button(root,text="RIGHT",command = lambda : right(position))
RIGHT.grid(row=1,column=2)

root.mainloop()
