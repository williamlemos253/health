from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from pacientes.models import Profile
from import_export import resources
from import_export.admin import ImportExportModelAdmin




admin.site.unregister(User)
class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.register(User, UserAdmin)


class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource

admin.site.register(Profile, ProfileAdmin)


