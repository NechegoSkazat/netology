from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, TagArticle


class TagArticleFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data:
                counter += 1
        if counter < 1:
            raise ValidationError('Укажите основной раздел')
        elif counter > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class TagArticleInline(admin.TabularInline):
    model = TagArticle
    formset = TagArticleFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagArticleInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
