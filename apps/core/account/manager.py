from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    # We can optionally serialize managers into migrations and have them
    # available in RunPython operations. This is done by defining a
    # use_in_migrations attribute on the manager class:
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """ Creates and saves a User with the given username and password """
        if not username:
            raise ValueError('Username must be needed.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        # these user will be normal user
        extra_fields.setdefault('is_superuser',
                                False)  # Insert key with a value of default if key is not in the dictionary.
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        # These user will be superuser
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have 'is_superuser=True'. ")

        return self._create_user(username, password, **extra_fields)
