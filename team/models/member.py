from django.db import models
import uuid


class Member(models.Model):

    MEMBER_TYPE = (
        ('admin', 'admin'),
        ('regular', 'regular')
    )

    class Meta:
        db_table = 'member'

    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=MEMBER_TYPE)





