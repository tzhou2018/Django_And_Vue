from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_title = 'MyDjango后台管理'
admin.site.site_header = 'MyDjango'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #设置字段列表
    list_display = ['id', 'name', 'weight', 'size', 'type',]
    list_fields = ['id', 'name', 'type__type_name']
    list_filter = ['name', 'type__type_name']
    ordering = ['id']
    fields = ['name', 'weight', 'size', 'type']
    readonly_fields = ['name']
    list_display.append('colored_type')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['name']
        return self.readonly_fields

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=6)