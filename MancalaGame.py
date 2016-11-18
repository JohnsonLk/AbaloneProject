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


    def __init__(self, h=14):
        self.h = h
        self.initial = GameState(to_move='Player', board={(1): 0, (2): 3, (3): 0, (4): 0, (5): 0, (6): 0})


    def actions(self, state):
        moves = []
        player = state.to_move
        try:
            return state.moves
        except:
            pass
        "Legal moves are any square not yet taken adjacent to a valid piece as long as another piece isn't already there." \
        ""

        if player == 'Player':
            for x in range(0, int(self.h/2 - 1)):
                if state.board.get(x) != 0:
                    moves.append(x)

        if player == 'Opponent':
            for x in range(int(self.h/2), int(self.h - 1)):
                if state.board.get(x) != 0:
                    moves.append(x)


        state.moves = moves
        return moves

    # defines the order of play
    def opponent(self, player):
        if player == 'Player':
            return 'Opponent'
        if player == 'Opponent':
            return 'Player'
        return None

    def result(self, state, move):
        if move not in self.actions(state):
            return state  # Illegal move has no effect
        board = state.board.copy()
        player = state.to_move

        if player == 'Player':
            for x in range(0, int(self.h/2 - 1)):
                if (x) == move:
                    y = board.get(x)

                    #takes all pebbles out of hole and put one in each hole counterclockwise (excluding opponent's
                    #mancala).
                    board[x] = 0
                    while y != 0:
                        if (x + 1) % self.h != self.h - 1:
                            board[((x + 1) % self.h)] += 1
                            y -= 1
                        x += 1

                    #if the last pebble lands in the player's mancala, player gets another turn.
                    if x % self.h == int(self.h/2 - 1):
                        next_mover = player
                        return GameState(to_move=next_mover, board=board)

                    #if the last pebble lands in a hole with no pebble already in it,
                    #and the hole adjacent to that hole has pebbles in it,
                    #take all the pebbles.
                    if int(x % self.h) < int(self.h/2):
                        if board[((x) % self.h)] == 1:
                            a = (self.h - 2) - ((x) % self.h)
                            if board[a] != 0:
                                b = board[a]
                                board[a] = 0
                                board[int(self.h / 2 - 1)] = board[int(self.h / 2 - 1)] + b + board[((x) % self.h)]
                                board[((x) % self.h)] = 0
            next_mover = self.opponent(player)
            return GameState(to_move=next_mover, board=board)





        if player == 'Opponent':
            for x in range(0, self.h):
                if (x) == move:
                    y = board.get(x)

                    # takes all pebbles out of hole and put one in each hole counterclockwise (excluding opponent's
                    # mancala).
                    board[x] = 0
                    while y != 0:
                        if (x + 1) % self.h != int(self.h / 2 - 1):
                            board[((x + 1) % self.h)] += 1
                            y -= 1
                        x += 1

                    # if the last pebble lands in the player's mancala, player gets another turn.
                    if x % self.h == int(self.h - 1):
                        next_mover = player
                        return GameState(to_move=next_mover, board=board)

                    # if the last pebble lands in a hole with no pebble already in it,
                    # and the hole adjacent to that hole has pebbles in it,
                    # take all the pebbles.
                    if int(x % self.h) >= int(self.h / 2):
                        if board[((x) % self.h)] == 1:
                            a = (self.h - 2) - ((x) % self.h)
                            if board[a] != 0:
                                b = board[a]
                                board[a] = 0
                                board[int(self.h - 1)] = board[int(self.h - 1)] + b + board[((x) % self.h)]
                                board[((x) % self.h)] = 0
            next_mover = self.opponent(player)
            return GameState(to_move=next_mover, board=board)




    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        try:
            return state.utility if player == 'Player' else -state.utility
        except:
            pass
        board = state.board
        util = self.check_win(board, 'Player')
        if util == 0:
            util = -self.check_win(board, 'Opponent')
        state.utility = util
        return util if player == 'Player' else -util

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
        for x in range(0, self.v + 1):
            for y in range(0, self.h):
                if state.board.get((x, y)) == 'Y':
                    y += 1
        return ((b == 0) or (y == 0)) and len(self.actions(state)) == 0

    def display(self, state):
        board = state.board
        str = '  '
        spaces = ''
        for x in range(int(self.h/2 - 1), (self.h - 1)):
            str = str + board.get(x) + ' '
            spaces = ''
        print(str)
        print
        print('  ',board.get(12),' ' , board.get(11), ' ' ,  board.get(10), ' ' ,  board.get(9) , ' ' ,  board.get(8) ,
                ' ' , board.get(7))
        print(board.get(13), '                       ', board.get(6))
        print('  ' , board.get(0) , ' ' , board.get(1) , ' ' , board.get(2) , ' ' , board.get(3) ,
              ' ' , board.get(4), ' ', board.get(5))




myGame = FlagrantCopy()

won = GameState(
    to_move = 'B',
    board = {
             (2,2): 'B', (2,3): 'B'
            },

    label = 'won'
)

winin1 = GameState(
    to_move = 'Player',
    board = {(0): 0, (1): 0, (2): 0, (3): 47, (4): 0, (5):0,
             (6): 3, (7): 47, (8): 0, (9): 4, (10):0,(11):1, (12): 0, (13): 0
            },
    label = 'winin1'
)

losein1 = GameState(
    to_move = 'Y',
    board = {(1,1): 'B', (1,2): 'B',
             (2,1): 'Y', (2,2): 'Y',
             (3,1): 'B',
            },
    label = 'losein1'
)

winin3 = GameState(
    to_move = 'B',
    board = {(1,1): 'B', (1,2): 'Y',
             (2,1): 'B',
             (3,1): 'Y',
            },
    label = 'winin3'
)

losein3 = GameState(
    to_move = 'Y',
    board = {(1,1): 'B',
             (2,1): 'B',
             (3,1): 'Y', (1,2): 'B', (1,2): 'Y',
            },
    label = 'losein3'
)

winin5 = GameState(
    to_move = 'B',
    board = {(1,1): 'B', (1,2): 'Y',
             (2,1): 'B',
            },
    label = 'winin5'
)

lost = GameState(
    to_move = 'B',
    board = {(1,1): 'B', (1,2): 'B',
             (2,1): 'Y', (2,2): 'Y', (2,3): 'Y',
             (3,1): 'B'
            },
    label = 'lost'
)

myGames = {
    myGame: [
        #won,
         winin1,
        #losein1, winin3, losein3, winin5,
        # lost,
    ]
}


#
myGame.display(winin1)
# print(myGame.terminal_test(winin1))
print(myGame.actions(winin1))
# print('\n')
winin1 = myGame.result(winin1,(3))
myGame.display(winin1)
print(myGame.actions(winin1))
winin1 = myGame.result(winin1,(7))
myGame.display(winin1)
print(myGame.actions(winin1))
#winin1 = myGame.result(winin1,(4))
#myGame.display(winin1)
#print(myGame.actions(winin1))
