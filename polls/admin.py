from django.contrib import admin
from .models import Question, Choice

# Register your models here.

#note the change to TabularInline (vs StackedInline)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.
