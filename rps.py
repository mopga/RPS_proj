def rps(zagad_u, zagad_c):
    win = f'Your choice - {zagad_u} Comp choice - {zagad_c} YOU WIN!'
    loose = f'Your choice - {zagad_u} Comp choice - {zagad_c}  COMP WIN!'

    if zagad_u == zagad_c:
        return "DRAW"
    elif zagad_u == 'R':
        if zagad_c == 'S':
            return ''.join(win)
        else:
            return ''.join(loose)
    elif zagad_u == 'P':
        if zagad_c == 'R':
            return ''.join(win)
        else:
            return ''.join(loose)
    elif zagad_u == 'S':
        if zagad_c == 'P':
            return ''.join(win)
        else:
            return ''.join(loose)
    elif zagad_u == '\n':
        return ''
    else:
        return "Incorrect input. Input only R / P / S"
