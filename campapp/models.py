from django.db import models
from django.contrib.auth.models import User
from django import forms

class College(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    ranking = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='college_logos/', blank=True, null=True)  # Store logos in media/college_logos/

    def __str__(self):
        return self.name


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('Verbal Ability', 'Verbal Ability'),
        ('Analytical Ability', 'Analytical Ability'),
        ('Numerical Ability', 'Numerical Ability'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    text = models.TextField()
    image = models.ImageField(upload_to='media/question_images/', blank=True, null=True)  # New field for images

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')])

    def __str__(self):
        return self.text

class QuizResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Verbal_score = models.IntegerField(default=0)
    Analytical_score = models.IntegerField(default=0)
    Numerical_score = models.IntegerField(default=0)
    recommended_course = models.CharField(max_length=50, blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)  # New field

    def determine_course(self):
        # (Insert the function definition here)
        course_descriptions = {
            'Verbal Ability': "Verbal Ability focuses on language proficiency, communication skills, and logical reasoning. Careers in this field include journalism, content writing, public relations, and teaching.",
            'Analytical Ability': "Analytical Ability involves problem-solving, logical thinking, and data interpretation. Fields such as data science, finance, business analytics, and research require strong analytical skills.",
            'Numerical Ability': "Numerical Ability emphasizes mathematical reasoning, quantitative aptitude, and statistical analysis. Career opportunities include engineering, finance, actuarial sciences, and economics.",
        }

        scores = {
            'Verbal Ability': self.Verbal_score,
            'Analytical Ability': self.Analytical_score,
            'Numerical Ability': self.Numerical_score,
        }
    
    # Get the category with the highest score
        self.recommended_course = max(scores, key=scores.get)
    
    # Assign the corresponding description
        self.course_description = course_descriptions[self.recommended_course]
    
        self.save()
        return self.recommended_course
    
class Courses(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Duration in years")
    fee = models.DecimalField(max_digits=10, decimal_places=2)