from django.contrib import admin
from .models import DonateMoney, Standard, Subject, Lesson, SundaySermon, DCCYearlyProgram, ChildrenSundaySchool, AdultSundaySchool, DonateMoney, WeeklyPrayersMotivations, WeeklyGiveAway, HistoryOfBabalola, HistoryOfCAC

# Re

class StandardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}


class SundaySermonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class DCCYearlyProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}


class ChildrenSundaySchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class AdultSundaySchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    
class DonateMoneyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class WeeklyPrayersMotivationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class WeeklyGiveAwayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class HistoryOfBabalolaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    
class HistoryOfCACAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    

admin.site.register(SundaySermon, SundaySermonAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(DCCYearlyProgram, DCCYearlyProgramAdmin)
admin.site.register(ChildrenSundaySchool, ChildrenSundaySchoolAdmin)
admin.site.register(AdultSundaySchool, AdultSundaySchoolAdmin)
admin.site.register(DonateMoney, DonateMoneyAdmin)
admin.site.register(WeeklyPrayersMotivations, WeeklyPrayersMotivationsAdmin)
admin.site.register(WeeklyGiveAway, WeeklyGiveAwayAdmin)
admin.site.register(HistoryOfBabalola, HistoryOfBabalolaAdmin)
admin.site.register(HistoryOfCAC, HistoryOfCACAdmin)
