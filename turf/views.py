
from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
import math
from datetime import date, datetime, timedelta
from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from pytz import timezone
import time
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

def index(request):

    # days=[
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    # matrix = bookslot(week = days)
    # matrix.save()
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'mainpage_index.html', {'username':username})
    return render(request, 'mainpage_index.html')


def book_now(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'booking_index.html', {'username':username})
    return render(request, 'booking_index.html')


def turf_details(request):
    currentDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
    return render(request, 'turfblog.html', {'currentDate': currentDate, 'endDate': endDate})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('book_now')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'signIn.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already Taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signUp.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def contactus(request):
    if request.method == "POST":
        # Handle the form submission here (save data or send email)
        return render(request, "thankyou.html")  # Show thank-you page after POST

    # For GET requests, just show the contact form
    return render(request, "contactUs.html")


def aboutus(request):
    return render(request, 'aboutus.html')
 


update = {"1"}

@login_required(login_url='login')
def slot_details(request):
    if request.method == 'POST':
        selectedDate = request.POST['selectedDate']
    slots = turfBooking.objects.all()
    
    days=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    matrix = bookslot(week = days)
    matrix.save()
    print(matrix.week)
    
    # matrix = bookslot.objects.get(id='1')
    # print("Matrix Before")
    # print(matrix.week)

    choosenDay = datetime.strptime(selectedDate, "%Y-%m-%d").strftime("%A")
    curentTime = datetime.now().strftime("%H:%M:%S")

    tomorrowDate = (datetime.now() + timedelta(days=1)
                    ).strftime("%Y-%m-%d")
    currentDate = datetime.now().strftime("%Y-%m-%d")
    # currentDate = tomorrowDate
    update.add(tomorrowDate)
    
    print("Array = ", update)
    for j in update.copy():
        if(currentDate == str(j)):
            dayTobeDeleated = (
                datetime.now() - timedelta(days=1)).strftime("%A")
            # dayTobeDeleated = "Wednesday"
            update.remove(currentDate)
            print(update)
            print("Day to be deleated: ", dayTobeDeleated)
            if dayTobeDeleated == "Monday":
                for i in range(1, 20):
                    matrix.week[0][i] = 0
            elif dayTobeDeleated == "Tuesday":
                for i in range(1, 20):
                    matrix.week[1][i] = 0
            elif dayTobeDeleated == "Wednesday":
                for i in range(1, 20):
                    matrix.week[2][i] = 0
            elif dayTobeDeleated == "Thursday":
                for i in range(1, 20):
                    matrix.week[3][i] = 0
            elif dayTobeDeleated == "Friday":
                for i in range(1, 20):
                    matrix.week[4][i] = 0
            elif dayTobeDeleated == "Saturday":
                for i in range(1, 20):
                    matrix.week[5][i] = 0
            elif dayTobeDeleated == "Sunday":
                for i in range(1, 20):
                    matrix.week[6][i] = 0

    ls = []
    if choosenDay == "Monday":
        for j in range(20):
            ls.append(str(matrix.week[0][j]))
    elif choosenDay == "Tuesday":
        for j in range(20):
            ls.append(str(matrix.week[1][j]))
    elif choosenDay == "Wednesday":
        for j in range(20):
            ls.append(str(matrix.week[2][j]))
    elif choosenDay == "Thursday":
        for j in range(20):
            ls.append(str(matrix.week[3][j]))
    elif choosenDay == "Friday":
        for j in range(20):
            ls.append(str(matrix.week[4][j]))
    elif choosenDay == "Saturday":
        for j in range(20):
            ls.append(str(matrix.week[5][j]))
    elif choosenDay == "Sunday":
        for j in range(20):
            ls.append(str(matrix.week[6][j]))

    print("Matrix After")
    print(matrix.week)
    return render(request, 'turfBooking.html', {'currentDate': currentDate, 'selectedDate': selectedDate,  'list': ls})


def turfDateSelection(request):

    if request.method == 'POST':
        selectedDate = request.POST['selectedDate']
        request.session['choosenDate'] = selectedDate
        return redirect('turf_bookings')
    else:
        currentDate = date.today().strftime("%Y-%m-%d")
        # print(currentDate)
        endDate = (date.today() + timedelta(days=6)).strftime("%Y-%m-%d")
        return render(request, 'turfDateSelection.html', {'currentDate': currentDate, 'endDate': endDate})


def turfBilling(request):
    if request.method == 'POST':
        currentDate = date.today().strftime("%Y-%m-%d")
        selectedDate = request.POST['date']
        list_of_input_ids = request.POST.getlist('id')
        
        # If no time selected → go to error page
        if not list_of_input_ids:
            return render(request, 'error.html', {
                'msg': 'Please select at least one time slot.'
            })

        print(list_of_input_ids)

        selectedTime = []
        # checkingTime = []
        bookedSlots = []
        for i in list_of_input_ids:
            if i == '1':
                bookedSlots.append('6-7 am')
                selectedTime.append('06:00:00')
            elif i == '2':
                bookedSlots.append('7-8 am')
                selectedTime.append('07:00:00')
            elif i == '3':
                bookedSlots.append('8-9 am')
                selectedTime.append('08:00:00')
            elif i == '4':
                bookedSlots.append('9-10 am')
                selectedTime.append('09:00:00')
            elif i == '5':
                bookedSlots.append('10-11 am')
                selectedTime.append('10:00:00')
            elif i == '6':
                bookedSlots.append('11-12 am')
                selectedTime.append('11:00:00')
            elif i == '7':
                bookedSlots.append('12-1 pm')
                selectedTime.append('12:00:00')
            elif i == '8':
                bookedSlots.append('1-2 pm')
                selectedTime.append('13:00:00')
            elif i == '9':
                bookedSlots.append('2-3 pm')
                selectedTime.append('14:00:00')
            elif i == '10':
                bookedSlots.append('3-4 pm')
                selectedTime.append('15:00:00')
            elif i == '11':
                bookedSlots.append('4-5 pm')
                selectedTime.append('16:00:00')
            elif i == '12':
                bookedSlots.append('5-6 pm')
                selectedTime.append('17:00:00')
            elif i == '13':
                bookedSlots.append('6-7 pm')
                selectedTime.append('18:00:00')
            elif i == '14':
                bookedSlots.append('7-8 pm')
                selectedTime.append('19:00:00')
            elif i == '15':
                bookedSlots.append('8-9 pm')
                selectedTime.append('20:00:00')
            elif i == '16':
                bookedSlots.append('9-10 pm')
                selectedTime.append('21:00:00')
            elif i == '17':
                bookedSlots.append('10-11 pm')
                selectedTime.append('22:00:00')
            elif i == '18':
                bookedSlots.append('11-12 pm')
                selectedTime.append('23:00:00')
            elif i == '19':
                bookedSlots.append('12-1 am')
                selectedTime.append(':00:00')

        print("BookedSlots :")
        print(bookedSlots)
        totalAmount = len(bookedSlots) * 700

        details = {
            'username': request.user.username,
            'email': request.user.email,
            'selectedDate': selectedDate,
            'currentDate': currentDate,
            'bookedSlots': bookedSlots,
            'totalAmount': totalAmount,
            'list_of_input_ids': list_of_input_ids
        }
        print("Turf Billing")
        print("Matrix in Billing")
        
        booking_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')
        keyId = 'rzp_test_9e8xrjzBFp5O7M'
        keySecret = 's4qIuVEiSi128ucHK9uAzoAU'

        client = razorpay.Client(auth=(keyId, keySecret))

        DATA = {
            # Amount will be in its smallest unit, that is Paisa (Therefore multiplying by 100 to convert amount in Rs to Paisa)
            "amount": int(totalAmount)* 100,
            "currency": "INR",
            "receipt": 'ACTIVEZONE',
            'notes': {
                'Name': request.user.username,
                'Payment_For': 'Turf Booking'
            },
            'payment_capture': '1'
        }

        payment = client.order.create(data=DATA)
        print(payment)
        turf = TurfBooked(name=request.user.username, email=request.user.email,
                           amount=totalAmount, selected_date=selectedDate,current_date=currentDate, booking_time=booking_time,slots=bookedSlots, payment_id=payment['id'])
        turf.save()
        return render(request, 'turfBilling.html', {'payment': payment, 'details': details})
    # return render(request, 'turfBilling.html', {'details': details})

@csrf_exempt
def success(request):
    if request.method == "POST":
        paymentDetails = request.POST   # Dictionary
        # {
        #     "razorpay_payment_id": "pay_29QQoUBi66xm2f",
        #     "razorpay_order_id": "order_9A33XWu170gUtm",
        #     "razorpay_signature": "9ef4dffbfd84f1318f6739a3ce19f9d85851857ae648f114332d8401e0949a3d"
        # }

        # Verify the Signature

        keyId = 'rzp_test_9e8xrjzBFp5O7M'
        keySecret = 's4qIuVEiSi128ucHK9uAzoAU'
        client = razorpay.Client(auth=(keyId, keySecret))
        params_dict = {
            'razorpay_order_id': paymentDetails['razorpay_order_id'],
            'razorpay_payment_id': paymentDetails['razorpay_payment_id'],
            'razorpay_signature': paymentDetails['razorpay_signature']
        }
        # If returns None, payment is successful, else some error occured
        check = client.utility.verify_payment_signature(params_dict)
        

        if check:
            print(check)
            order_id = paymentDetails['razorpay_order_id']
            user = TurfBooked.objects.filter(payment_id=order_id).first()
            print(user)
            user.paid = True
            user.save()
            return render(request, 'success.html')
        

        # If Payment is successfull done, the checkbox(Paid) is ticked in database of that user



        total_amount = request.POST.get('total_amount')
        username = request.POST.get('username')
        email = request.POST.get('email')
        selected_date = request.POST.get('selected_date')
        current_date = request.POST.get('current_date')
        slots = request.POST.getlist('slots')
        print(slots)
        booking_time = datetime.now(
            timezone("Asia/Kolkata")).strftime('%H:%M:%S')
        
        
        message_plain = render_to_string('email.txt')
        message_html = render_to_string('email.html', {'amount': user.amount})

        send_mail(
            'Turf Booking Successful',
            message_plain,
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=message_html
        )

    return render(request, 'success.html')


def deleteRecord(dayTobeDeleated):
    matrix = bookslot.objects.get(id='1')
    if dayTobeDeleated == "Monday":
        for i in range(20):
            matrix.week[0][i] = 0
    elif dayTobeDeleated == "Tuesday":
        for i in range(20):
            matrix.week[1][i] = 0
    elif dayTobeDeleated == "Wednesday":
        for i in range(20):
            matrix.week[2][i] = 0
    elif dayTobeDeleated == "Thursday":
        for i in range(20):
            matrix.week[3][i] = 0
    elif dayTobeDeleated == "Friday":
        for i in range(20):
            matrix.week[4][i] = 0
    elif dayTobeDeleated == "Saturday":
        for i in range(20):
            matrix.week[5][i] = 0
    elif dayTobeDeleated == "Sunday":
        for i in range(20):
            matrix.week[6][i] = 0



        


@login_required(login_url='login')
def orderHistory(request):

    # bookings = TurfBooked.objects.filter(paid=True)
    my_bookings = TurfBooked.objects.filter(paid=True).filter(email=request.user.email)

    currentDate = date.today().strftime("%Y-%m-%d")
    # currentDate = '2021-08-18'
    return render(request, 'orderHistory.html', {'bookings': my_bookings, 'currentDate': currentDate})


def delete_booking(request, id):

    if request.method == 'POST':

        booking = TurfBooked.objects.get(id=id)
        selectedDate = booking.selected_date
        slots = booking.slots

        bookedSlots = []
        for i in slots:
            if i == '6-7 am':
                bookedSlots.append(1)
            elif i == '7-8 am':
                bookedSlots.append(2)
            elif i == '8-9 am':
                bookedSlots.append(3)
            elif i == '9-10 am':
                bookedSlots.append(4)
            elif i == '10-11 am':
                bookedSlots.append(5)
            elif i == '11-12 am':
                bookedSlots.append(6)
            elif i == '12-1 pm':
                bookedSlots.append(7)
            elif i == '1-2 pm':
                bookedSlots.append(8)
            elif i == '2-3 pm':
                bookedSlots.append(9)
            elif i == '3-4 pm':
                bookedSlots.append(10)
            elif i == '4-5 pm':
                bookedSlots.append(11)
            elif i == '5-6 pm':
                bookedSlots.append(12)
            elif i == '6-7 pm':
                bookedSlots.append(13)
            elif i == '7-8 pm':
                bookedSlots.append(14)
            elif i == '8-9 pm':
                bookedSlots.append(15)
            elif i == '9-10 pm':
                bookedSlots.append(16)
            elif i == '10-11 pm':
                bookedSlots.append(17)
            elif i == '11-12 pm':
                bookedSlots.append(18)
            elif i == '12-1 am':
                bookedSlots.append(19)

        choosenDay = datetime.strptime(selectedDate, "%Y-%m-%d").strftime("%A")
        print(choosenDay)
        matrix = bookslot.objects.get(id='1')
        if choosenDay == "Monday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[0][i] = 0
                        matrix.save()
        elif choosenDay == "Tuesday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[1][i] = 0
                        matrix.save()
        elif choosenDay == "Wednesday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[2][i] = 0
                        matrix.save()
        elif choosenDay == "Thursday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[3][i] = 0
                        matrix.save()
        elif choosenDay == "Friday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[4][i] = 0
                        matrix.save()
        elif choosenDay == "Saturday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[5][i] = 0
                        matrix.save()
        elif choosenDay == "Sunday":
            for i in bookedSlots:
                for j in range(1, 20):
                    if(i == j):
                        matrix.week[6][i] = 0
                        matrix.save()

        TurfBooked.objects.filter(id=id).delete()

        return redirect('index')


def allBookings(request):
    datesInSortedOrder = []
    bookings = TurfBooked.objects.filter(paid = True).order_by('selected_date', 'booking_time')
    currentDate = date.today().strftime("%Y-%m-%d")
    # currentDate = '2021-08-19'
    return render(request, 'allBookings.html', {'bookings': bookings, 'dates': datesInSortedOrder, 'currentDate': currentDate})


def searchBooking(request):

    query = request.POST['query']
    print(query)
    bookings = TurfBooked.objects.filter(name__icontains=query)
    print(bookings)
    return render(request, 'allBookings.html', {'bookings': bookings, 'query': query})
    # return HttpResponse('This is search')
