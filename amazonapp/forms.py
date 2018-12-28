from django import forms
from .models import AmzSeries,AmzOrder

class CardForm(forms.ModelForm):
	class Meta:
		model = AmzSeries
		fields = ('cardnumber',)

class AddCardForm(forms.ModelForm):
	class Meta:
		model = AmzOrder
		fields = ('cardtype','total_cards_requirement', 'start_series', )

# class AddCardForm(forms.ModelForm):
# 	class Meta:
# 		model = AmzSeries
# 		fields = ('cardnumber',)
