from django.db import models

# model -> jadval yaratish
class Book(models.Model):
    title = models.CharField(max_length=200)  # qisqa nom uchun
    author = models.CharField(max_length=100, default="Unknown Author")  # muallif uchun default qiymat
    description = models.TextField()  # uzun matin uchun
    created_at = models.DateTimeField(auto_now_add=True)  # yuklangan sana
    updated_at = models.DateTimeField(auto_now=True)  # oxirgi o'zgarish
    ISBN = models.CharField(max_length=13, null=True, unique=True)  # ISBN raqamini matnli maydonda saqlash
    pages = models.IntegerField(default=0)  # sahifalar
    language = models.CharField(max_length=30, default="Unknown language")  # til
    book_category = models.CharField(max_length=50, default="Unknown book_category")  # kitob janiri

    def __str__(self):
        return self.title
