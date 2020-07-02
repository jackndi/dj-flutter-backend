from django.contrib import admin

from . import  models


admin.site.register(models.Course)
admin.site.register(models.TrackableItem)
admin.site.register(models.QRCode)
admin.site.register(models.TimeRecord)
admin.site.register(models.CourseUser)
