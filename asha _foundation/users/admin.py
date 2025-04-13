from django.contrib import admin
from .models import HouseholdData,Progress_report

@admin.register(HouseholdData)
class HouseholdDataAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user',
        'age',
        'gender',
        'religion',
        'cast',
        'head_of_family',
        'family_male',
        'family_female',
        'earning_members',
        'total_expense',
        'mobile_no',
        'created_at',
    ]
    search_fields = ['name', 'head_of_family', 'user__username', 'religion', 'cast']
    list_filter = ['gender', 'religion', 'cast', 'created_at']
    readonly_fields = ['total_expense', 'created_at']


@admin.register(Progress_report)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan_duration', 'address','plan_amount', 'phone', 'created_at']
    search_fields = ['name', 'plan_duration', 'phone']
    list_filter = ['plan_duration', 'created_at']