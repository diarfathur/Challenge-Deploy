from django.contrib import admin
from .models import Post

my_model = [Post]
admin.site.register(my_model)
fields = ( 'image_tag', )
readonly_fields = ( 'image_tag', )