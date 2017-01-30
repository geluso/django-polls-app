from django.contrib import admin
from .models import Question, Choice

# StackedInline displays the Choices taking up more space.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
  # specifically defining fields here imposes an order on how
  # the fields are display in the admin panel
  # defining only fields only imposes an order on fields.
  # fields = ['pub_date', 'question_text']
  # defining field sets groups different fields into sections on the page.
  fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date']})
  ]
  inlines = [ChoiceInline]

# We're registering the Question model to display with the
# configured QuestionAdmin class.
admin.site.register(Question, QuestionAdmin)

# Register your models here.
