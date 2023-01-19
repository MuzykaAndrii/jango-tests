from django.contrib import admin

from .models import Bb
from .models import Theme


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'theme')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Theme)