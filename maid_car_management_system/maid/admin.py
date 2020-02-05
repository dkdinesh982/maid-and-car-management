from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Society)
admin.site.register(Residents)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Request_backup)
# admin.site.register(GenerateReport)