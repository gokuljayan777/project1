from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in Question.objects.all():
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[
                    ('a', question.option_a),
                    ('b', question.option_b),
                    ('c', question.option_c),
                    ('d', question.option_d),
                ],
                widget=forms.RadioSelect,
                required=True
            )