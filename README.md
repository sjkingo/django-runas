# django-runas

Impersonate a user using the Django admin.

[![Latest version](https://img.shields.io/pypi/v/django-runas.svg)](https://pypi.python.org/pypi/django-runas)
[![Python support](https://img.shields.io/pypi/pyversions/django-runas.svg)](https://github.com/sjkingo/django-runas)
[![BSD License](https://img.shields.io/pypi/l/django-runas.svg)](https://pypi.python.org/pypi/django-runas)

## Installation and configuration

1. `$ pip install django-runas`
2. Add `runas` to the bottom of your `INSTALLED_APPS`
3. Add `runas.middleware.RunAsMiddleware` to the bottom of `MIDDLEWARE_CLASSES` or `MIDDLEWARE`
4. Add the following to your `urlpatterns`, underneath where you have included the admin site (this is important):

    ```python
    url("^admin/", include(admin.site.urls)),
    url("^admin/runas/", include('runas.urls')),
    ```

5. (Optional) If you would like a banner to display on each page of the site when you are impersonating a user,
   add the following to your base template:

    ```django
    {% load runas_tags %}
    {% runas_banner %}
    ```

6. Log in to the admin and navigate to the change page of a user, and you will see in the top right a new
   button called ***Impersonate \<user\>***
