from .models import *
from django.db.models import Count
from django.core.cache import cache

menu = [{'title': "About", 'url_name': "about"},
        {'title': "Add page", 'url_name': "add_page"},
        {'title': "Contact", 'url_name': "contact"},
        ]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        category = cache.get('category')
        if not category:
            category = Category.objects.annotate(Count('woman'))
            cache.set('category', category, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['category'] = category
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context
