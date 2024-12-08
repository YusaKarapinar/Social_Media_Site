from django.http import HttpResponse
from django.shortcuts import render

data = { 
    "Friend1":"1 Friend",
    "Friend2":"2 Friend",
    "Friend3":"3 Friend",
}



# Create your views here.


def FindProfileByName(req,ProfileName):
    friend_html=""


    friend_list=data.keys()
    for friend in friend_list:
        friend_html+=f"<div>{friend}<div><br>"
    friend_html=f"<div>Arkadaş Listesi<div><br>{friend_html}<br>"



    


    return render(req,'ProfilePage/index.html',{
        'ProfileName':ProfileName,
    })

def DefaultProfilePage(req):
    return render(req,'ProfilePage/index.html')