"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from dkecole.users.models import User, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  """Profile model admin."""
  list_display = ('user',)
  search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
  list_filter = ()

  fieldsets = (
    ('Profile', {
      'fields': (
        ('user', 'picture'),
        ('biography')
      )
    }),
    ('Stats', {
      'fields': (
      )
    }),
    ('Metadata', {
      'fields': (('created', 'modified'),),
    })
  )

  readonly_fields = ('created', 'modified')

class ProfileInLine(admin.StackedInline):
  model = Profile
  can_delete = False
  verbose_name_plural = 'profiles'

class CustomUserAdmin(UserAdmin):
  """User model admin."""
  #inlines = (ProfileInLine,)
  list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_student')
  list_filter = ('is_student', 'is_staff', 'created', 'modified')

admin.site.register(User, CustomUserAdmin)