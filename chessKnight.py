def chessKnight(knight_position):
    
    # make chess notation numeric
    numcol = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8
    }

    colnum = dict(zip(numcol.values(), numcol.keys()))

    xpos = numcol[knight_position[0]]
    ypos = int(knight_position[1])

    print('Knight x/y:', xpos, ypos)

    validmoves = []

    for updown in [1,2,-1,-2]:
        for leftright in [1,2,-1,-2]:
            if abs(updown) == abs(leftright):
                continue

            newx = xpos + leftright
            if newx > 8 or newx < 1:
                continue

            newy = ypos + updown
            if newy > 8 or newy < 1:
                continue
                
            validmoves.append(f"{colnum[newx]}{newy}")
            
    return len(validmoves)
