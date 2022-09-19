OPER =['/', '*', '-', '+']

def is_numeric (str):
    try:
        float (str)
        return True
    except ValueError:
        return False
  

def chek_vyr (X):
    NUM = []
    calc_oper = 0
    for i,item in enumerate(X):
        if item in OPER:
            calc_oper = calc_oper + 1
            NUM = X.replace(' ','').replace(',','.').split(item)
            NUM.append(item)
    if calc_oper != 1:
        return False
    for k in range(len(NUM)-1):
        if is_numeric (NUM[k]) == False:
            return False
            break
    return NUM