from django.contrib import admin
from .models import *

class AmzSeriesTable(admin.ModelAdmin):
	list_display = ('id','cardnumber','status','timestamp',) 

class AmzOrderTable(admin.ModelAdmin):
	list_display = ('id','cardtype','total_cards_requirement','start_series',) 
	
	
admin.site.register(AmzSeries,AmzSeriesTable)		
admin.site.register(AmzOrder,AmzOrderTable)





