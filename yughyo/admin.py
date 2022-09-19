from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import Iching, Question

# Register your models here.
class IchingResource(resources.ModelResource):

    class Meta:
        model = Iching
        import_id_fields = ['g_id']
        #fields = ('g_id', 'g_name', 'g_content', 'h_content_1', 'h_content_2', 'h_content_3', 'h_content_4', 'h_content_5', 'h_content_6', 'hope', 'consult', 'business', 'trade', 'contract', 'law', 'job', 'promotion', 'school',	'move',	'travel', 'love', 'marry')

class IchingAdmin(ImportExportActionModelAdmin):
    resource_class = IchingResource
    list_display = ['g_id', 'g_name', 'g_content', 'h_content_1', 'h_content_2', 'h_content_3', 'h_content_4', 'h_content_5', 'h_content_6', 'hope', 'consult', 'business', 'trade', 'contract', 'law', 'job', 'promotion', 'school',	'move',	'travel', 'love', 'marry']
    ordering = ['g_id']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'question_text', 'jum')

admin.site.register(Iching, IchingAdmin)
admin.site.register(Question, QuestionAdmin)
