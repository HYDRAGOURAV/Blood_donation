from django.contrib import admin
from .models import Donor_data,Feedback,contact_details,payment,delete_data_req
admin.site.register(Donor_data)
admin.site.register(Feedback)
admin.site.register(contact_details)
admin.site.register(payment)
admin.site.register(delete_data_req)
# Register your models here.
