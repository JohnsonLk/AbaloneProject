from collections import namedtuple
from games import (Game)

class GameState:

    def __init__(self, to_move, board, label=None):
        self.to_move = to_move
        self.board = board
        self.label = label

    def __str__(self):
        if self.label == None:
            return super(GameState, self).__str__()
        return self.label

class FlagrantCopy(Game):
    """A flagrant copy of TicTacToe, from game.py
    It's simplified, so that moves and utility are calculated as needed
    Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""


    def __init__(self, h=9, v=9, k=3):
        self.h = h
        self.v = v
        self.k = k
        # self.initial = GameState(to_move='Y', board={(1,1): 'Y', (2,1): 'Y', (3,1): 'Y',
        #                                              (4,2): 'B',(4,3): 'B',(4,4): 'B'})
        self.initial = GameState(to_move='Y', board={(0,0): 'Y', (2,1): 'Y', (3,1): 'Y',
                                                     (4,2): 'B', (4,3): 'B', (4,4): 'B'})

    def isontoprow(self,x,y):
        return x <= 4 and y == 0

    def isonbottomrow(self,x,y):
        return x <= 4 and y == 8

    def isonI5toE1diagonal(self,x,y):
        return x == 0 and y <= 4

    def isonE1toA1diagonal(self,x,y):
        return x == 0 and y >= 4

    def isonI9toE9diagonal(self,x,y):
        return (x == 4 and y == 0) or (x == 5 and y == 1) or (x == 6 and y == 2) or (x == 7 and y == 3) or (x == 8 and y == 4)

    def isonE9toA5diagonal(self,x,y):
        return (x == 4 and y == 8) or (x == 5 and y == 7) or (x == 6 and y == 6) or (x == 7 and y == 5) or (x == 8 and y == 4)

    def convertx(self, x, y):
        if x >= 0:
            if (y == 0):
                return 'I'
            if (y == 1):
                return 'H'
            if (y == 2):
                return 'G'
            if (y == 3):
                return 'F'
            if (y == 4):
                return 'E'
            if (y == 5):
                return 'D'
            if (y == 6):
                return 'C'
            if (y == 7):
                return 'B'
            if (y == 8):
                return 'A'

    def converty(self, x, y):
        if (x == 0):
            if (y == 0):
                return 5
            if (y == 1):
                return 4
            if (y == 2):
                return 3
            if (y == 3):
                return 2
            if (y >= 4):
                return 1

        if (x == 1):
            if (y == 0):
                return 6
            if (y == 1):
                return 5
            if (y == 2):
                return 4
            if (y == 3):
                return 3
            if (y >= 4):
                return 2

        if (x == 2):
            if (y == 0):
                return 7
            if (y == 1):
                return 6
            if (y == 2):
                return 5
            if (y == 3):
                return 4
            if (y >= 4):
                return 3

        if (x == 3):
            if (y == 0):
                return 8
            if (y == 1):
                return 7
            if (y == 2):
                return 6
            if (y == 3):
                return 5
            if (y >= 4):
                return 4

        if (x == 4):
            if (y == 0):
                return 9
            if (y == 1):
                return 8
            if (y == 2):
                return 7
            if (y == 3):
                return 6
            if (y >= 4):
                return 5

        if (x == 5):
            if (y == 1):
                return 9
            if (y == 2):
                return 8
            if (y == 3):
                return 7
            if (y >= 4):
                return 6

        if (x == 6):
            if (y == 2):
                return 9
            if (y == 3):
                return 8
            if (y >= 4):
                return 7

        if (x == 7):
            if (y == 3):
                return 9
            if (y >= 4):
                return 8

        if (x == 8):
            if (y >= 4):
                return 9




    def revertx(self, x, y):
        if(x=='I'):
            if (y == 5):
                return 0
            if (y == 6):
                return 1
            if (y == 7):
                return 2
            if (y == 8):
                return 3
            if (y == 9):
                return 4

        if(x=='H'):
            if (y == 4):
                return 0
            if (y == 5):
                return 1
            if (y == 6):
                return 2
            if (y == 7):
                return 3
            if (y == 8):
                return 4
            if (y == 9):
                return 5

        if (x == 'G'):
            if (y == 3):
                return 0
            if (y == 4):
                return 1
            if (y == 5):
                return 2
            if (y == 6):
                return 3
            if (y == 7):
                return 4
            if (y == 8):
                return 5
            if (y == 9):
                return 6

        if (x == 'F'):
            if (y == 2):
                return 0
            if (y == 3):
                return 1
            if (y == 4):
                return 2
            if (y == 5):
                return 3
            if (y == 6):
                return 4
            if (y == 7):
                return 5
            if (y == 8):
                return 6
            if (y == 9):
                return 7

        if (x == 'E'):
            if (y == 1):
                return 0
            if (y == 2):
                return 1
            if (y == 3):
                return 2
            if (y == 4):
                return 3
            if (y == 5):
                return 4
            if (y == 6):
                return 5
            if (y == 7):
                return 6
            if (y == 8):
                return 7
            if (y == 9):
                return 8

        if (x == 'D'):
            if (y == 1):
                return 0
            if (y == 2):
                return 1
            if (y == 3):
                return 2
            if (y == 4):
                return 3
            if (y == 5):
                return 4
            if (y == 6):
                return 5
            if (y == 7):
                return 6
            if (y == 8):
                return 7

        if (x == 'C'):
            if (y == 1):
                return 0
            if (y == 2):
                return 1
            if (y == 3):
                return 2
            if (y == 4):
                return 3
            if (y == 5):
                return 4
            if (y == 6):
                return 5
            if (y == 7):
                return 6

        if (x == 'B'):
            if (y == 1):
                return 0
            if (y == 2):
                return 1
            if (y == 3):
                return 2
            if (y == 4):
                return 3
            if (y == 5):
                return 4
            if (y == 6):
                return 5

        if (x == 'A'):
            if (y == 1):
                return 0
            if (y == 2):
                return 1
            if (y == 3):
                return 2
            if (y == 4):
                return 3
            if (y == 5):
                return 4

    def reverty(self, x, y):
        if (x == 'I'):
            return 0
        if (x == 'H'):
            return 1
        if (x == 'G'):
            return 2
        if (x == 'F'):
            return 3
        if (x == 'E'):
            return 4
        if (x == 'D'):
            return 5
        if (x == 'C'):
            return 6
        if (x == 'B'):
            return 7
        if (x == 'A'):
            return 8


    def actions(self, state):
        moves = []
        player = state.to_move
        try:
            return state.moves
        except:
            pass
        "Legal moves: 1-3 adjacent (in the same direction) pieces to upper left, upper right, left, right, lower left "
        "or lower right, so long as"
        "there are either no pieces in those directions, or so long as they can 'push' opponent's pieces. (i.e."
        "3 player's pieces can move 2 opponent's pieces, 3 can move 1, or 2 can move 1. For this to happen, there"
        "must be NO player pieces behind the opponent's pieces in the direction of the push). Players can ONLY "
        "push if the direction is 'inline' with the push. "
        ""

        "Unfortunately, because Python 3 doesn't support 'tuple unpacking', the moves won't be super intuitive."
        "Moves will be displayed in these formats:"
        "Single Marble Moves (move to - x coord, move to - y coord, move from - x coord, move from - y coord)"
        "Two Marble Moves    (move to - x coord, move to - y coord, move from - x coord, move from - y coord, move from - x coord, move from - y coord)"
        "Three Marble Moves  (move to - x coord, move to - y coord, move from - x coord, move from - y coord, move from - x coord, move from - y coord)"
        "The reason three marble moves only need 2 (move from)'s is because they designate the first and the last marble" \
        "in the chain. The marble in between those marbles moves with them."
        for x in range(0, self.h):
            for y in range(0, self.v):
                if state.board.get((x,y)) == player:

                    "Single Marble, Right Move"
                    if not self.isonI9toE9diagonal(x,y):
                        if not self.isonE9toA5diagonal(x,y):
                            if (x + 1, y) not in state.board.keys() or (state.board.get((x + 1, y)) == '.'):
                                movetox = self.convertx(x+1, y)
                                movetoy = self.converty(x+1, y)
                                movefromx = self.convertx(x, y)
                                movefromy = self.converty(x, y)
                                moves.append((movetox, movetoy, movefromx, movefromy))

                    "Single Marble, Lower Right Move"
                    if not self.isonbottomrow(x,y):
                        if not self.isonE9toA5diagonal(x, y):
                            if y < 4:
                                if (x+1, y + 1) not in state.board.keys() or (state.board.get((x+1, y + 1)) == '.'):
                                    movetox = self.convertx(x+1, y+1)
                                    movetoy = self.converty(x+1, y+1)
                                    movefromx = self.convertx(x, y)
                                    movefromy = self.converty(x, y)
                                    moves.append((movetox, movetoy, movefromx, movefromy))
                            else:
                                if (x, y + 1) not in state.board.keys() or (state.board.get((x, y + 1)) == '.'):
                                    movetox = self.convertx(x, y+1)
                                    movetoy = self.converty(x, y+1)
                                    movefromx = self.convertx(x, y)
                                    movefromy = self.converty(x, y)
                                    moves.append((movetox, movetoy, movefromx, movefromy))

                    "Single Marble, Lower Left Move"
                    if not self.isonE1toA1diagonal(x, y):
                        if not self.isonbottomrow(x, y):
                            if y < 4:
                                if (x,y+1) not in state.board.keys() or (state.board.get((x,y+1)) == '.'):
                                    movetox = self.convertx(x, y + 1)
                                    movetoy = self.converty(x, y + 1)
                                    movefromx = self.convertx(x, y)
                                    movefromy = self.converty(x, y)
                                    moves.append((movetox, movetoy, movefromx, movefromy))
                            else:
                                if (x-1,y+1) not in state.board.keys() or (state.board.get((x-1,y+1)) == '.'):
                                    movetox = self.convertx(x-1, y + 1)
                                    movetoy = self.converty(x-1, y + 1)
                                    movefromx = self.convertx(x, y)
                                    movefromy = self.converty(x, y)
                                    moves.append((movetox, movetoy, movefromx, movefromy))

                    "Single Marble, Left Move"
                    if not self.isonI5toE1diagonal(x, y):
                        if not self.isonE1toA1diagonal(x,y):
                            if (x - 1, y) not in state.board.keys() or (state.board.get((x - 1, y)) == '.'):
                                movetox = self.convertx(x-1, y)
                                movetoy = self.converty(x-1, y)
                                movefromx = self.convertx(x, y)
                                movefromy = self.converty(x, y)
                                moves.append((movetox, movetoy, movefromx, movefromy))

                    "Single Marble, Upper Left Move"
                    if not self.isontoprow(x, y):
                        if not self.isonI5toE1diagonal(x,y):
                            if y < 5:
                                if (x - 1, y - 1) not in state.board.keys() or (state.board.get((x - 1, y - 1)) == '.'):
                                    if (y != 0):
                                        movetox = self.convertx(x - 1, y-1)
                                        movetoy = self.converty(x - 1, y-1)
                                        movefromx = self.convertx(x, y)
                                        movefromy = self.converty(x, y)
                                        moves.append((movetox, movetoy, movefromx, movefromy))
                            else:
                                if (x, y - 1) not in state.board.keys() or (state.board.get((x, y - 1)) == '.'):
                                    if (y != 0):
                                        movetox = self.convertx(x, y-1)
                                        movetoy = self.converty(x, y-1)
                                        movefromx = self.convertx(x, y)
                                        movefromy = self.converty(x, y)
                                        moves.append((movetox, movetoy, movefromx, movefromy))


                    "Single Marble, Upper Right Move"
                    if not self.isontoprow(x,y):
                        if not self.isonI9toE9diagonal(x,y):
                            if y < 5:
                                if (x, y - 1) not in state.board.keys() or (state.board.get((x, y - 1)) == '.'):
                                    movetox = self.convertx(x, y-1)
                                    movetoy = self.converty(x, y-1)
                                    movefromx = self.convertx(x, y)
                                    movefromy = self.converty(x, y)
                                    moves.append((movetox, movetoy, movefromx, movefromy))
                            else:
                                if (x+1, y - 1) not in state.board.keys() or (state.board.get((x+1, y - 1)) == '.'):
                                    movetox = self.convertx(x+1, y - 1)
                                    movetoy = self.converty(x+1, y - 1)
                                    movefromx = self.convertx(x, y)
                                    movefromy = self.converty(x, y)
                                    moves.append((movetox, movetoy, movefromx, movefromy))

                    #"Two Marble (the second being to the first's right), Right Move. (Since this is an \
                    #inline move, we could also push an opponent's marble if it has no marbles behind it)."
                    #if(state.board.get((x + 1, y)) == player):
                        #if((x+2, y) not in state.board.keys() or state.board.get((x + 2, y)) == '.') \
                        #or (state.board.get((x + 2, y)) == opponent(player) and (state.board.get((x + 3, y)) == '.'
                        #or (x+3, y) not in state.board.keys())):
                            #moves.append((x+2,y,x+1,y,x,y))


        "Finally, return the moves."
        state.moves = moves
        return moves

    # defines the order of play
    def opponent(self, player):
        if player == 'O':
            return 'X'
        if player == 'X':
            return 'O'
        return None

    "in result() (a,b) is the coordinates of the new move and (c, d) are the coordinates of the previous move."
    def result(self, state, a, b, c, d, e=-1, f=-1):
        if(e >= 0):
            move = (a,b,c,d,e,f)
        else:
            move = (a,b,c,d)

        if move not in self.actions(state):
            return state  # Illegal move has no effect
        board = state.board.copy()
        player = state.to_move
        if(e <= 0):
            v = self.revertx(a,b)
            w = self.reverty(a,b)
            x = self.revertx(c,d)
            y = self.reverty(c,d)
            board[(x,y)] = '.'
            board[(v,w)] = player

        next_mover = self.opponent(player)
        return GameState(to_move=next_mover, board=board)

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        try:
            return state.utility if player == 'B' else -state.utility
        except:
            pass
        board = state.board
        util = self.check_win(board, 'B')
        if util == 0:
            util = -self.check_win(board, 'Y')
        state.utility = util
        return util if player == 'B' else -util

    # Did I win?

    def check_win(self, board, player):
        n = 0
        for x in range(0, self.v + 2):
            for y in range(0, self.h + 2):
                if board.get((x,y)) == player:
                    n += 1
        return n == 0

    # does player have all their pieces off the board? Return true if more than one piece on board.
    # def board_piece_check(self, board, start, player):
    #     n=0
    #     for x in range (1, self.v + 1):
    #         for y in range (1, self.h + 1):
    #             if board == player:
    #                 n += 1
    #     return n == 0

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        b = 0
        for x in range (1, self.v + 1):
            for y in range (1, self.h + 1):
                if state.board.get((x, y)) == 'B':
                    b+=1
        y = 0
        for x in range(1, self.v + 1):
            for y in range(1, self.h + 1):
                if state.board.get((x, y)) == 'Y':
                    y += 1
        return ((b == 0) or (y == 0)) and len(self.actions(state)) == 0

    def display(self, state):
        str = '        I   '
        board = state.board
        for x in range(0, 5):
            y = 0
            str = str + '   ' + board.get((x,y), '.')
        print(str)
        str = '      H   '
        for x in range(0, 6):
            y = 1
            str = str + '   ' + board.get((x,y), '.')
        print(str)
        str = '    G   '
        for x in range(0, 7):
            y = 2
            str = str + '   ' + board.get((x,y), '.')
        print(str)
        str = '  F   '
        for x in range(0, 8):
            y = 3
            str = str + '   ' + board.get((x,y), '.')
        print(str)
        str = 'E   '
        for x in range(0, 9):
            y = 4
            str = str + '   ' + board.get((x,y), '.')
        print(str)
        str = '  D   '
        for x in range(0, 8):
            y = 5
            str = str + '   ' + board.get((x,y), '.')
        str = str + '   '
        print(str)
        str = '    C   '
        for x in range(0, 7):
            y = 6
            str = str + '   ' + board.get((x,y), '.')
        str = str + '        9'
        print(str)
        str = '      B   '
        for x in range(0, 6):
            y = 7
            str = str + '   ' + board.get((x,y), '.')
        str = str + '        8'
        print(str)
        str = '        A   '
        for x in range(0, 5):
            y = 8
            str = str + '   ' + board.get((x,y), '.')
        str = str + '        7'
        print(str)
        print('                                     6')
        print('                  1   2   3   4   5')





myGame = FlagrantCopy()

won = GameState(
    to_move = 'B',
    board = {
             (2,2): 'B', (2,3): 'B'
            },

    label = 'won'
)

winin1 = GameState(
    to_move = 'O',
    board = {#(0,0): 'O', (1,0): 'O', (2,0): 'O', (3,0): 'O', (4,0): 'O',
             #(0,1): 'O', (1,1): 'O', (2,1): 'O', (3,1): 'O', (4,1): 'O', (5,1): 'O',
             (4,4): 'O',

             #(0,4): 'X',
             #(4,2): 'O',
             #(2,6): 'X', (3,6): 'X', (4,6): 'X',
             #(0,7): 'X', (1,7): 'X', (2,7): 'X', (3,7): 'X', (4,7): 'X', (5,7): 'X',
             #(0,8): 'X', (1,8): 'X', (2,8): 'X', (3,8): 'X', (4,8): 'X',
            })

myGames = {
    myGame: [
        #won,
        winin1,
        #losein1, winin3, losein3,winin5,
        # lost,
    ]
}


#
myGame.display(winin1)
print("\n")
print(myGame.actions(winin1))
winin1 = myGame.result(winin1,'A',5,'B',5)
myGame.display(winin1)
print(myGame.actions(winin1))
