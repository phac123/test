from django.contrib import admin

# Register your models here.
from .models import Users

class StudentsInfo(admin.TabularInline):
    model = Users
    extra = 2

@admin.register(Users) #修饰器
class UsersAdmin(admin.ModelAdmin):
    def gender(self):
        if self.ugender:
            return "男"
        return "女"
    #设置页面列的名称
    gender.short_description = "性别"

    #显示
    list_display = ['pk', 'uaccount', 'upassword', 'uname',
                    'uage', 'ugender', 'uhobby', 'isDelete']
    list_per_page = 10   #分页

    #执行动作
    actions_on_top = False
    actions_on_bottom = True
