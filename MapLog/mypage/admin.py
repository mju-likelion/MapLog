from django.contrib import admin
from .models import By_date

class By_dateAdmin(admin.ModelAdmin):
  list_display = ('id', 'start_date', 'end_date')
admin.site.register(By_date, By_dateAdmin)

