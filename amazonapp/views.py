from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .models import AmzSeries,AmzOrder
from .forms import CardForm,AddCardForm

def index(request):
	if request.method == 'POST':
		form = CardForm(request.POST)
	else:
		form = CardForm()
	if form.is_valid():
		# def cardnumber_present(cardnumber):
		cardnumber = form.cleaned_data['cardnumber']
		if AmzSeries.objects.filter(cardnumber=cardnumber).exists():
			messages.success(request, u'cardnumber "%s" is already in use.<br><img src='"./static/img/core-img/wrong.jpg"'>' % cardnumber,extra_tags='safe')
			return HttpResponseRedirect('/')
			
		
		form.save(commit=True)
		# messages.success(request, 'Scanned Successfully')
		messages.success(request, 
                     '<b>Success</b></br><img src='"./static/img/core-img/tick.jpg"'>.',
                     extra_tags='safe')
		return HttpResponseRedirect('/')
	return render(request,'index.html',{'form':form})

def addorder(request):
	if request.method == 'POST':
		form = AddCardForm(request.POST)
		
	else:
		form = AddCardForm()
	if form.is_valid():
		form.save(commit=True)
		total = 0  
		start_series = int(form.cleaned_data['start_series'])
		total_cards_requirement = int(form.cleaned_data['total_cards_requirement'])
		total = start_series + total_cards_requirement
		print(*range(start_series,total)) 
		amz = AmzOrder(end_series=total)
		amz.save()

		# for x in range(start_series,total):
		# 	print(x)
		# while start_series < total:
		# 	# print(total)
		# 	start_series = start_series + 1
		
		
		print(total)
		messages.success(request, 'Added Successfully')
		return HttpResponseRedirect('/addorder')
	 


	return render(request,'addorder.html',{'form':form})

