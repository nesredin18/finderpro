from django.contrib import admin
from .models import about,region,city,contact_us,help,privacy,terms,faq

# Register your models here.
admin.site.register(about)
admin.site.register(region)
admin.site.register(city)
admin.site.register(contact_us)
admin.site.register(help)
admin.site.register(privacy)
admin.site.register(terms)
admin.site.register(faq)
