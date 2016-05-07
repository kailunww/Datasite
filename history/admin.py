from django.contrib import admin

from models import Master, Log, Category, MasterProxy


def create_modeladmin(modeladmin, model, name=None):
    class Meta:
        proxy = True
        app_label = model._meta.app_label

    attrs = {'__module__': '', 'Meta': Meta}

    newmodel = type(name, (model,), attrs)

    admin.site.register(newmodel, modeladmin)
    return modeladmin


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'tag', 'log_count', 'status', 'year_start', 'year_end', 'remark')
    ordering = ('-year_start',)
    search_fields = ('name', 'category__name', 'tag')


class MasterAdminNotStarted(MasterAdmin):
    list_display = ('name', 'category', 'tag', 'year_start', 'year_end', 'remark')
    ordering = ('-year_start',)
    search_fields = ('name', 'category__name', 'tag')

    # def queryset(self, request):
    #     return self.model.objects.all()

# create_modeladmin(MasterAdminNotStarted, name='Master (Not started)', model=Master)


class LogAdmin(admin.ModelAdmin):
    list_display = ('log_dt', 'master', 'episode')
    ordering = ('-log_dt',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'master_count')

admin.site.register(Master, MasterAdmin)
admin.site.register(MasterProxy, MasterAdminNotStarted)
# admin.site.register(Master, MasterAdminNotStarted)
admin.site.register(Log, LogAdmin)
admin.site.register(Category, CategoryAdmin)
