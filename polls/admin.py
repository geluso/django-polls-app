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
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  # Adding list_filter activates a side panel in the admin interface that
  # let's users filter things easily. It shows options like "Any Date", "Today",
  # "Past 7 Days", "This Month" for DateFields. It only supports certain types
  # of fields by default. Using other fields requires customization.
  # list_filter docs:
  # https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
  # BooleanField, CharField, DateField, DateTimeField, IntegerField, ForeignKey
  # or ManyToManyField
  list_filter = ['pub_date', 'question_text']

# We're registering the Question model to display with the
# configured QuestionAdmin class.
admin.site.register(Question, QuestionAdmin)

# Register your models here.
