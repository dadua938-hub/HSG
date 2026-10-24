#Tính luỹ thừa nhanh
#Tính (co_so^mu) chia lấy dư cho m
co_so = 2
mu = 10**18
m = 10**9+7
kq = pow(co_so,mu,m)

#Xử lý số có hàng nghìn chữ số
import sys
#Tăng giới hạn chữ số nếu có hơn 4300 chữ số
sys.set_int_max_str_digits(10000)
so_lon = int(input())
