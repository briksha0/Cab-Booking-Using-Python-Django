from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
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
        'page7infodata':page7infodata
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
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def travellers(request):
    return render(request,"travellers.html")

def reservation(request):
    return render(request,"reservation.html")

def cars2(request):
    return render(request,"cars2.html")

def carsform(request):
    return render(request,"cars2.html")

def directions(request,my_id):
    return render(request,"directions.html")

def direction2(request,my_id2):
    return render(request,"direction2.html")

def home2(request):
    return render(request,"home2.html")

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
