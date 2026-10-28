''' Cho mảng A, tính tổng các số từ A[L] đến A[R] (thực hiện Q lần vấn tin).'''
def mang_cong_don(mang_a):
    n = len(mang_a)
    tong_tien_to = [0] * (n+1)
    for i in range(n):
        tong_tien_to[i+1] = tong_tien_to[i] + mang_a[i]
    return tong_tien_to
# Để tính tổng từ L đến R (chỉ số từ 1): 
#Tong = tong_tien_to[R] - tong_tien_to[L-1]