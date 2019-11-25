#############
Wolff Project
#############

Wolff Project is an accounting system made with Django and VueJS.

It is designed with the following assumptions:

    * Installed/served locally

        - each instance of the app should serve only one System Client

    * The system supports multiple company.

        - An instance of the app can have one or more company.
        - Company represents an organization that uses the system and maintains it's own data.
        - These companies belongs or managed by the current System Client
          

===========================
Installation for developers
===========================

    * Install requirements
    * ``python manage.py migrate``
    * ``python manage.py createsuperuser``