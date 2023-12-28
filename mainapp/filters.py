import django_filters
from mainapp.models import *
import datetime

# class CustomNumericRangeFilter(django_filters.Filter):
#     def filter(self, qs, value):
#         if value:
#             value_parts = value.split(',')
#             if len(value_parts) == 2:
#                 min_value, max_value = value_parts
#                 return super().filter(qs, django_filters.fields.Lookup((min_value, max_value), 'range'))
#         return super().filter(qs, value)
    

    
# class ProductFilter(django_filters.FilterSet):
#     # category__id = django_filters.CharFilter(lookup_expr='iexact')
#     # category__name = django_filters.CharFilter(lookup_expr='icontains')
#     # name = django_filters.CharFilter(lookup_expr='icontains')
#     # description = django_filters.CharFilter(lookup_expr='icontains')
#     full_name = django_filters.CharFilter(method='filter_full_name')
#     is_child = django_filters.BooleanFilter()
#     is_actor = django_filters.BooleanFilter()
#     is_model = django_filters.BooleanFilter()
#     gender = django_filters.CharFilter(lookup_expr='contains')
     
#     height = django_filters.RangeFilter()                 
    
#     min_age = django_filters.NumberFilter(method='filter_by_min_age')
#     max_age = django_filters.NumberFilter(method='filter_by_max_age')

#     def filter_by_min_age(self, queryset, name, value):
#         today = datetime.date.today()
#         birth_date = today - datetime.timedelta(days=(int(value) * 365))

#         return queryset.filter(birthday__lte=birth_date)

#     def filter_by_max_age(self, queryset, name, value):
#         today = datetime.date.today()
#         birth_date = today - datetime.timedelta(days=(int(value) * 365))

#         return queryset.filter(birthday__gte=birth_date)
                                            
#     class Meta:
#         model = Profile
#         fields = [ "gender", "height",'is_actor','is_model','is_child','full_name','min_age','max_age']
        
#     def filter_full_name(self, queryset, name, value):
#         return queryset.filter(first_name__icontains=value) | queryset.filter(last_name__icontains=value)
         
# #deyis

# class MagazineFilter(django_filters.FilterSet):
#     # category__id = django_filters.CharFilter(lookup_expr='iexact')
#     # category__name = django_filters.CharFilter(lookup_expr='icontains')
#     # name = django_filters.CharFilter(lookup_expr='icontains')
#     # description = django_filters.CharFilter(lookup_expr='icontains')
#     title = django_filters.CharFilter(lookup_expr='icontains')
                                                       
#     class Meta:
#         model = News
#         fields = ['title']
        
# class NotificationFilter(django_filters.FilterSet):
#     for_model = django_filters.BooleanFilter()
#     for_actor = django_filters.BooleanFilter()
#     for_company = django_filters.BooleanFilter()
#     for_child = django_filters.BooleanFilter()
#     for_none_users = django_filters.BooleanFilter()
                                                       
#     class Meta:
#         model = Notification
#         fields = ['for_model','for_actor','for_company','for_child','for_none_users']
        
        
# full_name = django_filters.CharFilter(field_name='first_name__last_name', lookup_expr='icontains')

class ProductFilter(django_filters.FilterSet):
    size = django_filters.ModelChoiceFilter(queryset=Size.objects.all(), field_name='size__name', label='Size')
    color = django_filters.ModelChoiceFilter(queryset=Color.objects.all(), field_name='color__name', label='Color')
    brand = django_filters.ModelChoiceFilter(queryset=Brand.objects.all(), field_name='brand__name', label='Brand')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['size', 'color', 'brand', 'price__gte', 'price__lte','name']