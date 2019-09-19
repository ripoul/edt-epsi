from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import requests
from datetime import date


def index(request):
    idUser = request.GET.get("id", "jules.lebris")
    today = date.today()

    payload = {
        "action": "posEDTBEECOME",
        "serverid": "C",
        "Tel": idUser,
        "date": today.strftime("%m/%d/%Y")
    }

    r = requests.request("GET", "https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx", params=payload)

    return redirect(r.url)