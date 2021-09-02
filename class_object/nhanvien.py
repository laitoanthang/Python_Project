class Nguoi:
    """ class Nguoi lưu các thông tin cơ bản của 1 người"""
    def __init__(self, ten, tuoi): #hàm khởi tạo, tham số đầu vào gồm self là để chỉ chính nó, ngoài ra còn có thêm ten và tuoi
        self.ten = ten #thuộc tính tên của 1 người, gán bằng biến đầu vào ten
        self.tuoi = tuoi #thuộc tính tuổi của 1 người, gán bằng biến đầu vào tuoi

    def sinh_nhat(self): #hàm sinh nhật của 1 người, khi gọi hàm này thì sẽ chúc mừng sinh nhật và thêm tuoi lên 1
        print('Happy birthday to you')
        print('Your were ', self.tuoi)
        self.tuoi += 1 #tăng thuộc tính tuoi lên 1
        print('You are now ', self.tuoi)

class Nhan_vien (Nguoi):
    """ class Nhan_vien lưu các thông tin của 1 nhân viên. Nhân viên là 1 người, class Nhan_vien thừa kế từ class Nguoi"""
    def __init__(self, ten, tuoi, ma_so, luong): #hàm khởi tạo, tham số đầu vào ngoài self còn có tên, tuổi, mã số, lương
        super().__init__(ten, tuoi) #cu pháp super()__init__() --> cho biết class Nhan_vien thừa kế class Nguoi các thuộc tính ten,tuoi
        self.ma_so = ma_so #thuộc tính mã số của nhân viên, thuộc tính mới chỉ có Nhan_viên mới có, Nguoi chưa có
        self.luong = luong #thuộc tính lương của nhân viên
    def tang_luong(self, tang_them): #hàm tăng lương cho nhân viên, khi gọi hàm này sẽ cộng thêm thuộc tính lương
        self.luong += tang_them #tăng lương thêm 1 khoản tang_them

class NV_kinh_doanh (Nhan_vien):
    """class nv kinh doanh thừa kế từ class Nhan_vien vì nhân viên kinh doanh cũng là nhân viên, nhưng có 1 số thuộc tính khác"""
    def __init__(self, ten, tuoi, ma_so, luong, doanh_so): #khởi tạo, ngoài các tham số đầu vào self, tên, tuổi, mã số, lương thì nv kinh doanh còn thêm doanh số
        super().__init__(ten, tuoi, ma_so, luong) #khai báo thừa kế các thuộc tính tê, tuổi, mã số, lương thì class Nhan_vien
        self.doanh_so = doanh_so #thuộc tính mới của nv kinh doanh

    def ban_hang(self,don_hang): #hàm bán hàng, mỗi khi bán được đơn hàng thì doanh số tăng thêm
        self.doanh_so += don_hang #tăng doanh số thêm 1 lượng bằng don_hang


p1 = Nguoi('Kien',25) # khởi tạo p1 là 1 người, tên Kien, 25 tuổi
print(p1.ten)
print(p1.tuoi)
p1.sinh_nhat()


p2 = Nhan_vien('Thao',27,12,20000000) # khởi tạo p2 là 1 nhân viên, tên Thao, 27 tuổi, mã số 12, lương 20tr
print(p2.ten)
print(p2.tuoi)
print(p2.ma_so)
print(p2.luong) # in lương, là 20tr
p2.tang_luong(5000000) #tăng lương 5tr cho nhân viên này
print(p2.luong) # in lại lương, là 25tr vì trước đó đã tăng lương 5tr


p3 = NV_kinh_doanh('Long',30,15,25000000,0) #khởi tạo p3 là 1 nv kinh doanh, tên Long, 30 tuổi, mã số 15, lương 25tr, doanh số hiện = 0
print(p3.doanh_so) #in doanh số, ra 0
p3.ban_hang(10000000) # bán được đơn hàng 10tr
print(p3.doanh_so) # in doanh số, ra 10tr vì mới bán được đơn hàng 10tr