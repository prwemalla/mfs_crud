import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from task_service import models as task_service_models


def create_task_service_tasks(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["name"] = ""
    defaults["user_id"] = ""
    defaults["status"] = ""
    defaults.update(**kwargs)
    return task_service_models.tasks.objects.create(**defaults)
