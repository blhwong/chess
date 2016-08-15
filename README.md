# chess

Description: Lists out all available chess moves given state of the board,
and player's turn (black or white). There is no accommodation for king in check,
en passant, or castling at the moment.

Important tips:
                1. Do not modify the order of myChessBoard. You only have to
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

Function: listMoves(myChessBoard, color)

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
