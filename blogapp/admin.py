from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Blog

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "first_name", "last_name")


    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'bio', 'profile_picture', 'job_title', 'facebook', 'twitter', 'instagram', 'linkedin')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )



    # Customize add_fieldsets to include custom fields in the create form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('bio', 'profile_picture', 'job_title', 'facebook', 'twitter', 'instagram', 'linkedin')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)



class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "is_draft")

admin.site.register(Blog, BlogAdmin)


