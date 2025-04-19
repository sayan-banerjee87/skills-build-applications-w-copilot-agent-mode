from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(username='john_doe', email='john@example.com')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com')

        # Add test teams
        team1 = Team.objects.create(name='Team Alpha', description='Alpha team description')
        team2 = Team.objects.create(name='Team Beta', description='Beta team description')

        # Add test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, distance=5.0)
        Activity.objects.create(user=user2, activity_type='Cycling', duration=60, distance=20.0)

        # Add test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Add test workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run', duration=30)
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session', duration=45)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
