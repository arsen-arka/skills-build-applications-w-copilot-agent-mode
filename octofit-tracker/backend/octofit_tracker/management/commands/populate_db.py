from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample data
        marvel_team = {'name': 'Team Marvel', 'members': ['Iron Man', 'Captain America', 'Thor', 'Hulk']}
        dc_team = {'name': 'Team DC', 'members': ['Superman', 'Batman', 'Wonder Woman', 'Flash']}
        db.teams.insert_many([marvel_team, dc_team])

        users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Steve Rogers', 'email': 'cap@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'Team DC'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'Team DC'},
        ]
        db.users.insert_many(users)

        activities = [
            {'user': 'Tony Stark', 'activity': 'Bench Press', 'reps': 20},
            {'user': 'Steve Rogers', 'activity': 'Running', 'distance_km': 5},
            {'user': 'Clark Kent', 'activity': 'Flying', 'distance_km': 1000},
            {'user': 'Bruce Wayne', 'activity': 'Martial Arts', 'duration_min': 60},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {'team': 'Team Marvel', 'points': 1500},
            {'team': 'Team DC', 'points': 1400},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {'name': 'Super Strength', 'suggested_for': ['Hulk', 'Superman']},
            {'name': 'Speed Run', 'suggested_for': ['Flash', 'Quicksilver']},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
