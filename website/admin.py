from django.contrib import admin
from .models import Record,Department,Organization,Lead,Type,Contacts


# Register your models here.

admin.site.register(Record)
admin.site.register(Department)
admin.site.register(Organization)
admin.site.register(Lead)
admin.site.register(Type)
admin.site.register(Contacts)


#by adding this code we can view records in the admin section of web page