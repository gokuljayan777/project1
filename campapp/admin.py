from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(College)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category')  # Display fields
    ordering = ('category', 'text')  # Sort by category first, then by question text
    search_fields = ('text',)  # Add search functionality
    list_filter = ('category',)  # Add filter option by category
admin.site.register(QuizResult)
admin.site.register(Courses)