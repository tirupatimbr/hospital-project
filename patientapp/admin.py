from django.contrib import admin
from . models import (Pharmacy,Patient,PrimaryInsurance,SecondaryInsurance,PatientPrescriber,
						OrderInfo,PatientAttachment,User,HighScore)

class UserAdmin(admin.ModelAdmin):
	list_display = ['id','username','password','phone_no','user_type']

class PharmacyAdmin(admin.ModelAdmin):
	list_display = ['id','pharmacy_name','email','phone','address_1','address_2','city','state','country','fax','pharmacy_id']

class PatientAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name','patient_id','address_1','address_2','zip_code','city','pharmacy']


class PrimaryInsuranceAdmin(admin.ModelAdmin):
	list_display = ['id','insurance_name','relation_to_patient','policy_holder_name','insurance_phone','policy',
					'group','patient']

class SecondaryInsuranceAdmin(admin.ModelAdmin):
	list_display = ['id','patient','insurance_name','relation_to_patient','policy_holder_name','insurance_phone','policy',
					'group']


class PatientPrescriberAdmin(admin.ModelAdmin):
	list_display = ['id','patient','req_fields']

class OrderInfoAdmin(admin.ModelAdmin):
	list_display = ['id','patient','date_written','date_received','need_by','quantity','days']

class PatientAttachmentAdmin(admin.ModelAdmin):
	list_display = ['id','patient','category','attachment','note']


admin.site.register(User,UserAdmin)
admin.site.register(Pharmacy,PharmacyAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(PrimaryInsurance,PrimaryInsuranceAdmin)
admin.site.register(SecondaryInsurance,SecondaryInsuranceAdmin)
admin.site.register(PatientPrescriber,PatientPrescriberAdmin)
admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(PatientAttachment,PatientAttachmentAdmin)

class HighScoreAdmin(admin.ModelAdmin):
	list_display = ['id','created','player_name','score']

admin.site.register(HighScore,HighScoreAdmin)

