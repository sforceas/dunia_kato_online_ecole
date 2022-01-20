"""Profile serializer"""

# Django REST Framework
from rest_framework import serializers

# Models
from dkecole.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer"""

    class Meta:
        """Meta class"""
        model = Profile
        fields = (
            'picture',
            'web_page',
            'biography',
            'gender',
            #'country',
            'birth_date',
            'educational_level',
            'is_working',
            'is_workin_role',
            'is_searching_work',
            'interest_bussiness',
            'interest_marketing',
            'interest_fabrication',
            'interest_programming',
            'interest_idiomes',
            'is_public_profile',
            'is_public_name'
        )
        read_only_fields = (

        )


