from django.contrib import admin
from .models import Publisher

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id','name','main_site','formatted_hit_count','is_active')
    list_display_links = ('id','name')
    list_editable = ('is_active',)

    def formatted_hit_count(self, obj):
        return obj.current_hitcount() if obj.current_hitcount() >0 else '-'
    formatted_hit_count.short_description = 'Просмотры'

admin.site.register(Publisher,PublisherAdmin)