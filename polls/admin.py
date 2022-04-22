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
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #list_display controls, ya know, how the list displays... was_published_recently is our custom method on the Question model
    list_filter = ["pub_date"]

admin.site.register(Question, QuestionAdmin)
# create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.
