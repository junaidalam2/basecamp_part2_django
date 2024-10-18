from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwards):

        users_data = [
            {'email': 'admin@gmail.com', 'first_name': 'adminFirst1', 'last_name': 'adminLast1', 'permissions': 'admin'},
            {'email': 'user1@gmail.com', 'first_name': 'fakeFirstName1', 'last_name': 'fakeLastName1', 'permissions': 'user'},
            {'email': 'user2@gmail.com', 'first_name': 'fakeFirstName2', 'last_name': 'fakeLastName2', 'permissions': 'user'},
            {'email': 'user3@gmail.com', 'first_name': 'fakeFirstName3', 'last_name': 'fakeLastName3', 'permissions': 'user'},
            {'email': 'user4@gmail.com', 'first_name': 'fakeFirstName4', 'last_name': 'fakeLastName4', 'permissions': 'user'},
            {'email': 'user5@gmail.com', 'first_name': 'fakeFirstName5', 'last_name': 'fakeLastName5', 'permissions': 'user'},
            {'email': 'user6@gmail.com', 'first_name': 'fakeFirstName6', 'last_name': 'fakeLastName6', 'permissions': 'user'},
            {'email': 'user7@gmail.com', 'first_name': 'fakeFirstName7', 'last_name': 'fakeLastName7', 'permissions': 'user'},
            {'email': 'user8@gmail.com', 'first_name': 'fakeFirstName8', 'last_name': 'fakeLastName8', 'permissions': 'user'},
            {'email': 'user9@gmail.com', 'first_name': 'fakeFirstName9', 'last_name': 'fakeLastName9', 'permissions': 'user'},
            {'email': 'user10@gmail.com', 'first_name': 'fakeFirstName10', 'last_name': 'fakeLastName10', 'permissions': 'user'},
        ]

        for user_data in users_data:
            if not CustomUser.objects.filter(email=user_data['email']).exists():
                CustomUser.objects.create_user(
                    email=user_data['email'],
                    password='password1',
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name']
                )

                self.stdout.write(self.style.SUCCESS(f"User {user_data['email']} created!"))
            else:
                self.stdout.write(self.style.WARNING(f"User {user_data['email']} already exists. Skipping."))
