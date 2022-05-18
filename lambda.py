def Check_Vow(ph:str):
    low_ph=ph.lower()
    v_letters="aeiou"

    if low_ph=="":
    
      return(0)

    if low_ph [0] in v_letters:
          return 1+ Check_Vow(low_ph[1:])
    return Check_Vow(low_ph[1:])
    
print(Check_Vow("ahmed"))
numbers =[40,35, 10, 15, 20]

nmumbermulti = list(map(lambda number : number*number,numbers))

print(nmumbermulti)