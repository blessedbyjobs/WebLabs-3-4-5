from django.contrib import admin

from app.models import Student, University, Lecturer, Subject, ExamMark


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)


class UniversityAdmin(admin.ModelAdmin):
    pass
admin.site.register(University, UniversityAdmin)


class LecturerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lecturer, LecturerAdmin)


class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject, SubjectAdmin)


class ExamMarkAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExamMark, ExamMarkAdmin)
