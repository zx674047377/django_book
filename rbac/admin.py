from django.contrib import admin

# Register your models here.
from rbac.models import Permission, Role, User

admin.site.register(Permission)

admin.site.register(Role)

admin.site.register(User)
