import sys

import django
from django.db import connection
from django.http import JsonResponse


def index(request):
    return JsonResponse(
        {
            "framework": "Django",
            "django": django.get_version(),
            "python": sys.version.split()[0],
            "database": connection.vendor,
        }
    )


def health(request):
    connection.ensure_connection()
    return JsonResponse({"status": "ok"})
