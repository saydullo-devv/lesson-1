from django.contrib import admin
from  .models import Book

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'created_at', 'updated_at', 'language','pages',)
