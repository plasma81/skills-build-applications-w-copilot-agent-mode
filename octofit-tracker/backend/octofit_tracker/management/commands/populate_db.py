from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Spider-Man', type='Running', duration=30),
            Activity(user='Iron Man', type='Cycling', duration=45),
            Activity(user='Wonder Woman', type='Swimming', duration=60),
            Activity(user='Batman', type='Yoga', duration=20),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Create workouts
        workouts = [
            Workout(name='Cardio Blast', difficulty='Medium'),
            Workout(name='Strength Training', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        # Ensure unique index on email for users collection
        with connection.cursor() as cursor:
            cursor.execute('''db.users.createIndex({ "email": 1 }, { "unique": true })''')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
