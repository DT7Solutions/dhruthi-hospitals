from django.shortcuts import render
from dhruthiapp.models import Slider 
# Create your views here.
def Home(request):  
    sliding_item = Slider.objects.all()
    return render (request, 'uifiles/index.html',{'sliding_item':sliding_item})