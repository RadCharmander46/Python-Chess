pieces = ["♔","♕","♖","♗","♘","♙","♚","♛","♜","♝","♞","♟︎"]
previous_moves = []
previous_boards = []
board = [] #Bottom left is starting place
checkmate = False
stalemate = False
tie = False
colour = "White"
en_passant = False
for i in range(0,8): # grid set up 
    board.append([]) #x
    for i2 in range(0,8): # more griding
        board[i].append([]) #y 
        if i2 == 0 or i2 == 1: # piece variables(piece,colour,castleabillty/double moveabillty)
            board[i][i2].append("White")
        elif i2 == 6 or i2 == 7:
            board[i][i2].append("Black")
        if i2 == 1 or i2 == 6:
            board[i][i2].append("Pawn")
            board[i][i2].append(True)
        elif i2 == 0 or i2 == 7:
            if i == 0 or i == 7:
                board[i][i2].append("Rook")
                board[i][i2].append(True)
            elif i == 1 or i == 6:
                board[i][i2].append("Knight")
                board[i][i2].append(False)
            elif i == 2 or i == 5:
                board[i][i2].append("Bishop")
                board[i][i2].append(False)
            elif i == 3:
                board[i][i2].append("Queen")
                board[i][i2].append(False)
            elif i == 4:
                board[i][i2].append("King")
                board[i][i2].append(True)
            
def board_imager(board,pieces):
    empty_space = "  "
    for i in range(0,8):
        line = str(8-i)+" "
        for i2 in range(0,8):  
            if len(board[i2][7-i]) == 0:
                line+=empty_space
            elif board[i2][7-i][0] == "White":
                if board[i2][7-i][1] == "King":
                    line = line +pieces[0]+" "
                elif board[i2][7-i][1] == "Queen":
                    line = line + pieces[1]+" "
                elif board[i2][7-i][1] == "Rook":
                    line = line +  pieces[2] + " "
                elif board[i2][7-i][1] == "Bishop":
                    line = line +  pieces[3]+" "
                elif board[i2][7-i][1] == "Knight":
                    line = line +  pieces[4]+ " "
                elif board[i2][7-i][1] == "Pawn":
                    line = line +  pieces[5]+ " "
                else:
                    line+=empty_space
            elif board[i2][7-i][0] == "Black":
                if board[i2][7-i][1] == "King":
                    line = line +  pieces[6]+" "
                elif board[i2][7-i][1] == "Queen":
                    line = line +  pieces[7]+" "
                elif board[i2][7-i][1] == "Rook":
                    line = line +  pieces[8] + " "
                elif board[i2][7-i][1] == "Bishop":
                    line = line +  pieces[9]+" "
                elif board[i2][7-i][1] == "Knight":
                    line = line +  pieces[10]+ " "
                elif board[i2][7-i][1] == "Pawn":
                    line = line + pieces[11]+ " "
                else:
                    line+=empty_space
        print(line)
    print("  A B C D E F G H")

def move_setter(board,piece_information,move_information):
    new_board = []
    for i in range(0,8):
        new_board.append([])
        for i2 in range(0,8):
            new_board[i].append([])
            for i3 in range(0,len(board[i][i2])):
                new_board[i][i2].append(board[i][i2][i3])
    move_y = move_information[1]
    move_x = move_information[0]
    #en passanting
    if en_passant:
        new_board[move_x][move_y].append(piece_information[1])
        new_board[move_x][move_y].append(piece_information[0])
        new_board[move_x][move_y].append(False)
        new_board[piece_information[2]][piece_information[3]] = []
        new_board[move_x][piece_information[3]] = []
    elif len(new_board[move_x][move_y]) == 0:
        new_board[move_x][move_y].append(piece_information[1]) # move to a blank space
        new_board[move_x][move_y].append(piece_information[0])
        new_board[move_x][move_y].append(False)
        new_board[piece_information[2]][piece_information[3]] = []
    else:
        new_board[move_x][move_y][0] = piece_information[1] # capture
        new_board[move_x][move_y][1] = piece_information[0]
        new_board[move_x][move_y][2] = False
        new_board[piece_information[2]][piece_information[3]] = []
    return new_board
def board_can_move(board,colour):
    for i in range(0,8):
        for i2 in range(0,8):
            if len(board[i][i2]) == 0 or board[i][i2][0] != colour:
                continue
            else:
                piece = board[i][i2][1]
                piece_colour = board[i][i2][0]
                piece_x = i
                piece_y = i2
                piece_variable = board[i][i2][2]
                piece_information = [piece,piece_colour,piece_x,piece_y,piece_variable]
                if len(piece_possible_moves(board,colour,piece_information)) > 0:
                    return True
    return False
def checkmate_checker(board,colour):
    if check_checker(board,colour):
        if board_can_move(board,colour):
            return False
        else:
            return True
    else:
        return False
def stalemate_checker(board,colour):
    if check_checker(board,colour):
        return False
    else:
        if board_can_move(board,colour):
            return False
        else:
            return True
def tie_checker(board,colour):
    global previous_boards
    repetitions = 0
    previous_boards.append(board)
    for i in range(0,len(previous_boards)):
        is_same = True
        for i2 in range(0,8):
            for i3 in range(0,8):
                if len(board[i2][i3]) == 0:
                    if len(previous_boards[i][i2][i3]) != 0:
                        is_same = False
                    continue
                elif len(previous_boards[i][i2][i3]) == 0:
                    if len(board[i2][i3]) != 0:
                        is_same = False
                    continue
                for i4 in range(0,3):
                    if board[i2][i3][i4] != previous_boards[i][i2][i3][i4]:
                        is_same = False
        if is_same:
            repetitions += 1
    if repetitions > 2:
        return True
    else:
        return False
def check_checker(new_board,colour,mode="checking"):
    danger_board = []
    king_coordinate = []
    for i in range(0,8):
        danger_board.append([])
        for i2 in range(0,8):
            danger_board[i].append(0)
    for i in range(0,8):#x
        for i2 in range(0,8):#y
            if len(new_board[i][i2]) == 0:
                continue
            piece = new_board[i][i2][1]
            piece_colour = new_board[i][i2][0]
            piece_variable = new_board[i][i2][2]
            piece_x = i
            piece_y = i2
            if piece_colour != colour and piece != "King":
                piece_information = [piece,piece_colour,piece_x,piece_y,piece_variable]
                moves = piece_possible_moves(new_board,piece_colour,piece_information,False)
                for i3 in range(0,len(moves),+2):
                    danger_board[moves[i3]][moves[i3+1]] += 1
            elif piece == "King" and piece_colour == colour:
                king_coordinate.append(i)
                king_coordinate.append(i2)
    if mode == "checking":
        global double_check
        if danger_board[king_coordinate[0]][king_coordinate[1]] > 0:
            if danger_board[king_coordinate[0]][king_coordinate[1]] > 1:
                double_check = True
            else:
                double_check = False
            return True
        return False
    else:
        return danger_board

def piece_possible_moves(board,colour,piece_information,mode = True):

    def one_direction_diagonal(x_increment,y_increment,max):
        piece_found = False
        directional_diagonal_moves = []
        for i in range(1,max):
            if piece_found:
                break
            xi = i*x_increment
            yi = i*y_increment
            if len(board[piece_x+xi][piece_y+yi]) == 0:
                directional_diagonal_moves.append(piece_x+xi)
                directional_diagonal_moves.append(piece_y+yi)
            elif board[piece_x+xi][piece_y+yi][0] == colour:
                piece_found = True
            else:
                piece_found = True
                directional_diagonal_moves.append(piece_x+xi)
                directional_diagonal_moves.append(piece_y+yi)
        return directional_diagonal_moves
    def diagonal_movement(length=8):
        diagonal_moves = []
        #northeast movement
        directional_diagonal_moves = one_direction_diagonal(+1,+1,min(piece_x_from_edge,piece_y_from_edge,length))
        for i in range(0,len(directional_diagonal_moves)):
            diagonal_moves.append(directional_diagonal_moves[i])
        #southeast movement
        directional_diagonal_moves = one_direction_diagonal(+1,-1,min(piece_x_from_edge,piece_y+1,length))
        for i in range(0,len(directional_diagonal_moves)):
            diagonal_moves.append(directional_diagonal_moves[i])
        #northwest movement
        directional_diagonal_moves = one_direction_diagonal(-1,+1,min(piece_x+1,piece_y_from_edge,length))
        for i in range(0,len(directional_diagonal_moves)):
            diagonal_moves.append(directional_diagonal_moves[i])
        #southwest movement
        directional_diagonal_moves = one_direction_diagonal(-1,-1,min(piece_x+1,piece_y+1,length))
        for i in range(0,len(directional_diagonal_moves)):
            diagonal_moves.append(directional_diagonal_moves[i])
        return diagonal_moves
    

    def horizonatal_movement(length=8):
        horizontals =[]
        one_directionals = one_direction_diagonal(+1,0,min(piece_x_from_edge,length))
        for i in range(0,len(one_directionals)):
            horizontals.append(one_directionals[i])
        one_directionals = one_direction_diagonal(-1,0,min(piece_x+1,length))
        for i in range(0,len(one_directionals)):
            horizontals.append(one_directionals[i])
        one_directionals = one_direction_diagonal(0,+1,min(piece_y_from_edge,length))
        for i in range(0,len(one_directionals)):
            horizontals.append(one_directionals[i])
        one_directionals = one_direction_diagonal(0,-1,min(piece_y+1,length))
        for i in range(0,len(one_directionals)):
            horizontals.append(one_directionals[i])
        return horizontals
    
    def equine_movement():
        equine_moves = []
        ys = [-2,-1,+1,+2]
        xs = [-1,+1,-2,+2,-2,+2,-1,+1]
        for i in range(0,len(ys)):
            move_y = piece_y+ys[i]
            if move_y > 7 or move_y < 0:
                continue
            for i2 in range(i*2,i*2+2):
                move_x = piece_x + xs[i2]
                if move_x > 7 or move_x < 0:
                    continue
                elif len(board[move_x][move_y]) == 0 or board[move_x][move_y][0] != colour:
                    equine_moves.append(move_x)
                    equine_moves.append(move_y)
        return equine_moves

    def pawn_movement():
        pawn_moves = []
        if colour == "White":
            y_diff = +1
        else:
            y_diff = -1
        if piece_information[4] == True and (piece_y == 6 or piece_y == 1):
            length = 2
        else:
            length = 1
        for i in range(1,length+1):
            if piece_y+(i*y_diff) > 7:
                break
            if len(board[piece_x][piece_y+(i*y_diff)]) > 0 :
                break
            pawn_moves.append(piece_x)
            pawn_moves.append(piece_y+(i*y_diff))
        #captures
        if piece_y + (1*y_diff) < 8 and piece_y + (1*y_diff) >= 0:
            if piece_x+1 < 8:
                if len(board[piece_x+1][piece_y+(1*y_diff)]) != 0 and board[piece_x+1][piece_y+(1*y_diff)][0] != colour:
                    pawn_moves.append(piece_x+1)
                    pawn_moves.append(piece_y+(1*y_diff))
            if piece_x-1 >= 0:
                if len(board[piece_x-1][piece_y+(1*y_diff)]) != 0 and board[piece_x-1][piece_y+(1*y_diff)][0] != colour:
                    pawn_moves.append(piece_x-1)
                    pawn_moves.append(piece_y+(1*y_diff))
        #en passant
        global en_passant
        if (piece_y == 4 and colour == "White") or (piece_y == 3 and colour == "Black"):
            if piece_x+1 < 8:
                if len(board[piece_x+1][piece_y]) != 0 and board[piece_x+1][piece_y][0] != colour:
                    if previous_moves[-2] == piece_x+1 and previous_moves[-1] == piece_y:
                        en_passant = True
                        pawn_moves.append(piece_x+1)
                        pawn_moves.append(piece_y+(1*y_diff))
            if piece_x-1 >= 0:
                if len(board[piece_x-1][piece_y]) != 0 and board[piece_x-1][piece_y][0] != colour:
                    if previous_moves[-2] == piece_x-1 and previous_moves[-1] == piece_y:
                        en_passant = True
                        pawn_moves.append(piece_x-1)
                        pawn_moves.append(piece_y+(1*y_diff))

        return pawn_moves
    

    piece = piece_information[0]
    piece_x = piece_information[2]
    piece_y = piece_information[3]
    piece_x_from_edge = 8-piece_x
    piece_y_from_edge = 8-piece_y
    moves = []
    if piece == "Bishop" or piece == "Queen" or piece == "Qnight":
        diagonals = diagonal_movement()
        for i in range(0,len(diagonals)):
            moves.append(diagonals[i])
    if piece == "Rook" or piece == "Queen" or piece == "Qnight":
        horizontals = horizonatal_movement()
        for i in range(0,len(horizontals)):
            moves.append(horizontals[i])
    if piece == "Pawn":
        pawns = pawn_movement()
        for i in range(0,len(pawns),+2):
            moves.append(pawns[i])
            moves.append(pawns[i+1])
    if piece == "King":
        diagonals = diagonal_movement(2)
        for i in range(0,len(diagonals)):
            moves.append(diagonals[i])
        horizontals = horizonatal_movement(2)
        for i in range(0,len(horizontals)):
            moves.append(horizontals[i])
        #castling
        if not check_checker(board,colour):
            if board[piece_information[2]][piece_information[3]][2]: #if king hasn't moved

                if len(board[0][piece_information[3]]) > 0: #if a rook is there /note I don't think there's any need to check if it's a rook
                    if board[0][piece_information[3]][2]: # if left rook hasn't moved
                        castle = True
                        for i in range(1,4):
                            if len(board[i][piece_information[3]]) != 0: #checks space between king and rook is empty
                                castle = False
                        if castle: #checks if king is moving through check
                            board_backup = board 
                            move = [piece_information[2]-1,piece_information[3]]
                            new_board = move_setter(board_backup,piece_information,move)
                            if not check_checker(new_board,colour):
                                moves.append(piece_information[2]-2)
                                moves.append(piece_information[3])
                if len(board[7][piece_information[3]]) > 0:
                    if board[7][piece_information[3]][2]: # if right rook hasn't moved
                        castle = True
                        for i in range(5,7):
                            if len(board[i][piece_information[3]]) != 0: #checks space between king and rook is empty
                                castle = False
                        if castle: #checks if king is moving through check
                            board_backup = board 
                            move = [piece_information[2]+1,piece_information[3]]
                            new_board = move_setter(board_backup,piece_information,move)
                            if not check_checker(new_board,colour):
                                moves.append(piece_information[2]+2)
                                moves.append(piece_information[3])
                
    if piece == "Knight" or piece == "Qnight":
        horses = equine_movement()
        for i in range(0,len(horses)):
            moves.append(horses[i])

    if mode:
        checked_moves = []
        board_backup = board
        for i in range(0,len(moves),+2):
            move_cooridinate = [moves[i],moves[i+1]]
            new_board = move_setter(board_backup,piece_information,move_cooridinate)
            if not check_checker(new_board,colour):
                checked_moves.append(moves[i])
                checked_moves.append(moves[i+1])
        return checked_moves
    else:
        return moves

def player_input(mode):
    checking = True
    while checking:
        checking = False
        if mode == "piece":
            coordinate = input("Enter the coordinate of the piece you wish to move. Letter first. ")
        elif mode == "move":
            coordinate = input("Enter the coordinate of where you want to move. Letter first. ")
        if len(coordinate) > 2:
            checking = True
            print("Coordinate is too long")
        else:
            try:
                number_coordinate = int(coordinate[1])
                if number_coordinate < 1 or number_coordinate > 8:
                    checking = True
                    print("Coordinate out of range")
                else:
                    try:
                        letter_coordinate = str(coordinate[0]).upper()
                        if letter_coordinate < "A" or letter_coordinate > "H":
                            checking = True
                            print("Coordinate out of range")
                    except:
                        checking = True
                        print("Incorrect format")
            except:
                checking = True
                print("Incorrect format")
    return ord(letter_coordinate)-65,number_coordinate-1

def player_piece_input(board,colour):
    piece_coordinate = player_input("piece")
    piece_x = piece_coordinate[0]
    piece_y = piece_coordinate[1]
    if len(board[piece_x][piece_y]) == 0:
        print("Piece cannot be found ")
        return player_piece_input(board,colour)
    else:
        piece = board[piece_x][piece_y][1]
        piece_colour = board[piece_x][piece_y][0]
        piece_variable = board[piece_x][piece_y][2]
        piece_information = [piece,piece_colour,piece_x,piece_y,piece_variable]
        if piece_colour != colour:
            print("Piece is not your colour")
            print("Piece:"+piece_colour)
            print("You:"+colour)
            return player_piece_input(board,colour)
        elif len(piece_possible_moves(board,colour,piece_information)) == 0:
            print("Piece has no moves")
            return player_piece_input(board,colour)
        else:
            return piece_information
        
def player_move_input(board,colour,piece_information):
    move_coordinate = player_input("move")
    move_x = move_coordinate[0]
    move_y = move_coordinate[1]
    moves = piece_possible_moves(board,colour,piece_information)
    if len(board[move_x][move_y]) != 0:
        if board[move_x][move_y][0] == colour:
            print("You cannot to take your own piece")
            return player_move_input(board,colour,piece_information)
    valid_move = False
    for i in range(0,len(moves),+2):
        if move_x == moves[i]:
            if move_y == moves[i+1]:
                valid_move = True

    if valid_move == False:
        print("Invalid move ")
        return player_move_input(board,colour,piece_information)
    return move_coordinate

def player_turn(board,colour):
    board_imager(board,pieces)
    piece_information = player_piece_input(board,colour)
    move_information = player_move_input(board,colour,piece_information)
    #board manipulation here
    board = move_setter(board,piece_information,move_information)
    previous_moves.append(move_information[0])
    previous_moves.append(move_information[1])
    #pawn promotion
    if piece_information[0] == "Pawn" and ((move_information[1] == 7 and colour == "White") or (move_information[1] == 0 and colour == "Black")):
        checking = True
        promotions = ["Knight","Bishop","Rook","Queen"]
        promotion = input("What do you want to promote your pawn to? ")
        if promotion in promotions:
            board[move_information[0]][move_information[1]][1] = promotion
    #castling
    if piece_information[0] == "King" and max(move_information[0],piece_information[2]) > min(move_information[0],piece_information[2])+1: 
        piece_y = piece_information[3]
        if move_information[0] > piece_information[2]: #moved to the right
            board[5][piece_y].append(board[7][piece_y][0])
            board[5][piece_y].append(board[7][piece_y][1])
            board[5][piece_y].append(False)
            board[7][piece_y] = []
        else: # moved to the left
            board[3][piece_y].append(board[0][piece_y][0])
            board[3][piece_y].append(board[0][piece_y][1])
            board[3][piece_y].append(False)
            board[0][piece_y] = []
    return board
while checkmate == False and stalemate == False and tie == False:
    en_passant = False
    board = player_turn(board,colour)
    if colour == "White":
        colour = "Black"
    elif colour == "Black":
        colour = "White"
    checkmate = checkmate_checker(board,colour)
    stalemate = stalemate_checker(board,colour)
    tie = tie_checker(board,colour)
if checkmate_checker(board,colour):
    if colour == "Black":
        print("Black has been checkmated \nWhite wins")
    else:
        print("White has been checkmated \nBlack wins")
elif stalemate_checker(board,colour):
    print(colour,"has no moves \nTie")
elif tie:
    print("Three move repetition \nTie")
