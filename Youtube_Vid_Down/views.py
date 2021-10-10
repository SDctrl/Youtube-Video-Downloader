from django.shortcuts import render
from django.http import HttpResponse
import pafy
# Create your views here.

def Downloader(request):
 if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'C:\\Users\\Shante\\Desktop\\DJProject\\Youtube_Vid_Down\\Templates\\Youtube_Vid\\home.html',context)
 return render(request, 'C:\\Users\\Shante\\Desktop\\DJProject\\Youtube_Vid_Down\\Templates\\Youtube_Vid\home.html')     
 