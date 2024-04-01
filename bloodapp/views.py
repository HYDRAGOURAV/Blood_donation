from django.shortcuts import render,HttpResponse,redirect
from . models import Donor_data,Feedback,contact_details,delete_data_req,payment
from django.contrib import messages
from django.core.paginator import Paginator
# import razorpay
import random

# 404 Page 
def error_404(req,exception):
    return render(req,"error404.html")

def main_page(req):
    return render(req,'Main_Page.html')

def Donor_reg_page_(req):
    return render(req,"Donor_registraction.html")

def Donor_list(req):
    donors=Donor_data.objects.all()
    paginator = Paginator(donors,10)
    page_number = req.GET.get("page")
    page_object = paginator.get_page(page_number)
    # context = {
    #     'donors':donors,
    # }
    return render(req,"Donor_List.html",{'page_object':page_object})

def Help_page(req):
    return render(req,'help_Page.html')

# Add Donor Data 
def Add_Donor_Data(req):
    if req.method == "POST":
        name = req.POST.get('First_Name')
        contact_number = req.POST.get('Contact')
        age = req.POST.get('age')
        email = req.POST.get('email')
        Blood_Group = req.POST.get('Blood_Group')    
        address = req.POST.get('address')
        State = req.POST.get('State')
        City = req.POST.get('City')
        contect_length = len(contact_number)
        if(contect_length==10):
            addDonor = Donor_data(name = name, contact_number = contact_number, 
                                age = age , email = email, Blood_Group= Blood_Group, address = address, State = State, City = City)
            addDonor.save()
            messages.success(req,"Data add Successfully")
        else:
            messages.error(req,"Contact Number  should be of 10 digits.")

def Search_Blood_Data(req):
    return render(req,"Search.html")


def Search_blood_Result(req):
    if req.method =="POST":
        Blood_Group_Name = req.POST.get("Blood_Group_Name")
        Query = Donor_data.objects.filter(Blood_Group__icontains=Blood_Group_Name)
        context = {'Query':Query,}
        return  render(req,"Search.html",context)

def Search_CityName_page(req):
    return render(req,'SearchByCity.html')


def Search_city_Result(req):
    if req.method =="POST":
        City_Name = req.POST.get("City_name")
        Query_1 = Donor_data.objects.filter(City__icontains=City_Name)
        context = {'Query_1':Query_1,}
        return render(req,'SearchByCity.html', context)

def About_Page(req):
    return render(req,"About_Page.html")


def Contact_Page(req):
    return render(req,"Contact.html")
# FeedBack
def feedback_record(req):
    if req.method=="POST":
        FeedBack_email = req.POST.get( "FeedBack_email" )
        FeedBack = req.POST.get("FeedBack")
        Feedback_add = Feedback(FeedBack_email=FeedBack_email, FeedBack=FeedBack)
        Feedback_add.save()
        messages.success(req,"Your FeedBack has been Record  successfully!")
        return  render(req,'help_Page.html')

def user_Contact_Data_add(req):
    if req.method=="POST":
        User_name = req.POST.get("User_name")
        User_email =  req.POST.get("User_email")
        User_message = req.POST.get('User_message')
        Contact_Save = contact_details(User_name=User_name,User_email=User_email,User_message=User_message)
        Contact_Save.save()
        messages.success(req,"Your Contact Data Have Been  Save Successfully.")
        return render(req,"Contact.html")
    

def Modify(req,id):
    get_data = Donor_data.objects.get(id=id)
    return render(req,"Update&delete.html",{'i':get_data})

def Deletedata(req,id):
    print("The data delete Process Panding...",id)



def Payment_Donate_1(req):
    return render(req,'Donation.html')

def Donate_money_function(req):
    if req.method =="POST":
        D_name = req.POST.get("D_name")
        D_email = req.POST.get("D_email")
        D_Amount = req.POST.get("D_Amount")
        def generate_random_number():
            return random.randint(10000000000, 30000000000)
        TransactionID = generate_random_number()
        The_amount_paid = payment(D_name  = D_name , D_email = D_email, D_Amount = D_Amount, TransactionID = TransactionID)
        The_amount_paid.save()
        messages.success(req,"Your  Amount Patch Successfully.")
        return render(req,"Donation.html")

def delete_data_req_admin(req):
    if req.method=="POST":
        SNo = req.POST.get("SNo")
        Delete_Name_req = req.POST.get("Delete_Name_req")
        Delete_Contact_req = req.POST.get("Delete_Contact_req")
        Delete_EMAIL_req= req.POST.get("Delete_EMAIL_req")
        Delete_city_req  = req.POST.get("Delete_req_city")
        Delete_address_req   = req.POST.get("Delete_req_address")
        Delete_Reason   = req.POST.get("Delete_Reason")
        The_delete_Data = delete_data_req(SNo = SNo ,Delete_Name_req= Delete_Name_req, Delete_Contact_req  = Delete_Contact_req, 
                       Delete_EMAIL_req = Delete_EMAIL_req, Delete_city_req = Delete_city_req, Delete_address_req = Delete_address_req,
                        Delete_Reason = Delete_Reason )
        The_delete_Data.save()
        messages.success(req,"Your Data successfully sent to admin for deleting 👍✔✔")
        return render(req,"Update&delete.html")
