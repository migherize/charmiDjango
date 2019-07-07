from django.contrib import admin

# Register your models here.

from charmi.models import *

#admin.site.unregister(U)

admin.site.register(Profile)

admin.site.register(Photo)
admin.site.register(Game)
admin.site.register(Address)
admin.site.register(Ranking)
admin.site.register(Followers)
admin.site.register(Game_list)
admin.site.register(Opponents)
