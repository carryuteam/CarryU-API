from django.contrib import admin

from .models import Resource
from .models import ResouceTag
from .models import ResouceFolder,ResouceComment
# Register your models here.

admin.site.register(Resource)
admin.site.register(ResouceFolder)
admin.site.register(ResouceTag)
admin.site.register(ResouceComment)
# Register your models here.
