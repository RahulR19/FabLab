from django.contrib import admin
from .models import Reserve
from .models import Cancel
from .models import Item

admin.site.register(Reserve)
admin.site.register(Cancel)
admin.site.register(Item)
