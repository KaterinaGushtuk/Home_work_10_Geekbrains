def oper (N):
    if N[2] == '+':
        return round(float(N[0]) + float(N[1]),2)
    elif N[2] == '-':
        return round(float(N[0]) - float(N[1]),2)
    elif N[2] == '*':
        return round(float(N[0]) * float(N[1]),2)
    elif N[2] == '/':
        return round(float(N[0]) / float(N[1]),2)