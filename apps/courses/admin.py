from django.contrib import admin
from .models import Course,Post,Homework,Review,Question,Response,FilesCourse
# Register your models here.
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(Homework)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(FilesCourse)