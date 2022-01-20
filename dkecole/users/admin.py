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
        ('biography'),
        ('web_page'),
        ('country','gender','birth_date'),
        ('educational_level'),
        ('is_working','is_workin_role'),
        ('is_searching_work'),
      )
    }),
    
    ('Stats', {
      'fields': (
        ('points','answers','questions'),
        ('courses_joined','courses_completed'),
        )
    }),

    ('Interests', {
      'fields': (
        'interest_bussiness','interest_marketing','interest_fabrication','interest_programming','interest_idiomes'
      )
    }),

    ('Privacity', {
      'fields': ('is_public_profile', 'is_public_name'),
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
  readonly_fields = ('created', 'modified')

admin.site.register(User, CustomUserAdmin)