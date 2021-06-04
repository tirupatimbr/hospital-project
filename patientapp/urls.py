# from django.urls import path
# from patientapp import views

# urlpatterns = [

# 	path('api/',views.api),
#     # path('list_Pharmacy/',views.list_Pharmacy),
#     # path('Pharmacy_details/<int:pk>/',views.Pharmacy_details),
#     # path('Pharmacy_create/',views.Pharmacy_create),
#     # path('Pharmacy_update/<int:pk>/',views.Pharmacy_update),

#     path('Pharmacy_details/',views.Pharmacy_details),

# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from patientapp import views



urlpatterns = [



	path('user_registration/',views.user_registration.as_view()),
	path('user_details/<int:pk>/',views.user_details.as_view()),

	path('userlogin/',views.userlogin),

    path('PharmacyList/', views.PharmacyList.as_view()),
    path('Pharmacy_details/<int:pk>/',views.Pharmacy_details.as_view()),

    path('PatientList/',views.PatientList.as_view()),
    path('Patient_Details/<int:pk>/',views.Patient_Details.as_view()),

    path('PrimaryInsuranceList/',views.PrimaryInsuranceList.as_view()),
    path('PrimaryInsurance_Details/<int:pk>/',views.PrimaryInsurance_Details.as_view()),

    # path('high_score/<int:pk>/',views.high_score),
    path('all_high_score/',views.all_high_score),


]

