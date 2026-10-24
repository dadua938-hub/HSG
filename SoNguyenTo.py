#Duyệt đến căn bậc hai của N
import math
def ktnt(n):
    if n<2: False
    #Duyet tu 2 den can bac hai cua n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
        return True
#Sàng Eratosthenes – Tìm mọi số nguyên tố đến 10^6 (O(N log N))
def sang_SNT(gioi_han):
    #Khởi tạo danh sách toàn bộ là True(coi là số nguyên tố)
    la_so_nguyen_to = [True] * (gioi_han+1)
    la_so_nguyen_to[0] = la_so_nguyen_to[1] = False

    for p in range(2,int(math.sqrt(gioi_han))+1):
        if la_so_nguyen_to[p]:
            # Đánh dấu các bội của p không phải là số nguyên tố 
            for i in range(p*p,gioi_han+1,p):
                la_so_nguyen_to[i] = False
    return la_so_nguyen_to

a = 56
print(ktnt(a))
print(sang_SNT(a))