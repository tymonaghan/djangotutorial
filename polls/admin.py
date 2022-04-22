from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
# create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.