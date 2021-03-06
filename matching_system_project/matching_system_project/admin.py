from django.contrib import admin
# from models import Project, Position, Application

from models import Project, Position, Application, UserProfile

admin.site.register(Position)
admin.site.register(Application)
admin.site.register(UserProfile)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectName', 'description')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'fk_CreatedBy', None) is None:
            obj.fk_CreatedBy = request.user
        obj.save()

admin.site.register(Project, ProjectAdmin)
