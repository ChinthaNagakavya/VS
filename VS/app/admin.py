from django.contrib import admin
from .models import Game
# Register your models here.
@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    list_display=['name','place','thing','number']
