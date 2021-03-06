from django.core.management import call_command

from celery import task


@task
def syncldap():
    """
    Call the appropriate management command to synchronize the LDAP users
    with the local database.
    """
    call_command('syncldap')
