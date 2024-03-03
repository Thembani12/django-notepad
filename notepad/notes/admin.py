from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser ,Tag ,Note
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.
class UserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['email','username']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    model=Note
    list_display=['title','body','noteuser']


@admin.register(Tag)
class NoteUserAdmin(admin.ModelAdmin):
    model=Tag


admin.site.register(CustomUser,UserAdmin)