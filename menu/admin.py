from django.contrib import admin
from .models import Menu, Vegetable, Desserts, Plate, StreetFood, Snacks, Beverages, Breads, Rice


class MenuAdmin(admin.ModelAdmin):
    list_display = ("category", "updated", "created", )
    search_fields = ("category", )
    list_filter = ("created", "updated", )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Vegetable)
admin.site.register(Desserts)
admin.site.register(Plate)
admin.site.register(Snacks)
admin.site.register(StreetFood)
admin.site.register(Breads)
admin.site.register(Beverages)
admin.site.register(Rice)
