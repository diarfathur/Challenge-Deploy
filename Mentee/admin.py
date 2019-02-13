from django.contrib import admin
from .models import Mentee

my_model = [Mentee]
admin.site.register(my_model)
fields = ( 'image_tag', )
readonly_fields = ( 'image_tag', )

