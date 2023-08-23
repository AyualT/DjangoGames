from django.contrib import admin
from .models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','title','studio','publisher','genre','price','formatted_hit_count','is_active')
    list_display_links = ('id','title')
    list_editable = ('price','is_active','genre','studio','publisher')
    list_filter = ('release_date','is_active','genre','studio','publisher')
    search_fields = ('title','desc')

    def formatted_hit_count(self, obj):
        return obj.current_hitcount() if obj.current_hitcount() >0 else '-'
    formatted_hit_count.short_description = 'Просмотры'

admin.site.register(Game, GameAdmin)
admin.site.register(Genre)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','game','author','comment','rating','get_like_dislike_count')
    list_display_links = ('id','game')
    def get_like_dislike_count(self, obj):
        lcount = ReviewLike.objects.filter(review_id = obj.pk, value = 1).count()
        dlcount = ReviewLike.objects.filter(review_id = obj.pk, value = 0).count()
        if lcount==0:
            lcount='-'
        if dlcount==0:
            dlcount='-'
        return f'{lcount} | {dlcount}'
    get_like_dislike_count.short_description = 'Likes/Dislikes'

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewLike)