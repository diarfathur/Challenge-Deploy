from django.contrib import admin
from .models import Mentor

my_model = [Mentor]
admin.site.register(my_model)
fields = ( 'image_tag', )
readonly_fields = ( 'image_tag', )