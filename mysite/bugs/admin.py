from django.contrib import admin
from .models import Bug, Stage
# Register your models here.


class StageInline(admin.TabularInline):
    model = Stage
    extra = 1

class BugAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem', 'create_person', 'create_time')
    list_filter = ['create_time']
    search_fields = ['bug_id', 'problem', 'create_person']
    fieldsets = [
        (None,          {'fields': ['bug_id', 'problem']}),
        ('Bug Details', {'fields': ['create_person', 'create_time', 'note']})
    ]
    inlines = [StageInline]
admin.site.register(Bug, BugAdmin)
