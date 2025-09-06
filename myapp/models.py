from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class page2(models.Model):
    Page2_Heading = models.CharField(max_length=20)
    Page2_paragraph = models.TextField()
    image1 = models.ImageField(default='', upload_to="")
    image2 = models.ImageField(default='', upload_to="")


class page3(models.Model):
    Page3_span = models.CharField(max_length=50)
    Page3_paragraph = models.TextField()


class page4(models.Model):
    Page4_Heading = models.CharField(max_length=20)
    Page4_paragraph = models.TextField()
    image = models.ImageField(upload_to="images")

class PAGE3HEADING(models.Model):
    Page3_Heading = models.CharField(max_length=50)
    

class PAGE5HEADING(models.Model):
    Page5_Heading = models.CharField(max_length=50)



class PAGE5_PARA(models.Model):
    Page5_paragraph = models.TextField()

class PAGE5_IMG(models.Model):
    image = models.ImageField(default='', upload_to="")

class PAGE7HEADING(models.Model):
    Page7_Heading = models.CharField(max_length=50)

class page7img(models.Model):
    Page7_Img = models.ImageField()

class page7info(models.Model):
    Page7_Para = models.TextField()
    Page7_Name = models.CharField(max_length=50)
    
class cabEnquiry(models.Model):
    pickup=models.CharField(max_length=150)
    drop=models.CharField(max_length=150)
    phone=models.IntegerField()


class CarBooking(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    pickup = models.CharField(max_length=255)
    trip = models.CharField(max_length=50)
    departure = models.DateField()
    arrival = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.trip}"


class Carstype(models.Model):
    car_img = models.ImageField(upload_to='cartype',blank=True,null=True)
    car_type = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    price = models.FloatField()
    included_km = models.FloatField()
    toll_tax = models.CharField(max_length=100,default="Extra")
    extra_Fare = models.FloatField()
    fuel_prc = models.CharField(max_length=100)
    driver_prc = models.CharField(max_length=100)
    night_prc = models.CharField(max_length=100)


class Tempo(models.Model):
    car_img = models.ImageField(upload_to='cartype',default=0)
    Tempo_name = models.CharField(max_length=100)
    seat = models.CharField(max_length=200)
    price = models.FloatField()
    toll_tax = models.CharField(max_length=100,default=0)
    extra_Fare = models.FloatField()
    fuel_prc = models.CharField(max_length=100)
    driver_prc = models.CharField(max_length=100)
    night_prc = models.CharField(max_length=100)

class BookingCab(models.Model):
    is_paid = models.BooleanField(default=False,null=True,blank=True)
    booking_id=models.CharField(max_length=10,default=0)
    username = models.CharField(max_length=100,)
    email = models.EmailField(max_length=200,default=0)
    phone = models.IntegerField(default=0)
    pick_up_location = models.CharField(max_length=100,null=True,blank=True)
    drop_location = models.CharField(max_length=100,null=True,blank=True)
    pick_up_time = models.CharField(max_length=100,null=True,blank=True)
    total_price=models.CharField(max_length=100,null=True,blank=True)
    advance_payment=models.CharField(max_length=100,null=True,blank=True)
    amount_to_pay=models.IntegerField(null=True,blank=True,default=0)
    way=models.CharField(max_length=100,choices=(('One','One'),('Two','Two')),default='One')
    cab=models.CharField(max_length=100,blank=True,null=True)
    pick_up_date = models.DateField(null=True,blank=True,auto_now_add=True)
    departure_date=models.CharField(max_length=100,blank=True,null=True)
    arrival_date=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f"{self.username} - {self.phone}"



class Payment(models.Model):
    order_id = models.CharField(max_length=255, unique=True)
    payment_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone=models.CharField(max_length=11)
    pickup=models.CharField(max_length=100)
    drop=models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    bookcap=models.ForeignKey(BookingCab,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
class TermsAndConditions(models.Model):
    con=RichTextField()

class PickupLocation(models.Model):
    pickup=models.CharField(max_length=100)
    def __str__(self):
        return self.pickup

class Droplocation(models.Model):
    c=models.ForeignKey(PickupLocation,on_delete=models.CASCADE)
    drop=models.CharField(max_length=100)
    drop_loc_info = RichTextField()
    img = models.ImageField(default=True,null=True)
    place_visit = RichTextField(blank=True,null=True)
    Key_Travel_Details = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.drop

class ContactUsFormData(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    email = models.CharField(blank=True,null=True,max_length=100)
    message = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

class ReservationFormData(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    email = models.CharField(blank=True,null=True,max_length=100)
    message = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name