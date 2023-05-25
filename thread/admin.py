from django.contrib import admin
from .models import account
from .models import user_type
from .models import lost_P,lost_i
from .models import found_P,found_i
from .models import wanted_p,matched_p,matched_i,item_type,person_type

# Register your models here.
admin.site.register(account)
admin.site.register(user_type)
admin.site.register(lost_P)
admin.site.register(found_P)
admin.site.register(wanted_p)
admin.site.register(matched_p)
admin.site.register(lost_i)
admin.site.register(found_i)
admin.site.register(matched_i)
admin.site.register(item_type)
admin.site.register(person_type)
