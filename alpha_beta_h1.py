import time
import numpy as np
from tkinter import *
import tkinter.messagebox


class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        
        self.button = [ [ None for y in range(0, 3 ) ] for x in range(0, 3 ) ]
        self.nbNoeuds = 0

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()
        
        tk = Tk()
        tk.title("Tic Tac Toe")

        
        label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
        label.grid(row=1, column=0)
        start = time.time()
        (m, qx, qy) = self.max_alpha_beta(-2, 2,'X')
        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print('Recommended move: X = {}, Y = {}'.format(qx, qy))
        

        
        
        self.button[0][0] = Button(tk, text=" ", font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[0][0].config(command=lambda: self.btnClick(0,0,tk))
        self.button[0][0].grid(row=3, column=0)

        self.button[0][1] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[0][1].config(command=lambda: self.btnClick(0,1,tk))
        self.button[0][1].grid(row=3, column=1)

        self.button[0][2] = Button(tk, text=' ',font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[0][2].config(command=lambda: self.btnClick(0,2,tk))
        self.button[0][2].grid(row=3, column=2)

        self.button[1][0] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[1][0].config(command=lambda: self.btnClick(1,0,tk))
        self.button[1][0].grid(row=4, column=0)

        self.button[1][1] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[1][1].config(command=lambda: self.btnClick(1,1,tk))
        self.button[1][1].grid(row=4, column=1)

        self.button[1][2] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[1][2].config(command=lambda: self.btnClick(1,2,tk))
        self.button[1][2].grid(row=4, column=2)

        self.button[2][0] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[2][0].config(command=lambda: self.btnClick(2,0,tk))
        self.button[2][0].grid(row=5, column=0)

        self.button[2][1] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[2][1].config(command=lambda: self.btnClick(2,1,tk))
        self.button[2][1].grid(row=5, column=1)

        self.button[2][2] = Button(tk, text=' ', font='Times 20 bold', bg='dark green', fg='white', height=4, width=8)
        self.button[2][2].config(command=lambda: self.btnClick(2,2,tk))
        self.button[2][2].grid(row=5, column=2)
        
        tk.mainloop()

    def btnClick(self,i,j,tk):
        # If it's player's turn
        if self.button[i][j]['text'] == " " :
            self.button[i][j].config(text="X")
            self.current_state[i][j] = 'X'
            self.nbNoeuds = self.nbNoeuds +1
            self.result = self.H()
            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'X':
                    tkinter.messagebox.showinfo("Tic-Tac-Toe", "The winner is Player!")
                elif self.result == 'O':
                    tkinter.messagebox.showinfo("Tic-Tac-Toe", "The winner is CPU!")
                elif self.result == '.':
                    tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")

                
                tk.destroy()
                return print('nb noeuds ',self.nbNoeuds)
            self.play()
            self.result = self.H()
            if self.result != None:
                if self.result == 'X':
                    tkinter.messagebox.showinfo("Tic-Tac-Toe", "The winner is Player!")
                elif self.result == 'O':
                    tkinter.messagebox.showinfo("Tic-Tac-Toe", "The winner is CPU!")
                elif self.result == '.':
                    tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")

                
                tk.destroy()
                return print('nb noeuds ',self.nbNoeuds)
        

        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
        


    

    # Checks if the game has ended and returns the winner in each case
    def H(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'

    
    def max_alpha_beta(self, alpha, beta,c):
        if c == 'X':
            player1,player2='X','O'
        else : player2,player1='X','O'
        maxv = -2
        px = None
        py = None
        self.nbNoeuds = self.nbNoeuds +1
        result = self.H()

        if result == player2:
            return (-1, 0, 0)
        elif result == player1:
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = player1
                    self.nbNoeuds = self.nbNoeuds +1
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta,player2)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)


    
    def min_alpha_beta(self, alpha, beta,c):
        if c == 'X':
            player1,player2='X','O'
        else : player2,player1='X','O'
            
        minv = 2

        qx = None
        qy = None

        result = self.H()
        self.nbNoeuds = self.nbNoeuds +1
        if result == player2:
            return (-1, 0, 0)
        elif result == player1:
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = player1
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta,player2)
                    self.nbNoeuds = self.nbNoeuds +1
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)



    def play(self):
        # AI's turn
        
        (m, px, py) = self.max_alpha_beta(-2, 2,'O')
        self.current_state[px][py] = 'O'
        self.button[px][py].config(text="O")
        
        self.nbNoeuds = self.nbNoeuds +1

        # Player next move (recommended)
        start = time.time()
        (m, qx0, qy0) = self.max_alpha_beta(-2, 2,'X')
        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print('Recommended move: X = {}, Y = {}'.format(qx0, qy0))
        
        # Player next move (not recommended)
        start = time.time()
        (m, qx, qy) = self.min_alpha_beta(-2, 2,'X')
        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print('Recommended move: X = {}, Y = {}'.format(qx, qy))
        
        # Player next move (warning)
        if qx == qx0 and qy== qy0 : self.button[qx][qy].config(bg='yellow')
        else :
            self.button[qx0][qy0].config(bg='blue')
            self.button[qx][qy].config(bg='red')


                    

def main():
    g = Game()
    g.draw_board()
    

if __name__ == "__main__":
    main()
