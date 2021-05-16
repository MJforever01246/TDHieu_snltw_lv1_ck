print ("Chào mừng bạn đến với Văn phòng phẩm Teky")
print ("Sau đây là danh mục sản phẩm của chúng tôi:")
print ("1. Bút máy: MS01 (40.000/chiếc)")
print ("2. Bút bi: MS02 (2.000/chiếc)")
print ("3. Bút chì: MS03 (2.000/chiếc)")
print ("4. Gọt bút: MS04 (5.000/cái)")
print ("5. Tẩy: MS05 (10.000/cái)")
print ("6. Mực bút máy: MS06 (50.000/hộp)")
print ("7. Giấy A4: MS07 (80.000/tập)")
print ("---------")
giohang = []
soluong = []
thanhtien = []
price = []
MS01 = "bút máy"
giaMS01 = 40000
MS02 = "bút bi"
giaMS02 = 2000
MS03 = "bút chì"
giaMS03 = 2000
MS04 = "gọt bút"
giaMS04 = 5000
MS05 = "tẩy"
giaMS05 = 10000
MS06 = "mực bút máy"
giaMS06 = 50000
MS07 = "giấy A4"
giaMS07 = 80000
tongtien = 0
name = str(input("Vui lòng nhập họ và tên quý khách: "))
address = str(input("Vui lòng nhập địa chỉ: "))
phonenumber = str(input("Vui lòng nhập số điện thoại: "))
print ("Vui lòng chọn sản phẩm cần mua")
a = True
while a:
    b = str(input("Nhập mã sản phẩm: "))
    c = int(input("Nhập số lượng: "))
    if b == "MS01" or b == "ms01" or b == "Ms01":
        print("Bạn đã cho", MS01, "vào giỏ hàng")
        gia = giaMS01*c
        e = "Bút máy: MS01 (40.000/chiếc)"
    elif b == "MS02" or b == "ms02" or b == "Ms02":
        print("Bạn đã cho", MS02, "vào giỏ hàng")
        gia = giaMS02*c
        e = "Bút bi: MS02 (2.000/chiếc)"
    elif b == "MS03" or b == "ms03" or b == "Ms03":
        print("Bạn đã cho", MS03, "vào giỏ hàng")
        gia = giaMS03*c
        e = "Bút chì: MS03 (2.000/chiếc)"
    elif b == "MS04" or b == "ms04" or b == "Ms04":
        print("Bạn đã cho", MS04, "vào giỏ hàng")
        gia = giaMS04*c
        e = "Gọt bút: MS04 (5.000/cái)"
    elif b == "MS05" or b == "ms05" or b == "Ms05":
        print("Bạn đã cho", MS05, "vào giỏ hàng")
        gia = giaMS05*c
        e = "Tẩy: MS05 (10.000/cái)"
    elif b == "MS06" or b == "ms06" or b == "Ms06":
        print("Bạn đã cho", MS06, "vào giỏ hàng")
        gia = giaMS06*c
        e = "Mực bút máy: MS06 (50.000/hộp)"
    elif b == "MS07" or b == "ms07" or b == "Ms07":
        print("Bạn đã cho", MS07, "vào giỏ hàng")
        gia = giaMS07*c
        e = "Giấy A4: MS07 (80.000/tập)"
    else:
        print("Sản phẩm bạn chọn không tồn tại")
        gia = 0
    d = str(input("Bạn có muốn mua thêm sản phẩm không? (Vui lòng nhập Y nếu có, N nếu không): "))
    tongtien = tongtien + gia
    if d == "Y" or d =="y":
        if e in giohang:
            sothutu = giohang.index(e)
            slmot = soluong[sothutu]
            sltong = c + int(slmot)
            oldprice = thanhtien[sothutu]
            newprice = int(oldprice) + gia
            thanhtien[sothutu] = str(newprice)
            soluong[sothutu]=str(sltong)
        else:
            giohang.append(e)
            soluong.append(str(c))
            thanhtien.append(str(gia))
        continue
    elif d == "N" or d == "n":
        if e in giohang:
            sothutu = giohang.index(e)
            slmot = soluong[sothutu]
            sltong = c + int(slmot)
            oldprice = thanhtien[sothutu]
            newprice = int(oldprice) + gia
            thanhtien[sothutu] = str(newprice)
            soluong[sothutu]=str(sltong)
        else:
            giohang.append(e)
            soluong.append(str(c))
            thanhtien.append(str(gia))
        a = False
    else:
        d=str(input("Cú pháp bạn nhập không chính xác. Vui lòng nhập lại: "))
        if d == "Y" or d == "y":
            if e in giohang:
                sothutu = giohang.index(e)
                slmot = soluong[sothutu]
                sltong = c + int(slmot)
                oldprice = thanhtien[sothutu]
                newprice = int(oldprice) + gia
                thanhtien[sothutu] = str(newprice)
                soluong[sothutu]=str(sltong)
            else:
                giohang.append(e)
                soluong.append(str(c))
                thanhtien.append(str(gia))
            continue
        elif d == "N" or d == "n":
            if e in giohang:
                sothutu = giohang.index(e)
                slmot = soluong[sothutu]
                sltong = c + int(slmot)
                oldprice = thanhtien[sothutu]
                newprice = int(oldprice) + gia
                thanhtien[sothutu] = str(newprice)
                soluong[sothutu]=str(sltong)
            else:
                giohang.append(e)
                soluong.append(str(c))
                thanhtien.append(str(gia))
            a = False
print ("Bạn đã hoàn tất đơn hàng. Sau đây là hóa đơn của bạn")
print ("---------")
print ("Văn phòng phẩm Teky")
print ("Họ và tên khách hàng:", name)
print ("Địa chỉ:", address)
print ("Số điện thoại:", phonenumber)
print ("---------")
k = len(giohang)
print ("Sản phẩm đã mua:")
print ("STT" + "        " + "Tên sản phẩm")
if k == 1:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
elif k == 2:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
    print("02"+"     " + giohang[1] + "(SL: " + soluong[1] + "):" + thanhtien[1])
elif k == 3:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
    print("02"+"     " + giohang[1] + "(SL: " + soluong[1] + "):" + thanhtien[1])
    print("03"+"     " + giohang[2] + "(SL: " + soluong[2] + "):" + thanhtien[2])
elif k == 4:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
    print("02"+"     " + giohang[1] + "(SL: " + soluong[1] + "):" + thanhtien[1])
    print("03"+"     " + giohang[2] + "(SL: " + soluong[2] + "):" + thanhtien[2])
    print("04"+"     " + giohang[3] + "(SL: " + soluong[3] + "):" + thanhtien[3])
elif k == 5:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
    print("02"+"     " + giohang[1] + "(SL: " + soluong[1] + "):" + thanhtien[1])
    print("03"+"     " + giohang[2] + "(SL: " + soluong[2] + "):" + thanhtien[2])
    print("04"+"     " + giohang[3] + "(SL: " + soluong[3] + "):" + thanhtien[3])
    print("05"+"     " + giohang[4] + "(SL: " + soluong[4] + "):" + thanhtien[4])
elif k == 6:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
    print("02"+"     " + giohang[1] + "(SL: " + soluong[1] + "):" + thanhtien[1])
    print("03"+"     " + giohang[2] + "(SL: " + soluong[2] + "):" + thanhtien[2])
    print("04"+"     " + giohang[3] + "(SL: " + soluong[3] + "):" + thanhtien[3])
    print("05"+"     " + giohang[4] + "(SL: " + soluong[4] + "):" + thanhtien[4])
    print("06"+"     " + giohang[5] + "(SL: " + soluong[5] + "):" + thanhtien[5])
elif k == 7:
    print("01"+"     " + giohang[0] + "(SL: " + soluong[0] + "):" + thanhtien[0])
    print("02"+"     " + giohang[1] + "(SL: " + soluong[1] + "):" + thanhtien[1])
    print("03"+"     " + giohang[2] + "(SL: " + soluong[2] + "):" + thanhtien[2])
    print("04"+"     " + giohang[3] + "(SL: " + soluong[3] + "):" + thanhtien[3])
    print("05"+"     " + giohang[4] + "(SL: " + soluong[4] + "):" + thanhtien[4])
    print("06"+"     " + giohang[5] + "(SL: " + soluong[5] + "):" + thanhtien[5])
    print("07"+"     " + giohang[6] + "(SL: " + soluong[6] + "):" + thanhtien[6])
print ("---------")
print ("Tổng tiền:", tongtien)
print ("Cảm ơn bạn đã mua hàng cùng Teky!")

