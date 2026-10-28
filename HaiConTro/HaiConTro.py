'''Tìm một cặp số trong mảng đã sắp xếp có tổng bằng K.'''
def tim_cap_so(mang,k):
    trai = 0
    phai = len(mang)-1
    while trai<phai:
        tong_ht mang[trai]+mang[phai]
        if tong_ht == k:
            return mang[trai],mang[phai]
        elif tong_ht < k:
            trai += 1 #Cần tổng lớn hơn, tăng con trỏ trái
        else:
            phai -= 1 #Cần tổng nhỏ hơn, giảm con trỏ phải
    return None
