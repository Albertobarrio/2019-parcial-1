def decimal_to_hexadecimal(hexadecimal):
    abc=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    number=[]
    hexa=""
    while hexadecimal >= 16:
        number.append(hexadecimal%16)
        hexadecimal=int(hexadecimal/16)
    number.append(hexadecimal)
    for index in number[::-1]:
        hexa = hexa + abc[index]
    return hexa