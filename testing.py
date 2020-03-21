def ilanginLast_move(generated, last_move):
    if last_move == None:
        return generated
    elif last_move not in generated:
        return generated
    else:
        return generated.remove(last_move)
    
