from django.contrib import admin


from .models import Survey, Question, SurveyOptions

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(SurveyOptions)
# Register your models here.
