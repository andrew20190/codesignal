def lineEncoding(s):
    priorchar = None
    repcount = 1
    accumulator = ''
    encoded = ''
    for char in s:
        #print(f"s={s} char={char} repcount={repcount} accumulator={accumulator} encoded={encoded}")
        if priorchar is None:
            pass
        elif priorchar != char:
            if repcount == 1:
                encoded += priorchar
            else:
                encoded += f"{repcount}{priorchar}"
            repcount = 1        
        else:
            repcount += 1
            
        priorchar = char

    # add final accumulation
    if repcount == 1:
        encoded += priorchar
    else:
        encoded += f"{repcount}{priorchar}"
        
    return encoded

