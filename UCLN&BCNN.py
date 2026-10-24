#UCLN sử dụng thuật toán Euclid
#BCNN dựa trên công thức: BCNN(a,b) = Trị tuyệt đối của a * b / UCLN(a,b)
import math
a = 12
b = 18
ucln = math.gcd(a,b)
bcnn = (a*b)//ucln