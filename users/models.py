# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     USER_TYPES = (
#         ('admin', 'Admin'),
#         ('lecturer', 'Lecturer'),
#         ('student', 'Student'),
#     )
#     user_type = models.CharField(max_length=20, choices=USER_TYPES, default='student')

#     def __str__(self):
#         return f"{self.username} ({self.user_type})"
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any extra fields here if needed
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

