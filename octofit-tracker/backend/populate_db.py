import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Clear existing data
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Workout.objects.all().delete()
Leaderboard.objects.all().delete()

# Create test users
user1 = User.objects.create(email="john.doe@example.com", name="John Doe", age=30)
user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", age=25)

# Create test teams
team1 = Team.objects.create(name="Team Alpha")
team1.members.add(user1, user2)

# Create test activities
Activity.objects.create(user=user1, type="Running", duration=45, date=date(2025, 4, 7))
Activity.objects.create(user=user2, type="Cycling", duration=60, date=date(2025, 4, 6))

# Create test workouts
Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session", duration=30)
Workout.objects.create(name="Evening Cardio", description="High-intensity cardio workout", duration=40)

# Create test leaderboard entries
Leaderboard.objects.create(user=user1, score=150, rank=1)
Leaderboard.objects.create(user=user2, score=120, rank=2)

print("Test data populated successfully.")
