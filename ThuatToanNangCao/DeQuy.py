def tinh_giai_thua(n):
    #Điểm dừng: 0!=1
    if n==0:
        return 1
    #Gọi đệ quy: n! = n*(n-1)!
    return n*tinh_giai_thua(n-1)