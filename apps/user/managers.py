from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    """
    Custom user manager to handle user creation and authentication.
    """

    def create_user(self, email, first_name=None, last_name=None, image=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            image=image,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name=None, last_name=None, image=None, password=None, **extra_fields):
        """
        Creates and saves a SuperUser with the given email and password.
        """

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            image=image,
            password=password,
            **extra_fields,
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user
