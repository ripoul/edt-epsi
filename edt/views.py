from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from datetime import date


def index(request):
    idUser = request.GET.get("id", "jules.lebris")
    today = date.today()

    url = "https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel={idUser}&date={date}".format(
        idUser=idUser, date=today.strftime("%m/%d/%Y")
    )

    return redirect(url)
