'''
Created on Aug 11, 2016

@author: Brandon
'''
class chessSquare:
    def __init__(self, piece, color, square):
        self.piece = piece
        self.color = color
        self.square = square

def listRookMoves(myChessBoard, color, i, j):
    count = 1
    for a in range(1,8):
        if (i + a) > 7 or myChessBoard[i+a][j].color == color:                                         #traversing backwards
            break
        if myChessBoard[i+a][j].piece != '0' and myChessBoard[i+a][j].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move backwards to take ' + myChessBoard[i+a][j].color + ' ' + myChessBoard[i+a][j].piece + '@' + myChessBoard[i+a][j].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move backwards to ' + myChessBoard[i+a][j].square
        count+=1
    for a in range(1,8):
        if (i - a) < 0 or myChessBoard[i-a][j].color == color:                                         #traversing forward
            break
        if myChessBoard[i-a][j].piece != '0' and myChessBoard[i-a][j].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move forward to take ' + myChessBoard[i-a][j].color + ' ' + myChessBoard[i-a][j].piece + '@' + myChessBoard[i-a][j].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move forward to ' + myChessBoard[i-a][j].square
        count+=1
    for a in range(1,8):
        if (j + a) > 7 or myChessBoard[i][j+a].color == color:                                         #traversing right
            break
        if myChessBoard[i][j+a].piece != '0' and myChessBoard[i][j+a].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move right to take ' + myChessBoard[i][j+a].color + ' ' + myChessBoard[i][j+a].piece + '@' + myChessBoard[i][j+a].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move right to ' + myChessBoard[i][j+a].square
        count+=1
    for a in range (1,8):
        if (j - a) < 0 or myChessBoard[i][j-a].color == color:                                         #traversing left
            break
        if myChessBoard[i][j-a].piece != '0' and myChessBoard[i][j-a].color != color:
            print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move left to take ' + myChessBoard[i][j-a].color + ' ' + myChessBoard[i][j-a].piece + '@' + myChessBoard[i][j-a].square
            count+=1
            break
        print str(count) + ': ' + color + ' rook@' + myChessBoard[i][j].square + ' move left to ' + myChessBoard[i][j-a].square
        count+=1
    return

def listKnightMoves(myChessBoard, color, i, j):
    return
def listBishopMoves(myChessBoard, color, i, j):
    return
def listQueenMoves(myChessBoard, color, i, j):
    return
def listKingMoves(myChessBoard, color, i, j):
    return
def listPawnMoves(myChessBoard, color, i, j):
    return

def listMoves(myChessBoard, color):
    for i in range(0,8):
        for j in range(0,8):
            if myChessBoard[i][j].color != color:
                continue
            #print myChessBoard[i][j].piece
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

a1 = chessSquare('0','0','a1')
a2 = chessSquare('0','0','a2')
a3 = chessSquare('0','0','a3')
a4 = chessSquare('0','0','a4')
a5 = chessSquare('0','0','a5')
a6 = chessSquare('0','0','a6')
a7 = chessSquare('0','0','a7')
a8 = chessSquare('0','0','a8')
b1 = chessSquare('0','0','b1')
b2 = chessSquare('0','0','b2')
b3 = chessSquare('0','0','b3')
b4 = chessSquare('pawn','b','b4')
b5 = chessSquare('0','0','b5')
b6 = chessSquare('0','0','b6')
b7 = chessSquare('0','0','b7')
b8 = chessSquare('0','0','b8')
c1 = chessSquare('0','0','c1')
c2 = chessSquare('0','0','c2')
c3 = chessSquare('pawn','b','c3')
c4 = chessSquare('rook','w','c4')
c5 = chessSquare('pawn','b','c5')
c6 = chessSquare('0','0','c6')
c7 = chessSquare('0','0','c7')
c8 = chessSquare('0','0','c8')
d1 = chessSquare('0','0','d1')
d2 = chessSquare('0','0','d2')
d3 = chessSquare('0','0','d3')
d4 = chessSquare('pawn','b','d4')
d5 = chessSquare('0','0','d5')
d6 = chessSquare('0','0','d6')
d7 = chessSquare('0','0','d7')
d8 = chessSquare('0','0','d8')
e1 = chessSquare('0','0','e1')
e2 = chessSquare('0','0','e2')
e3 = chessSquare('0','0','e3')
e4 = chessSquare('0','0','e4')
e5 = chessSquare('0','0','e5')
e6 = chessSquare('0','0','e6')
e7 = chessSquare('0','0','e7')
e8 = chessSquare('0','0','e8')
f1 = chessSquare('0','0','f1')
f2 = chessSquare('0','0','f2')
f3 = chessSquare('0','0','f3')
f4 = chessSquare('0','0','f4')
f5 = chessSquare('0','0','f5')
f6 = chessSquare('0','0','f6')
f7 = chessSquare('0','0','f7')
f8 = chessSquare('0','0','f8')
g1 = chessSquare('0','0','g1')
g2 = chessSquare('0','0','g2')
g3 = chessSquare('0','0','g3')
g4 = chessSquare('0','0','g4')
g5 = chessSquare('0','0','g5')
g6 = chessSquare('0','0','g6')
g7 = chessSquare('0','0','g7')
g8 = chessSquare('0','0','g8')
h1 = chessSquare('0','0','h1')
h2 = chessSquare('0','0','h2')
h3 = chessSquare('0','0','h3')
h4 = chessSquare('0','0','h4')
h5 = chessSquare('0','0','h5')
h6 = chessSquare('0','0','h6')
h7 = chessSquare('0','0','h7')
h8 = chessSquare('0','0','h8')

myChessBoard=[[a8,b8,c8,d8,e8,f8,g8,h8],
              [a7,b7,c7,d7,e7,f7,g7,h7],
              [a6,b6,c6,d6,e6,f6,g6,h6],
              [a5,b5,c5,d5,e5,f5,g5,h5],
              [a4,b4,c4,d4,e4,f4,g4,h4],
              [a3,b3,c3,d3,e3,f3,g3,h3],
              [a2,b2,c2,d2,e2,f2,g2,h2],
              [a1,b1,c1,d1,e1,f1,g1,h1]]


listMoves(myChessBoard,'w')
