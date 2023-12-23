from django_filters import FilterSet, DateFilter, ChoiceFilter
from django.forms import DateInput
from .models import Post


class PostFilter(FilterSet):
    tanks = 'Танки'
    healers = 'Хилеры'
    damagers = 'ДД'
    merchants = 'Торговцы'
    guildmasters = 'Гилдмастеры'
    questgivers = 'Квестгиверы'
    warsmiths = 'Кузнецы'
    tanners = 'Кожевенники'
    potionmasters = 'Зельевары'
    spellmasters = 'Мастера заклинаний'
    ANN_CATEGORIES = [
        (tanks, "Танки"),
        (healers, "Хилы"),
        (damagers, "ДД"),
        (merchants, "Торговцы"),
        (guildmasters, "Гилдмастеры"),
        (questgivers, "Квестгиверы"),
        (warsmiths, "Кузнецы"),
        (tanners, "Кожевники"),
        (potionmasters, "Зельевары"),
        (spellmasters, "Мастера заклинаний")
    ]

    time = DateFilter(
        field_name = 'post_time',
        label = 'Дата (позже)',
        lookup_expr = 'gt',
        widget = DateInput(
            attrs = {
                'type': 'date',
            }
        ),
    )

    category = ChoiceFilter(
    field_name = 'category',
    choices = ANN_CATEGORIES,
    label = 'Категория',
    )

    class Meta:
        model = Post
        fields = {
            'author__username' : ['iexact'],
            'title' : ['icontains'],
        }

    def get_choices(self):
        return Post.objects.values_list('category', flat=True).distinct()