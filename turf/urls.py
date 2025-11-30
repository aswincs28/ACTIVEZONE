from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Booking & turf pages
    path("book_now", views.book_now, name="book_now"),
    path("turf_details", views.turf_details, name="turf_details"),
    path("slot_details", views.slot_details, name="slot_details"),

    # User authentication pages
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),

    # Static info pages
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),

    # Billing & history
    path("turfBilling", views.turfBilling, name="turfBilling"),
    path("orderHistory", views.orderHistory, name="orderHistory"),

    # Admin controls
    path("allBookings", views.allBookings, name="allBookings"),
    path("delete_booking/<int:id>", views.delete_booking, name="delete_booking"),

    # Razorpay success callback
    path("success", views.success, name="success"),
]
