from django.contrib import admin

from .models import *
admin.site.register(Review)
admin.site.register(BookContributor)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Contributor)
# Register your models here.
