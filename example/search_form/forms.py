from django import forms

from .models import Rubric


# Rubrics = []
# for rubrics in Rubric.objects.all():
#     for category in rubrics.category_set.all():
#         for product in category.product_set.all():
#             Rubrics.append((product.id, product.title))


Rubrics = [(r.id, r.name) for r in Rubric.objects.all()]


class Searchform(forms.Form):
    rub = forms.TypedMultipleChoiceField(label='Rubric', choices=Rubrics,
                                    widget=forms.widgets.CheckboxSelectMultiple(attrs={'size': 6}))
