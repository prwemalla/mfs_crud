import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_tasks_list_view():
    instance1 = test_helpers.create_task_service_tasks()
    instance2 = test_helpers.create_task_service_tasks()
    client = Client()
    url = reverse("task_service_tasks_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_tasks_create_view():
    client = Client()
    url = reverse("task_service_tasks_create")
    data = {
        "description": "text",
        "name": "text",
        "user_id": 1,
        "status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_tasks_detail_view():
    client = Client()
    instance = test_helpers.create_task_service_tasks()
    url = reverse("task_service_tasks_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_tasks_update_view():
    client = Client()
    instance = test_helpers.create_task_service_tasks()
    url = reverse("task_service_tasks_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
        "user_id": 1,
        "status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
