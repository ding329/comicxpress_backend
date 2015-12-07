from django.contrib import admin
#from comicxpress_backend.api.models import *
from api.models import *


admin.site.register(catalog, catalogAdmin)
admin.site.register(monthlyorder, monthlyorderAdmin)
admin.site.register(previewselections, previewselectionsAdmin)
# Register your models here.
