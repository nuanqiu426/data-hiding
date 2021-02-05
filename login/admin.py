from django.contrib import admin

# Register your models here.

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):




    #列表页属性
    list_display = ['pk','uid','uname','upassword','uaddress','uemail','uflag']
    list_filter = ['uname']
    search_fields = ['uname']
    list_per_page = 3

    #添加、修改页属性
    fields=[]
    # fieldsets = []