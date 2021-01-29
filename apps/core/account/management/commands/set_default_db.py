from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Set all default models objects to setup default db.'

    def handle(self, *args, **kwargs):
        print('[+] Resource: ', end='')
        call_command('loaddata', 'import_sql/resource.json')
        print('[+] Permission: ', end='')
        call_command('loaddata', 'import_sql/permission.json')
        print('[+] Role: ', end='')
        call_command('loaddata', 'import_sql/role.json')
        print('[+] User: ', end='')
        call_command('loaddata', 'import_sql/user.json')

