from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2025-04-08")
        self.assertEqual(activity.type, "Running")

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick morning run", duration=30)
        self.assertEqual(workout.name, "Morning Run")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.score, 100)
