from django.conf import settings

from django_jinja_knockout.views import ListSortingView, ContextDataMixin

from .models import Action


class ActionList(ContextDataMixin, ListSortingView):

    model = Action
    paginate_by = settings.OBJECTS_PER_PAGE
    grid_fields = [
        'performer',
        'date',
        'action_type',
        'content_object'
    ]
    allowed_sort_orders = [
        'performer',
        'date',
        'action_type',
    ]

    def get_allowed_filter_fields(self):
        allowed_filter_fields = {
            'action_type': None,
            'content_type': self.get_contenttype_filter(
                ('club_app', 'club'),
                ('club_app', 'equipment'),
                ('club_app', 'member'),
            )
        }
        return allowed_filter_fields