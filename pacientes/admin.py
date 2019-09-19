from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from pacientes.models import Profile
from import_export import resources
from import_export.admin import ImportExportModelAdmin




admin.site.unregister(User)



class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
        fields = ('user__first_name','user__username', 'cpf', 'empresa', 'birth_date', 'sexo', 'data_inclusao', 'user__password', 'user__id')

class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource

admin.site.register(Profile, ProfileAdmin)


