from django.contrib import admin
from . models import post
import sys


class Origin(admin.ModelAdmin):
    list_display = ("name", "roll", "city")
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 1
    #date_hierarchy = 'added_on'
    #list_per_page = sys.maxsize
    




admin.site.register(post,Origin)