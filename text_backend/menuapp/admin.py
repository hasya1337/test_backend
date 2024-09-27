from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    fk_name = 'menu'
    show_change_link = True


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'order')
    list_filter = ('menu',)
    search_fields = ('title',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
