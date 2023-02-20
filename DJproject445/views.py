import datetime

from django.shortcuts import render, redirect
#from .forms import *


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
def showMyData(request):
    return render(request,'showMyData.html')

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


def listProduct(request):
    details = "ครีม"
    name = "นางสาวจุฑารัตน์ ประจันตะเสน"
    date = datetime.datetime.now()
    return render(request,'listProduct.html',{'lstProduct':lstOurProduct,
                                              'details':details,'name':name,
                                              'date':date.strftime("%A %d-%m-%Y %H :%M")})

def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['pid']
            pname = form.cleaned_data['pname']
            color = form.cleaned_data['colors']
            size = form.cleaned_data['size']
            price = form.cleaned_data['price']
            am = form.cleaned_data['amount']
            promotion = form.cleaned_data['promotion']
            productnew = product(pid,pname,color,size,price,am,promotion)
            lstOurProduct.append(productnew)
            return redirect('listProduct')
        else:
            return redirect('pro_retrive_all')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return  render(request,'inputProduct.html',context)

