from django.test import TestCase
from rest_framework.test import APIClient
from .models import UserProfile, Project, Category, Country
from django.contrib.auth.models import User
from faker import Faker
import random



class RecommendationSystemTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        
        test_categories = [
            Category.objects.create(name='Technology'),
            Category.objects.create(name='Healthcare'),
            Category.objects.create(name='Finance'),
            Category.objects.create(name='Education'),
            Category.objects.create(name='Retail'),
            Category.objects.create(name='Food & Beverage'),
            Category.objects.create(name='Transportation'),
            Category.objects.create(name='Manufacturing'),
            Category.objects.create(name='Real Estate'),
            Category.objects.create(name='Energy'),
            Category.objects.create(name='Media'),
            Category.objects.create(name='Entertainment'),
            Category.objects.create(name='Telecommunications'),
            Category.objects.create(name='Hospitality'),
            Category.objects.create(name='Construction'),
            Category.objects.create(name='Agriculture'),
            Category.objects.create(name='Mining'),
            Category.objects.create(name='Pharmaceuticals'),
            Category.objects.create(name='Biotechnology'),
            Category.objects.create(name='Engineering'),
            Category.objects.create(name='Automotive'),
            Category.objects.create(name='Aerospace'),
            Category.objects.create(name='Chemical'),
            Category.objects.create(name='Textile'),
            Category.objects.create(name='Tourism'),
            Category.objects.create(name='Sports'),
            Category.objects.create(name='Gaming'),
        ]
        test_countries = [
            # South East Asia
            Country.objects.create(name='Brunei'),
            Country.objects.create(name='Cambodia'),
            Country.objects.create(name='Indonesia'),
            Country.objects.create(name='Laos'),
            Country.objects.create(name='Malaysia'),
            Country.objects.create(name='Myanmar'),
            Country.objects.create(name='Philippines'),
            Country.objects.create(name='Singapore'),
            Country.objects.create(name='Thailand'),
            Country.objects.create(name='Timor-Leste'),
            Country.objects.create(name='Vietnam'),
            # East Asia
            Country.objects.create(name='China'),
            Country.objects.create(name='Hong Kong'),
            Country.objects.create(name='Japan'),
            Country.objects.create(name='Macao'),
            Country.objects.create(name='Mongolia'),
            # South Asia
            Country.objects.create(name='Bangladesh'),
            Country.objects.create(name='Bhutan'),
            Country.objects.create(name='India'),
            Country.objects.create(name='Maldives'),
            Country.objects.create(name='Nepal'),
            Country.objects.create(name='Pakistan'),
            Country.objects.create(name='Sri Lanka'),
            # Central Asia
            Country.objects.create(name='Kazakhstan'),
            Country.objects.create(name='Kyrgyzstan'),
            Country.objects.create(name='Tajikistan'),
            Country.objects.create(name='Turkmenistan'),
            Country.objects.create(name='Uzbekistan'),
            # West Asia
            Country.objects.create(name='Afghanistan'),
            Country.objects.create(name='Armenia'),
            Country.objects.create(name='Azerbaijan'),
            Country.objects.create(name='Bahrain'),
            Country.objects.create(name='Cyprus'),
            Country.objects.create(name='Georgia'),
            Country.objects.create(name='Iran'),
            Country.objects.create(name='Iraq'),
        ]
        # Create multiple users with distinct preferences
        self.users = []
        for i in range(5):
            # Create a new user
            user = User.objects.create_user(
                username=f'testuser{i}', 
                password='testpassword'
            )

            # Create a profile for each user with distinct preferences
            user_profile = UserProfile.objects.create(
                user=user, email=self.fake.email(), 
                company_name=self.fake.company(), 
                interests=self.fake.bs(),
            )
            user_profile.preferred_categories.add(random.choice(test_categories))
            user_profile.preferred_countries.add(random.choice(test_countries))
            
            self.users.append(user)

            # Create projects for each user
            for j in range(2):
                title = f"Next-Gen {self.fake.catch_phrase()} Platform"
                description = f"This project aims to revolutionize {self.fake.bs()} using technologies like {self.fake.word(ext_word_list=['AI', 'Blockchain', 'IoT'])}."
                
                Project.objects.create(
                    title=f'{title}', 
                    description=f'{description}',
                    user=user,
                    category=random.choice(test_categories),
                    location=random.choice(test_countries).name,
                    investment_sought=random.randint(10000, 50000) * j
                )

    def test_recommendation_retrieval(self):
        for user in self.users:
            client = APIClient()
            client.force_authenticate(user=user)
            response = client.get('/api/recommendations/')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.data, dict)
            self.assertIn('recommendations', response.data)
            # print(f"User: {user.username}, Recommendations: {response.data['recommendations']}")
            self.assertTrue(len(response.data['recommendations']) == 5)
            # for project in response.data['recommendations']:
            #     print(project['title'])

    # def test_recommendation_retrieval_without_auth(self):
    #     client = APIClient()
    #     response = client.get('/api/recommendations/')
    #     self.assertEqual(response.status_code, 403)