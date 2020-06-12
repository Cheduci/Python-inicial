# analizador de flotante
def flotante(xstr):
    try:
        float(xstr)
        return True
    except:
        return False

# analizador de primo
def primo(a):
    b = a  
    c = 0
    for n in range(b-1,1,-1):
        if b % n == 0: # condición de no primo
            c = 1
            print("{0} No es primo".format(b))
            break
    if c == 0: # condición de primo
        print("{0} Es primo".format(b))
