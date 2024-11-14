from django.contrib import admin
from django.utils import timezone
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('request_type', 'status', 'date_submitted', 'date_resolved')
    list_filter = ('status', 'request_type') 
    search_fields = ('request_type', 'status')  
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(status='resolved', date_resolved= timezone.now())
        self.message_user(request, "Selected requests have been marked as resolved.")

    mark_resolved.short_description = "Mark selected requests as resolved"

admin.site.register(ServiceRequest, ServiceRequestAdmin)
