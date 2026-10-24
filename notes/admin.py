from django.contrib import admin
from .models import Note, Tag


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
