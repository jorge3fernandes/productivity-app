from django.contrib import admin

# Register your models here.
from .models import *

# Setting up admins
class WeekAdmin(admin.StackedInline):
    model = Week


class DailyReflectionAdmin(admin.StackedInline):
    model = DailyReflection
    
# Registering Models
@admin.register(TwelveWeek)
class TwelveWeekAdmin(admin.ModelAdmin):
    inlines = [WeekAdmin]

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    inlines = [DailyReflectionAdmin]


@admin.register(DailyReflection)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    pass

@admin.register(Tactic)
class TacticAdmin(admin.ModelAdmin):
    pass








