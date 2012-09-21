#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import Upload, Campaign, DayEntry


class UploadAdmin(admin.ModelAdmin):
    list_display = ("csv", "loaded", )
    list_filter = ("loaded", )


admin.site.register(Upload, UploadAdmin)


admin.site.register(Campaign)


admin.site.register(DayEntry)

