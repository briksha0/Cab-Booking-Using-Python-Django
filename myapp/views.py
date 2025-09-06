from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myapp.models import *
import razorpay
from django.conf import settings
from avt import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

client = razorpay.Client(auth=("rzp_live_QMEG4rXlMpzUbV", "IRRoscnGfpYe3k8bNT3HuNHv"))


# Create your views here.


def submit_booking(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        pickup = request.POST.get('pickup_location')
        dropoff = request.POST.get('dropoff_location')
        trip_type = request.POST.get('trip_type')
        phone = request.POST.get('phone_number')

        # TODO: Process/save data as needed

        # ✅ Render home.html after submission
        return render(request, 'home.html')  # must be inside templates/
    
    # Optionally handle non-POST
    return redirect('home')
def cars_view(request):
    return render(request, 'cars.html') 

def about_view(request):
    return render(request, 'about.html')

def index_view(request):
    return render(request, 'home.html')
def photo_view(request):
    return render(request, 'photo.html')
def contact_view(request):
    return render(request, 'contact.html')

def home(request):
    page2data=page2.objects.all()
    page3data=page3.objects.all()
    page4data=page4.objects.all()
    page3hdata=PAGE3HEADING.objects.all()
    page5hdata=PAGE5HEADING.objects.all()
    page5pdata=PAGE5_PARA.objects.all()
    page5idata=PAGE5_IMG.objects.all()
    page7hdata=PAGE7HEADING.objects.all()
    page7imgdata=page7img.objects.all()
    page7infodata=page7info.objects.all()
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()
    conditions = TermsAndConditions.objects.all()

    data={
        'page2data':page2data,
        'page3data':page3data,
        'page3hdata':page3hdata,
        'page4data':page4data,
        'page5hdata':page5hdata,
        'page5pdata':page5pdata,
        'page5idata':page5idata,
        'page7hdata':page7hdata,
        'page7imgdata':page7imgdata,
        'page7infodata':page7infodata,
        'pickupLocation':pickupLocation,
        'droplocation':droplocation,
        'conditions':conditions
    }
    return render(request,"home.html",data)

def saveCabdata(request):
    if request.method=="POST":
        pickup=request.POST.get('pickup')
        drop=request.POST.get('drop')
        number=request.POST.get('number')
        cab=cabEnquiry(pickup=pickup,drop=drop,number=number)
        cab.save()
    return render(request,"home.html")

def about(request):
    page2data=page2.objects.all()
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()
    page5hdata=PAGE5HEADING.objects.all()
    page5pdata=PAGE5_PARA.objects.all()
    page5idata=PAGE5_IMG.objects.all()

    data={
        'page2data':page2data,
        'pickupLocation':pickupLocation,
        'droplocation':droplocation,
        'page5hdata':page5hdata,
        'page5pdata':page5pdata,
        'page5idata':page5idata,
    }
    return render(request,"about.html",data)

def contact(request):
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()

    data={
        'pickupLocation':pickupLocation,
        'droplocation':droplocation,
    }
    return render(request,"contact.html",data)

def submitdataContact(request):
    if request.method == 'POST':
        a = request.POST["uname"]
        b = request.POST["uphone"]
        c = request.POST["uemail"]
        d = request.POST["umessage"]
        obj = ContactUsFormData(name= a , email = c, phone = b, message = d)
        obj.save()
        return render(request,"contact.html")

def travellers(request):
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()
    page5hdata=PAGE5HEADING.objects.all()
    page5pdata=PAGE5_PARA.objects.all()
    page5idata=PAGE5_IMG.objects.all()

    data={
        'pickupLocation':pickupLocation,
        'droplocation':droplocation,
        'page5hdata':page5hdata,
        'page5pdata':page5pdata,
        'page5idata':page5idata,
    }
    return render(request,"travellers.html",data)

def reservation(request):
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()

    data={
        'pickupLocation':pickupLocation,
        'droplocation':droplocation,
    }
    return render(request,"reservation.html",data)

def submitdataResrvation(request):
    if request.method == 'POST':
        a = request.POST["uname"]
        b = request.POST["uphone"]
        c = request.POST["uemail"]
        d = request.POST["umessage"]
        obj = ContactUsFormData(name= a , email = c, phone = b, message = d)
        obj.save()
        return render(request,"reservation.html")

def cars2(request):
    return render(request,"cars2.html")

def carsform(request):
    return render(request,"cars2.html")

def directions(request,my_id):
    cars=Carstype.objects.all()
    conditions = TermsAndConditions.objects.all()
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()
    return render(request,"directions.html",{'cars':cars,'conditions':conditions,'pickupLocation':pickupLocation,'droplocation':droplocation})

def direction2(request,my_id2):
    tempo=Tempo.objects.all()
    conditions = TermsAndConditions.objects.all()
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()
    return render(request,"direction2.html",{"tempo":tempo,'conditions':conditions,'pickupLocation':pickupLocation,'droplocation':droplocation})

@csrf_exempt
def submitdata(request):
    print("hello")
    if request.method == "POST":
        print("hey")
        a = request.POST["uname"]
        b = request.POST["uemail"]
        c = request.POST["uphone"]
        d = request.POST["upickuptime"]
        # e=request.POST["totalprice"]
        f = request.POST["ucarname"]
        g=request.POST['pick']
        h=request.POST['drop']
        i=request.POST['upickupDate']
        way=request.POST['way']
        if way=="Roundway":
            wa="Two"
        else:
            wa="One"
        print(e,f)
        # g = request.POST["other.. data"]
        s=float(e)
        amount=s*10
        obj = BookingCab.objects.create(username=a,email=b,phone=c,pick_up_time=d,cab=f,total_price=amount, pick_up_location=g,drop_location=h,advance_payment=e,way=wa)      
        order = None   
        payment = None
      
        currency="INR"
        notes={
            'email':b
        }
        order = client.order.create(
                {
                    
            'notes' : notes,
            'amount' : amount,
            'currency' : currency
            })
        payment=Payment()
        payment.phone=c
        payment.pickup=g
        payment.drop=h
        payment.amount=e
        payment.order_id=order.get('id')
        payment.save()
        return render(request,"directions.html",{'order':order})

def submitdata2(request):
    print("hello")
    if request.method == "POST":
        print("hey")
        a = request.POST["uname"]
        b = request.POST["uemail"]
        c = request.POST["uphone"]

        e=request.POST["totalprice"]
        f = request.POST["ucarname"]
        g=request.POST['pick']
        h=request.POST['drop']
        i=request.POST['ddate']
        j=request.POST['adate']
        print(e,f)
        
        s=float(e)
        amount=s*10
        print(amount,"new")
        obj = BookingCab.objects.create(username=a,email=b,phone=c,cab=f,total_price=e, pick_up_location=g,drop_location=h,departure_date=i,arrival_date=j,advance_payment=amount)
        order = None   
        payment = None
        
        currency="INR"
        notes={
            'email':b
        }
        order = client.order.create(
                {
                    
            'notes' : notes,
            'amount' : amount,
            'currency' : currency
            })
        payment=Payment()
        payment.phone=c
        payment.pickup=g
        payment.drop=h
        payment.amount=e
        payment.order_id=order.get('id')
        payment.save()
        return render(request,"direction2.html",{'order':order})
@csrf_exempt
def verify_payment(request):
     if request.method=="POST":
        data=request.POST 
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            
            payment = Payment.objects.get(order_id=razorpay_order_id)
            phone=payment.phone
            payment.payment_id = razorpay_payment_id
            payment.status = True
            book_cap=BookingCab.objects.filter(phone=phone).last()
            book_cap.booking_id=book_cap.id
            c=float(book_cap.total_price)
            d=float(book_cap.advance_payment)
            e=c-d
            print(c,d)
            book_cap.is_paid=True
            book_cap.amount_to_pay=e
        
            book_cap.save()
            payment.bookcap = book_cap
            payment.save()
            
            print(phone)
            a=BookingCab.objects.filter(is_paid=True,phone=phone)
            b=BookingCab.objects.filter(is_paid=True,phone=phone).last()
            

            print("ye hai payed:",a)
            html_content=render_to_string("email.html",{'b':b})
            text_content=strip_tags(html_content)
            email=EmailMultiAlternatives(
                "Your AST CAB confirmation",
                text_content,
                settings.EMAIL_HOST_USER,
                [book_cap.email],
                )
            email.attach_alternative(html_content,"text/html")
            
            email.send(fail_silently=True)
            
            return render(request,'reciept.html',{'b':b})

        except:
           return HttpResponse("invalid payment details")   

    
def home2(request):
    page2data=page2.objects.all()
    page3data=page3.objects.all()
    page4data=page4.objects.all()
    page3hdata=PAGE3HEADING.objects.all()
    page5hdata=PAGE5HEADING.objects.all()
    page5pdata=PAGE5_PARA.objects.all()
    page5idata=PAGE5_IMG.objects.all()
    page7hdata=PAGE7HEADING.objects.all()
    page7imgdata=page7img.objects.all()
    page7infodata=page7info.objects.all()
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()

    data={
        'page2data':page2data,
        'page3data':page3data,
        'page3hdata':page3hdata,
        'page4data':page4data,
        'page5hdata':page5hdata,
        'page5pdata':page5pdata,
        'page5idata':page5idata,
        'page7hdata':page7hdata,
        'page7imgdata':page7imgdata,
        'page7infodata':page7infodata,
        'pickupLocation':pickupLocation,
        'droplocation':droplocation
    }
    return render(request,"home2.html",data)

def page1(request):
    return render(request,"page1.html")

def page(request):
    return render(request,"page.html")

def popup1(request):
    return render(request,"pop-up.html")

def cars3(request):
    return render(request,"cars3.html")
def cars4(request):
    return render(request,"cars4.html")
def cars5(request):
    return render(request,"cars5.html")
def cars6(request):
    return render(request,"cars6.html")
def cars7(request):
    return render(request,"cars7.html")

def cars8(request):
    return render(request,"cars8.html")
def cars9(request):
    return render(request,"cars9.html")
def cars10(request):
    return render(request,"cars10.html")
def cars11(request):
    return render(request,"cars11.html")
def cars13(request):
    return render(request,"cars12.html")
def cars12(request):
    return render(request,"cars12.html")


razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def payment_page(request):
    # The amount should be in paisa (INR)
    amount = 50000  # e.g., 500.00 INR

    # Create Razorpay order
    razorpay_order = razorpay_client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
        'amount': amount,
        'currency': 'INR'
    }
    return render(request, 'payment_page.html', context)

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')

        # Verify payment signature
        try:
            razorpay_client.utility.verify_payment_signature({
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
            return JsonResponse({'status': 'Payment successful'})
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({'status': 'Payment verification failed'}, status=400)



# views.py
from django.shortcuts import render, redirect
from .forms import CarBookingForm

def booking_view(request):
    if request.method == 'POST':
        form = CarBookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('payments/payment_page.html')  # Redirect to a success page or another view
    else:
        form = CarBookingForm()
    return render(request, 'cars2.html')

# page for delhi to agra like data
def Tour(request):
    pickupLocation = PickupLocation.objects.all()
    droplocation=Droplocation.objects.all()
    return render(request,"Tour.html",{'pickupLocation':pickupLocation,'droplocation':droplocation})

def popular(request,drop_id):
    ob = Droplocation.objects.get(id=drop_id)
    return render(request,"popular.html",{'ob':ob})

def popularCity(request,drop_id):
    obj = Droplocation.objects.get(id=drop_id)
    return render(request,"PopularCitites.html",{'obj':obj})