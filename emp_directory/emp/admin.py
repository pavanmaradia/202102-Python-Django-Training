from django.contrib import admin

# Register your models here.
from .models import Employee, City, State, Country, BankDetail, SkillSet, Accounts


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'city', 'state', 'country']
    search_fields = ('first_name', 'last_name')
    list_filter = ['age']
    list_editable = ('age', 'city', 'state', 'country')


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name',)


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name',)



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(BankDetail)
admin.site.register(SkillSet)
admin.site.register(Accounts)
