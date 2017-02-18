# django-runas

Impersonate a user using the Django admin.

## Installation and configuration

1. `pip install django-runas`
2. Add `runas` to the bottom of your `INSTALLED_APPS`
3. Add `runas.middleware.RunAsMiddleware` to `MIDDLEWARE_CLASSES` or `MIDDLEWARE`
4. Add the following url include to your `urlpatterns`, underneath where you have included the admin site:

       url("^admin/", include(admin.site.urls)),
       url("^admin/runas/", include('runas.urls')),

5. (Optional) If you would like a banner to display on each page of the site when you are impersonating a user,
   add the following to your base template:

       {% load runas_tags %}
       {% runas_banner %}

6. Log in to the admin and navigate to the change page of a user, and you will see in the top right a new
   button called "Impersonate user".
