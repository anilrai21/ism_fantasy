from django.contrib import admin

from magnificence.models import Team, ElementType, Element


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "short_name")


@admin.register(ElementType)
class ElementTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "singular_name", "singular_name_short")


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "second_name", "element_type", "team")
