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

def showMyData(request):
    name = "chutharat"
    surname = "chutharat"
    gender = "Male"
    status = "student"
    work = "RMUTI.Khonkean"
    education = ""
    return render(request,'showMyData.html',
                  {'name':name,'surname':surname,'gender':gender,'status':status,'work':work,'education':education}
                  )


