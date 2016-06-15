from django.contrib import admin

from journal.models import Entry, Skill, Resource


class ResourcesInline(admin.StackedInline):
    model = Resource


class EntryAdmin(admin.ModelAdmin):
    inlines = [ResourcesInline, ]

admin.site.register(Skill)
admin.site.register(Entry, EntryAdmin)
