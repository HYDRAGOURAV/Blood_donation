from django.contrib import admin

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('Donor_reg_page', views.Donor_reg_page_, name='Donor_reg_page'),
    path('Donor_List', views.Donor_list, name='Donor_List'),
    path('Home', views.main_page, name='Home'),
    path('Help', views.Help_page, name='Help'),
    path('Add_Data', views.Add_Donor_Data, name='Add_Data'),
    path('Search_Blood', views.Search_Blood_Data, name='Search_Blood'),
    path('Search_blood_group', views.Search_blood_Result, name='Search_blood_group'),
    path('Search_CityName', views.Search_CityName_page, name='Search_CityName'),
    path('Search_city', views.Search_city_Result, name='Search_city'),
    path('About_Page', views.About_Page, name='About_Page'),
    path('Contact', views.Contact_Page, name='Contact'),
    path('feedback', views.feedback_record, name='feedback'),
    path('user_Contact_Data', views.user_Contact_Data_add, name='user_Contact_Data'),
    path('Modify/<int:id>', views.Modify, name='Modify'),
    path('Delete_data/<int:id>', views.Deletedata, name='Delete_data'),
    path('Payment_Donate', views.Payment_Donate_1, name='Payment_Donate'),
    path('Donate_money', views.Donate_money_function, name='Donate_money'),
    path('delete_data_req', views.delete_data_req_admin, name='delete_data_req'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

