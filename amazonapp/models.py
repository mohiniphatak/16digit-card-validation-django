from django.db import models
from django.core.validators import RegexValidator

class AmzSeries(models.Model):
	cardnumber = models.CharField(max_length=16,validators=[RegexValidator(r'\d{16,16}','Number must be 16 digits',)])
	
	status = models.CharField(max_length=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	# end_series = models.CharField(max_length=16)
	def __str__(self):
		return self.cardnumber
		# return self.cardtype
		# return self.total_cards_requirement
		# return self.start_series
		return self.status
		return self.timestamp

class AmzOrder(models.Model):

	cardtype = models.CharField(max_length=20)
	total_cards_requirement = models.CharField(max_length=20)
	start_series = models.CharField(max_length=16,validators=[RegexValidator(r'\d{16,16}','Number must be 16 digits',)])
	end_series = models.CharField(max_length=16,default=0)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		# return self.cardnumber
		return self.cardtype
		return self.total_cards_requirement
		return self.start_series
		# return self.status
		# return self.timestamp
		
