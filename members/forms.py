from django.forms import ModelForm
from .models import Member, Order
class OrderForm(ModelForm):

    class Meta:
        model = Order
        
    name = AutoCompleteSelectField('members', required=False)