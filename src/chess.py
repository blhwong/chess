'''
Created on Aug 11, 2016
Modified on Aug 15, 2016

@author: Brandon Wong

Description: Lists out all available chess moves given state of the board,
and player's turn (black or white). There is no accommodation for king in check,
en passant, or castling at the moment. The board is already set for initial
states for all pieces.

Important tips: 1. Do not modify the order of myChessBoard. You only have to
                   modify arguments of object chessSquare to change the state of
                   the board.

                2. Moving a piece from a1 to a8 on the board is going "north",
                   and moving a piece from a1 to h1 on the board is going
                   "east". This will be helpful in understanding the output.

                3. The white chess pieces can only start at rows a1 and a2, and
                   the white pawns can only move "north". The black pieces can
                   only start at rows a8 and a7, and the black pawns can only
                   move "south".

                4. You only have to modify piece, and color parameters of
                   chessSquare. Do not modify the square parameter!
                   Piece argument is a string ('rook, 'knight', 'bishop',
                   'queen', 'king', 'pawn'), and color argument is a character
                   'w' for white or 'b' for black.

                   Example: a1 = chessSquare('queen', 'b', 'a1')

Function: listMoves(myChessBoard, color) located at the very bottom!
Input:    myChessBoard array. Each element of array comprises of object
          chessSquare as shown below.

          a1 = chessSquare('piece', 'color', 'square')
          .
          .
          .
          myChessBoard=[[a8,b8,c8,d8,e8,f8,g8,h8],
                        [a7,b7,c7,d7,e7,f7,g7,h7],
                        [a6,b6,c6,d6,e6,f6,g6,h6],
                        [a5,b5,c5,d5,e5,f5,g5,h5],
                        [a4,b4,c4,d4,e4,f4,g4,h4],
                        [a3,b3,c3,d3,e3,f3,g3,h3],
                        [a2,b2,c2,d2,e2,f2,g2,h2],
                        [a1,b1,c1,d1,e1,f1,g1,h1]]

          color is a one letter char either 'b' for black or 'w' for white.
          color is the color of player's turn.

Output:   The list of available moves for state of pieces on myChessBoard, and
          the turn given by color parameter. Output will list out chess piece's
          nth move, color of piece @ initial square, direction of movement, to
          position of its final square.

          Example:
          3: w pawn@c2 move northwest to take b pawn@b3
          1: w pawn@d2 move north to d3
'''

'''
PLEASE DO NOT MODIFY CODE BELOW
'''
class chessSquare:
    def __init__(self, piece, color, square):
        self.piece = piece
        self.color = color
        self.square = square

def listRookMoves(myChessBoard, color, i, j):
    count = 1
    for a in range(1,8):
        if (i + a) > 7 or myChessBoard[i+a][j].color == color:                                         #traversing south
            break
        if myChessBoard[i+a][j].piece != '0' and myChessBoard[i+a][j].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move south to take ' + myChessBoard[i+a][j].color + ' ' + myChessBoard[i+a][j].piece + '@' + myChessBoard[i+a][j].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move south to ' + myChessBoard[i+a][j].square
        count+=1
    for a in range(1,8):
        if (i - a) < 0 or myChessBoard[i-a][j].color == color:                                         #traversing north
            break
        if myChessBoard[i-a][j].piece != '0' and myChessBoard[i-a][j].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move north to take ' + myChessBoard[i-a][j].color + ' ' + myChessBoard[i-a][j].piece + '@' + myChessBoard[i-a][j].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move north to ' + myChessBoard[i-a][j].square
        count+=1
    for a in range(1,8):
        if (j + a) > 7 or myChessBoard[i][j+a].color == color:                                         #traversing east
            break
        if myChessBoard[i][j+a].piece != '0' and myChessBoard[i][j+a].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move east to take ' + myChessBoard[i][j+a].color + ' ' + myChessBoard[i][j+a].piece + '@' + myChessBoard[i][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move east to ' + myChessBoard[i][j+a].square
        count+=1
    for a in range (1,8):
        if (j - a) < 0 or myChessBoard[i][j-a].color == color:                                         #traversing west
            break
        if myChessBoard[i][j-a].piece != '0' and myChessBoard[i][j-a].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move west to take ' + myChessBoard[i][j-a].color + ' ' + myChessBoard[i][j-a].piece + '@' + myChessBoard[i][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move west to ' + myChessBoard[i][j-a].square
        count+=1
    return

def listKnightMoves(myChessBoard, color, i, j):
    count = 1
    if (i + 1) < 8 and (j + 2) < 8 and myChessBoard[i+1][j+2].color != color:                       #knight is in bounds and not blocked by own piece
        if myChessBoard[i+1][j+2].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i+1][j+2].color + ' ' + myChessBoard[i+1][j+2].piece + '@' + myChessBoard[i+1][j+2].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i+1][j+2].square
        count+=1
    if (i + 2) < 8 and (j + 1) < 8 and myChessBoard[i+2][j+1].color != color:                       #knight is in bounds and not blocked by own piece
        if myChessBoard[i+2][j+1].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i+2][j+1].color + ' ' + myChessBoard[i+2][j+1].piece + '@' + myChessBoard[i+2][j+1].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i+2][j+1].square
        count+=1
    if (i - 1) > -1 and (j + 2) < 8 and myChessBoard[i-1][j+2].color != color:                      #knight is in bounds and not blocked by own piece
        if myChessBoard[i-1][j+2].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i-1][j+2].color + ' ' + myChessBoard[i-1][j+2].piece + '@' + myChessBoard[i-1][j+2].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i-1][j+2].square
        count+=1
    if (i + 2) < 8 and (j - 1) > -1 and myChessBoard[i+2][j-1].color != color:                      #knight is in bounds and not blocked by own piece
        if myChessBoard[i+2][j-1].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i+2][j-1].color + ' ' + myChessBoard[i+2][j-1].piece + '@' + myChessBoard[i+2][j-1].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i+2][j-1].square
        count+=1
    if (i + 1) < 8 and (j - 2) > -1 and myChessBoard[i+1][j-2].color != color:                      #knight is in bounds and not blocked by own piece
        if myChessBoard[i+1][j-2].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i+1][j-2].color + ' ' + myChessBoard[i+1][j-2].piece + '@' + myChessBoard[i+1][j-2].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i+1][j-2].square
        count+=1
    if (i - 2) > -1 and (j + 1) < 8 and myChessBoard[i-2][j+1].color != color:                      #knight is in bounds and not blocked by own piece
        if myChessBoard[i-2][j+1].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i-2][j+1].color + ' ' + myChessBoard[i-2][j+1].piece + '@' + myChessBoard[i-2][j+1].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i-2][j+1].square
        count+=1
    if (i - 1) > -1 and (j - 2) > -1 and myChessBoard[i-1][j-2].color != color:                     #knight is in bounds and not blocked by own piece
        if myChessBoard[i-1][j-2].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i-1][j-2].color + ' ' + myChessBoard[i-1][j-2].piece + '@' + myChessBoard[i-1][j-2].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i-1][j-2].square
        count+=1
    if (i - 2) > -1 and (j - 1) > -1 and myChessBoard[i-2][j-1].color != color:                     #knight is in bounds and not blocked by own piece
        if myChessBoard[i-2][j-1].piece != '0':                                                     #knight takes opposite piece
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' takes ' + myChessBoard[i-2][j-1].color + ' ' + myChessBoard[i-2][j-1].piece + '@' + myChessBoard[i-2][j-1].square
            count+=1
        else:                                                                                       #knight moves to empty space
            print str(count) + ': ' + color + ' knight@' + myChessBoard[i][j].square + ' move to ' + myChessBoard[i-2][j-1].square
        count+=1
    return

def listBishopMoves(myChessBoard, color, i, j):
    count = 1
    for a in range(1,8):
        if (i + a) > 7 or (j + a) > 7 or myChessBoard[i+a][j+a].color == color:                                         #traversing southeast
            break
        if myChessBoard[i+a][j+a].piece != '0' and myChessBoard[i+a][j+a].color != color:
            print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move southeast to take ' + myChessBoard[i+a][j+a].color + ' ' + myChessBoard[i+a][j+a].piece + '@' + myChessBoard[i+a][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move southeast to ' + myChessBoard[i+a][j+a].square
        count+=1
    for a in range(1,8):
        if (i - a) < 0 or (j + a) > 7 or myChessBoard[i-a][j+a].color == color:                                         #traversing northeast
            break
        if myChessBoard[i-a][j+a].piece != '0' and myChessBoard[i-a][j+a].color != color:
            print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move northeast to take ' + myChessBoard[i-a][j+a].color + ' ' + myChessBoard[i-a][j+a].piece + '@' + myChessBoard[i-a][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move northeast to ' + myChessBoard[i-a][j+a].square
        count+=1
    for a in range(1,8):
        if (i + a) > 7 or (j - a) < 0 or myChessBoard[i+a][j-a].color == color:                                         #traversing southwest
            break
        if myChessBoard[i+a][j-a].piece != '0' and myChessBoard[i+a][j-a].color != color:
            print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move southwest to take ' + myChessBoard[i+a][j-a].color + ' ' + myChessBoard[i+a][j-a].piece + '@' + myChessBoard[i+a][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move southwest to ' + myChessBoard[i+a][j-a].square
        count+=1
    for a in range (1,8):
        if (i - a) < 0 or (j - a) < 0 or myChessBoard[i-a][j-a].color == color:                                         #traversing northwest
            break
        if myChessBoard[i-a][j-a].piece != '0' and myChessBoard[i-a][j-a].color != color:
            print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move northwest to take ' + myChessBoard[i-a][j-a].color + ' ' + myChessBoard[i-a][j-a].piece + '@' + myChessBoard[i-a][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' bishop@' + myChessBoard[i][j].square + ' move northwest to ' + myChessBoard[i-a][j-a].square
        count+=1
    return

def listQueenMoves(myChessBoard, color, i, j):
    count = 1
    for a in range(1,8):
        if (i + a) > 7 or myChessBoard[i+a][j].color == color:                                         #traversing south
            break
        if myChessBoard[i+a][j].piece != '0' and myChessBoard[i+a][j].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move south to take ' + myChessBoard[i+a][j].color + ' ' + myChessBoard[i+a][j].piece + '@' + myChessBoard[i+a][j].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move south to ' + myChessBoard[i+a][j].square
        count+=1
    for a in range(1,8):
        if (i - a) < 0 or myChessBoard[i-a][j].color == color:                                         #traversing north
            break
        if myChessBoard[i-a][j].piece != '0' and myChessBoard[i-a][j].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move north to take ' + myChessBoard[i-a][j].color + ' ' + myChessBoard[i-a][j].piece + '@' + myChessBoard[i-a][j].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move north to ' + myChessBoard[i-a][j].square
        count+=1
    for a in range(1,8):
        if (j + a) > 7 or myChessBoard[i][j+a].color == color:                                         #traversing east
            break
        if myChessBoard[i][j+a].piece != '0' and myChessBoard[i][j+a].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move east to take ' + myChessBoard[i][j+a].color + ' ' + myChessBoard[i][j+a].piece + '@' + myChessBoard[i][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move east to ' + myChessBoard[i][j+a].square
        count+=1
    for a in range (1,8):
        if (j - a) < 0 or myChessBoard[i][j-a].color == color:                                         #traversing west
            break
        if myChessBoard[i][j-a].piece != '0' and myChessBoard[i][j-a].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move west to take ' + myChessBoard[i][j-a].color + ' ' + myChessBoard[i][j-a].piece + '@' + myChessBoard[i][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move west to ' + myChessBoard[i][j-a].square
        count+=1
    for a in range(1,8):
        if (i + a) > 7 or (j + a) > 7 or myChessBoard[i+a][j+a].color == color:                                         #traversing southeast
            break
        if myChessBoard[i+a][j+a].piece != '0' and myChessBoard[i+a][j+a].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move southeast to take ' + myChessBoard[i+a][j+a].color + ' ' + myChessBoard[i+a][j+a].piece + '@' + myChessBoard[i+a][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move southeast to ' + myChessBoard[i+a][j+a].square
        count+=1
    for a in range(1,8):
        if (i - a) < 0 or (j + a) > 7 or myChessBoard[i-a][j+a].color == color:                                         #traversing northeast
            break
        if myChessBoard[i-a][j+a].piece != '0' and myChessBoard[i-a][j+a].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move northeast to take ' + myChessBoard[i-a][j+a].color + ' ' + myChessBoard[i-a][j+a].piece + '@' + myChessBoard[i-a][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move northeast to ' + myChessBoard[i-a][j+a].square
        count+=1
    for a in range(1,8):
        if (i + a) > 7 or (j - a) < 0 or myChessBoard[i+a][j-a].color == color:                                         #traversing southwest
            break
        if myChessBoard[i+a][j-a].piece != '0' and myChessBoard[i+a][j-a].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move southwest to take ' + myChessBoard[i+a][j-a].color + ' ' + myChessBoard[i+a][j-a].piece + '@' + myChessBoard[i+a][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move southwest to ' + myChessBoard[i+a][j-a].square
        count+=1
    for a in range(1,8):
        if (i - a) < 0 or (j - a) < 0 or myChessBoard[i-a][j-a].color == color:                                         #traversing northwest
            break
        if myChessBoard[i-a][j-a].piece != '0' and myChessBoard[i-a][j-a].color != color:
            print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move northwest to take ' + myChessBoard[i-a][j-a].color + ' ' + myChessBoard[i-a][j-a].piece + '@' + myChessBoard[i-a][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' queen@' + myChessBoard[i][j].square + ' move northwest to ' + myChessBoard[i-a][j-a].square
        count+=1
    return

def listKingMoves(myChessBoard, color, i, j):
    count = 1
    if (i - 1) > -1 and myChessBoard[i-1][j].color != color:                                        #king is in bounds and not blocked by own piece
        if myChessBoard[i-1][j].piece != '0':                                                       #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move north to take ' + myChessBoard[i-1][j].color + ' ' + myChessBoard[i-1][j].piece + '@' + myChessBoard[i-1][j].square
            count+=1
        else:                                                                                       #king moves to empty space north
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move north to ' + myChessBoard[i-1][j].square
        count+=1
    if (i - 1) > -1 and (j + 1) < 8 and myChessBoard[i-1][j+1].color != color:                       #king is in bounds and not blocked by own piece
        if myChessBoard[i-1][j+1].piece != '0':                                                     #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move northeast to take ' + myChessBoard[i-1][j+1].color + ' ' + myChessBoard[i-1][j+1].piece + '@' + myChessBoard[i-1][j+1].square
            count+=1
        else:                                                                                       #king moves to empty space northeast
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move northeast to ' + myChessBoard[i-1][j+1].square
        count+=1
    if (j + 1) < 8 and myChessBoard[i][j+1].color != color:                                         #king is in bounds and not blocked by own piece
        if myChessBoard[i][j+1].piece != '0':                                                       #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move east to take ' + myChessBoard[i][j+1].color + ' ' + myChessBoard[i][j+1].piece + '@' + myChessBoard[i][j+1].square
            count+=1
        else:                                                                                       #king moves to empty space east
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move east to ' + myChessBoard[i][j+1].square
        count+=1
    if (i + 1) < 8 and (j + 1) < 8 and myChessBoard[i+1][j+1].color != color:                       #king is in bounds and not blocked by own piece
        if myChessBoard[i+1][j+1].piece != '0':                                                     #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move southeast to take ' + myChessBoard[i+1][j+1].color + ' ' + myChessBoard[i+1][j+1].piece + '@' + myChessBoard[i+1][j+1].square
            count+=1
        else:                                                                                       #king moves to empty space southeast
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move southeast to ' + myChessBoard[i+1][j+1].square
        count+=1
    if (i + 1) < 8 and myChessBoard[i+1][j].color != color:                                         #king is in bounds and not blocked by own piece
        if myChessBoard[i+1][j].piece != '0':                                                       #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move south to take' + myChessBoard[i+1][j].color + ' ' + myChessBoard[i+1][j].piece + '@' + myChessBoard[i+1][j].square
            count+=1
        else:                                                                                       #king moves to empty space south
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move south to ' + myChessBoard[i+1][j].square
        count+=1
    if (i + 1) < 8 and (j - 1) > -1 and myChessBoard[i+1][j-1].color != color:                      #king is in bounds and not blocked by own piece
        if myChessBoard[i+1][j-1].piece != '0':                                                     #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move southwest to take ' + myChessBoard[i+1][j-1].color + ' ' + myChessBoard[i+1][j-1].piece + '@' + myChessBoard[i+1][j-1].square
            count+=1
        else:                                                                                       #king moves to empty space southwest
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move southwest to ' + myChessBoard[i+1][j-1].square
        count+=1
    if (j - 1) > -1 and myChessBoard[i][j-1].color != color:                                        #king is in bounds and not blocked by own piece
        if myChessBoard[i][j-1].piece != '0':                                                       #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move west to take ' + myChessBoard[i][j-1].color + ' ' + myChessBoard[i][j-1].piece + '@' + myChessBoard[i][j-1].square
            count+=1
        else:                                                                                       #king moves to empty space west
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move west to ' + myChessBoard[i][j-1].square
        count+=1
    if (i - 1) > -1 and (j - 1) > -1 and myChessBoard[i-1][j-1].color != color:                     #king is in bounds and not blocked by own piece
        if myChessBoard[i-1][j-1].piece != '0':                                                     #king takes opposite piece
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move northwest to take ' + myChessBoard[i-1][j-1].color + ' ' + myChessBoard[i-1][j-1].piece + '@' + myChessBoard[i-1][j-1].square
            count+=1
        else:                                                                                       #king moves to empty space northwest
            print str(count) + ': ' + color + ' king@' + myChessBoard[i][j].square + ' move northwest to ' + myChessBoard[i-1][j-1].square
        count+=1
    return

def listPawnMoves(myChessBoard, color, i, j):
    count = 1
    if myChessBoard[i][j].color == 'w':                                                                                  #pawn is white. move north.
        if (i - 1) > -1 and myChessBoard[i-1][j].piece == '0':                                      #pawn is in bounds and not blocked by own piece
            print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move north to ' + myChessBoard[i-1][j].square
            count+=1
            if i == 6:
                if myChessBoard[i-2][j].piece == '0':
                    print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move north to ' + myChessBoard[i-2][j].square
                    count+=1
        if (i - 1) > -1 and (j - 1) > -1 and myChessBoard[i-1][j-1].color != color and myChessBoard[i-1][j-1].piece != '0':                            #can take piece diagonal from pawn
            print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move northwest to take ' + myChessBoard[i-1][j-1].color + ' ' + myChessBoard[i-1][j-1].piece + '@' + myChessBoard[i-1][j-1].square
            count+=1
        if (i - 1) > -1 and (j + 1) < 8 and myChessBoard[i-1][j+1].color != color and myChessBoard[i-1][j+1].piece != '0':
            print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move northeast to take ' + myChessBoard[i-1][j+1].color + ' ' + myChessBoard[i-1][j+1].piece + '@' + myChessBoard[i-1][j+1].square
            count+=1
    else:                                                                                            #pawn is black. move south.
        if (i + 1) < 8 and myChessBoard[i+1][j].piece == '0':                                       #pawn is in bounds and not blocked by own piece
            print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move south to ' + myChessBoard[i+1][j].square
            count+=1
            if i == 1:
                if myChessBoard[i+2][j].piece == '0':
                    print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move south to ' + myChessBoard[i+2][j].square
                    count+=1
        if (i + 1) < 8 and (j - 1) > -1 and myChessBoard[i+1][j-1].color != color and myChessBoard[i+1][j-1].piece != '0':                   #can take piece diagonal from pawn
            print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move southwest to take ' + myChessBoard[i+1][j-1].color + ' ' + myChessBoard[i+1][j-1].piece + '@' + myChessBoard[i+1][j-1].square
            count+=1
        if (i + 1) < 8 and (j + 1) < 8 and myChessBoard[i+1][j+1].color != color and myChessBoard[i+1][j+1].piece != '0':
            print str(count) + ': ' + color + ' pawn@' + myChessBoard[i][j].square + ' move southeast to take ' + myChessBoard[i+1][j+1].color + ' ' + myChessBoard[i+1][j+1].piece + '@' + myChessBoard[i+1][j+1].square
            count+=1
    return

def listMoves(myChessBoard, color):
    for i in range(0,8):
        for j in range(0,8):
            if myChessBoard[i][j].color != color:
                continue
            if myChessBoard[i][j].piece == 'rook':
                listRookMoves(myChessBoard, color, i, j)
            elif myChessBoard[i][j].piece == 'knight':
                listKnightMoves(myChessBoard, color, i, j)
            elif myChessBoard[i][j].piece == 'bishop':
                listBishopMoves(myChessBoard, color, i, j)
            elif myChessBoard[i][j].piece == 'queen':
                listQueenMoves(myChessBoard, color, i, j)
            elif myChessBoard[i][j].piece == 'king':
                listKingMoves(myChessBoard, color, i, j)
            else:
                listPawnMoves(myChessBoard, color, i, j)
    return
'''
PLEASE DO NOT MODIFY CODE ABOVE
'''

'''
The board is already set for initial states for all pieces.
MODIFY STATE OF CHESSBOARD BELOW
square = chessSquare('piece', 'color', 'square')
modify by changing piece, and color parameter only. Do not change square parameter.

Here is the order of the board for your reference:
[a8,b8,c8,d8,e8,f8,g8,h8],
[a7,b7,c7,d7,e7,f7,g7,h7],
[a6,b6,c6,d6,e6,f6,g6,h6],
[a5,b5,c5,d5,e5,f5,g5,h5],
[a4,b4,c4,d4,e4,f4,g4,h4],
[a3,b3,c3,d3,e3,f3,g3,h3],
[a2,b2,c2,d2,e2,f2,g2,h2],
[a1,b1,c1,d1,e1,f1,g1,h1]
'''
a1 = chessSquare('rook','w','a1')
b1 = chessSquare('knight','w','b1')
c1 = chessSquare('bishop','w','c1')
d1 = chessSquare('king','w','d1')
e1 = chessSquare('queen','w','e1')
f1 = chessSquare('bishop','w','f1')
g1 = chessSquare('knight','w','g1')
h1 = chessSquare('rook','w','h1')

a2 = chessSquare('pawn','w','a2')
b2 = chessSquare('pawn','w','b2')
c2 = chessSquare('pawn','w','c2')
d2 = chessSquare('pawn','w','d2')
e2 = chessSquare('pawn','w','e2')
f2 = chessSquare('pawn','w','f2')
g2 = chessSquare('pawn','w','g2')
h2 = chessSquare('pawn','w','h2')

a3 = chessSquare('0','0','a3')
b3 = chessSquare('0','0','b3')
c3 = chessSquare('0','0','c3')
d3 = chessSquare('0','0','d3')
e3 = chessSquare('0','0','e3')
f3 = chessSquare('0','0','f3')
g3 = chessSquare('0','0','g3')
h3 = chessSquare('0','0','h3')

a4 = chessSquare('0','0','a4')
b4 = chessSquare('0','0','b4')
c4 = chessSquare('0','0','c4')
d4 = chessSquare('0','0','d4')
e4 = chessSquare('0','0','e4')
f4 = chessSquare('0','0','f4')
g4 = chessSquare('0','0','g4')
h4 = chessSquare('0','0','h4')

a5 = chessSquare('0','0','a5')
b5 = chessSquare('0','0','b5')
c5 = chessSquare('0','0','c5')
d5 = chessSquare('0','0','d5')
e5 = chessSquare('0','0','e5')
f5 = chessSquare('0','0','f5')
g5 = chessSquare('0','0','g5')
h5 = chessSquare('0','0','h5')

a6 = chessSquare('0','0','a6')
b6 = chessSquare('0','0','b6')
c6 = chessSquare('0','0','c6')
d6 = chessSquare('0','0','d6')
e6 = chessSquare('0','0','e6')
f6 = chessSquare('0','0','f6')
g6 = chessSquare('0','0','g6')
h6 = chessSquare('0','0','h6')

a7 = chessSquare('pawn','b','a7')
b7 = chessSquare('pawn','b','b7')
c7 = chessSquare('pawn','b','c7')
d7 = chessSquare('pawn','b','d7')
e7 = chessSquare('pawn','b','e7')
f7 = chessSquare('pawn','b','f7')
g7 = chessSquare('pawn','b','g7')
h7 = chessSquare('pawn','b','h7')

a8 = chessSquare('rook','b','a8')
b8 = chessSquare('knight','b','b8')
c8 = chessSquare('bishop','b','c8')
d8 = chessSquare('king','b','d8')
e8 = chessSquare('queen','b','e8')
f8 = chessSquare('bishop','b','f8')
g8 = chessSquare('knight','b','g8')
h8 = chessSquare('rook','b','h8')
'''
The board is already set for initial states for all pieces.
MODIFY STATE OF CHESSBOARD ABOVE
square = chessSquare('piece', 'color', 'square')
modify by changing piece, and color parameter only. Do not change square parameter.

Here is the order of the board for your reference:
[a8,b8,c8,d8,e8,f8,g8,h8],
[a7,b7,c7,d7,e7,f7,g7,h7],
[a6,b6,c6,d6,e6,f6,g6,h6],
[a5,b5,c5,d5,e5,f5,g5,h5],
[a4,b4,c4,d4,e4,f4,g4,h4],
[a3,b3,c3,d3,e3,f3,g3,h3],
[a2,b2,c2,d2,e2,f2,g2,h2],
[a1,b1,c1,d1,e1,f1,g1,h1]
'''

myChessBoard=[[a8,b8,c8,d8,e8,f8,g8,h8],            #PLEASE DO NOT MODIFY ORDER OF ELEMENTS IN myChessBoard
              [a7,b7,c7,d7,e7,f7,g7,h7],
              [a6,b6,c6,d6,e6,f6,g6,h6],
              [a5,b5,c5,d5,e5,f5,g5,h5],
              [a4,b4,c4,d4,e4,f4,g4,h4],
              [a3,b3,c3,d3,e3,f3,g3,h3],
              [a2,b2,c2,d2,e2,f2,g2,h2],
              [a1,b1,c1,d1,e1,f1,g1,h1]]

'''
Function: listMoves(myChessBoard, color)
Inputs:   myChessBoard- (do not have to change argument)
          color - player's turn ('b' for black; 'w' for white)
More details in the comments at the very beginning!
'''
listMoves(myChessBoard,'w')
