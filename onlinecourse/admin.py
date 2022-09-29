from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here

class QuestionInline(admin.StackedInline):
    model = Question

class ChoiceInline(admin.StackedInline):
    model = Choice

class SubmissionInline(admin.StackedInline):
    model = Submission

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('question')
    list_filter = ['question']
    search_fields = ['question']

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('choice_text')
    list_filter = ['choice_text']
    search_fields = ['choice_text']

class SubmissionAdmin(admin.ModelAdmin):
    inlines = [SubmissionInline]
    list_display = ('choices')
    list_filter = ['choices']
    search_fields = ['choices']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)