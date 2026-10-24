def phan_tich_thua_so(n):
    uoc = 2
    dsach = []
    tam = n
    while uoc*uoc<=tam:
        while tam%uoc==0:
            dsach.append(uoc)
            tam//=uoc
        uoc+=1
    if tam>1:
        dsach.append(tam)
    return dsach

a = 125
print(phan_tich_thua_so(a))