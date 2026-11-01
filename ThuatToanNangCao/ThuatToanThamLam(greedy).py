#Bài toán đổi tiền (Tìm số tờ tiền ít nhất) 
def doi_tien(so_tien_can_doi,danh_sach_menh_gia):
    danh_sach_menh_gia.sort(reverse=True) #Sắp xếp danh sách mệnh giá giảm dần
    so_to = 0
    for menh_gia in danh_sach_menh_gia:
        so_to += so_tien_can_doi // menh_gia #Số tờ tiền của mệnh giá hiện tại
        so_tien_can_doi %= menh_gia #Cập nhật số tiền còn lại cần đổi
    return so_to