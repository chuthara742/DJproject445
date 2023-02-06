from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def info(request):
    return render(request, 'infoSTD.html')


def edu(request):
    return render(request, 'eduSTD.html')


def inter(request):
    return render(request, 'inter.html')


def myidol(request):
    return render(request, 'myidol.html')


def manu(request):
    return render(request, 'manu.html')

def header(request):
    return render(request,'header.html')

def package(request):
    return render(request,'package.html')

#def showMyData(request):
 #   name = "chutharat"
  #  surname = "chutharat"
   # gender = "Male"
    #status = "student"
  #  work = "RMUTI.Khonkean"
  #  education = ""
 #   return render(request,'showMyData.html',
  #                {'name':name,'surname':surname,'gender':gender,'status':status,'work':work,'education':education}
   #               )


def showMyData(request):
    name = "นางสาวจุฑารัตน์ ประจันตะเสน"
    stdid = "65342310044-5"
    address = "84 ม.1 อ.ชนบท จ.ขอนแก่น 40180"
    gender = "หญิง"
    weigth = "47"
    heigth = "156"
    colors = "สีชมพู"
    food = "อาหารประเภทเส้น"
    job = "นักศึกษา"
    myproduct = [["ทรีเอ็กซ์ เนเชอรัล แอนตี้-แฮร์ฟอล คอนดิชันเนอร์ 250 กรัม", "299", "images/A.jpg"],
                 ["ไฮยา ลิป บาล์ม กิ๊ฟต์เซ็ต ", "199", "images/B.jpg"],
                 ["เดย์ ทู ไนท์ อาย แอนด์ ชีค พาเลทท์", "299", "images/C.jpg"],]
    return render(request, 'showMyData.html', {'name':name, 'stdid':stdid, 'address':address, 'gender':gender,
                                          'weigth':weigth, 'heigth':heigth, 'colors':colors, 'food':food,
                                          'job':job, 'myproduct':myproduct})