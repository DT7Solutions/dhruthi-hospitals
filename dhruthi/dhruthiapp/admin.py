from django.contrib import admin
from .models import Slider
# Register your models here.
class AdminHome(admin.ModelAdmin):
    list_display=('Id','Title','Image')

admin.site.register(Slider,AdminHome)