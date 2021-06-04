from django.db import models


from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
	phone_no = models.CharField(max_length=64,null=True,blank=True)
	user_type = models.CharField(max_length=64,null=True,blank=True)

	 # def create(self, request, *args, **kwargs):
		# serializer.password = make_password(serializer)
		# serializer.save()
		




class Pharmacy(models.Model):
	pharmacy_name = models.CharField(max_length=256, null=True, blank=True)
	email = models.EmailField(max_length=256, null=True, blank=True)
	phone = models.CharField(max_length=128, null=True, blank=True)
	address_1 = models.CharField(max_length=256, null=True, blank=True)
	address_2 = models.CharField(max_length=256, null=True, blank=True)
	city = models.CharField(max_length=128, null=True, blank=True)
	state = models.CharField(max_length=128, null=True, blank=True)
	country = models.CharField(max_length=128, null=True, blank=True)
	fax = models.CharField(max_length=128, null=True, blank=True)
	pharmacy_id = models.CharField(max_length=128, null=True, blank=True)
	
  
	# def __str__(self):
	# 	return self.pharmacy_name



class Patient(models.Model):
	first_name = models.CharField(max_length=128, null=True, blank=True)
	# mi = models.CharField(max_length=128, null=True, blank=True)
	last_name = models.CharField(max_length=128, null=True, blank=True)
	patient_id = models.BigIntegerField(null=True, blank=True, unique=True)
	address_1 = models.CharField(max_length=256)
	address_2 = models.CharField(max_length=256, null=True, blank=True)
	zip_code = models.CharField(max_length=128, null=True, blank=True)
	city = models.CharField(max_length=128, null=True, blank=True)
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.SET_NULL, null=True, blank=True)
  
	# state = models.CharField(max_length=128, null=True, blank=True)
	# primary_phone = models.CharField(max_length=128, null=True, blank=True)
	# home_phone = models.CharField(max_length=128, null=True, blank=True)
	# work_phone = models.CharField(max_length=128, null=True, blank=True)
	# ext = models.CharField(max_length=128, null=True, blank=True)
	# cell_phone = models.CharField(max_length=128, null=True, blank=True)
	# date_of_birth = models.DateField(null=True, blank=True)
	# ssn = models.CharField(max_length=128, null=True, blank=True)
	# best_time_to_call = models.CharField(max_length=256, null=True, blank=True)
	# email = models.EmailField(max_length=256, null=True, blank=True)
	# allow_call = models.BooleanField(default=True)
	# gender = models.CharField(max_length=128, null=True, blank=True)
	# mrn = models.CharField(max_length=128, null=True, blank=True)
	# primary_language = models.CharField(max_length=128, null=True, blank=True)
	# important_info = models.CharField(max_length=256, null=True, blank=True)
	# weight = models.CharField(max_length=128, null=True, blank=True)
	# weight_type = models.CharField(max_length=16, null=True, blank=True)
	# height = models.CharField(max_length=128, null=True, blank=True)
	# height_type = models.CharField(max_length=16, null=True, blank=True)
	# veterinary_use = models.BooleanField(default=False)
	# allergies = models.ManyToManyField(Allergy, blank=True)
	# concomitant_condition = models.ManyToManyField(Concomitant, blank=True)
	# additional_medications = models.ManyToManyField(Drug, blank=True)
	# req_fields = models.BooleanField(default=False)
	# all_fields = models.BooleanField(default=False)

	# prescriber = models.ForeignKey(Prescriber, on_delete=models.SET_NULL, null=True, blank=True)
	# bmi = models.CharField(max_length=128, null=True, blank=True)
	# pharmacy_insurance = models.ForeignKey(PharmacyPrimaryInsurance, on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
		return self.first_name

class PrimaryInsurance(models.Model):
	patient = models.ForeignKey(Patient,related_name='primary',on_delete=models.CASCADE, null=True, blank=True)
	# insurance_type = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True)
	insurance_name = models.CharField(max_length=256, null=True, blank=True)
	relation_to_patient = models.CharField(max_length=128, null=True, blank=True)
	policy_holder_name = models.CharField(max_length=256, null=True, blank=True)
	insurance_phone = models.CharField(max_length=256, null=True, blank=True)
	policy = models.CharField(max_length=256, null=True, blank=True)
	group = models.CharField(max_length=256, null=True, blank=True)
	# rx_bin = models.CharField(max_length=256, null=True, blank=True)
	# pcn = models.CharField(max_length=256, null=True, blank=True)
	# req_fields = models.BooleanField(default=False)

	def __str__(self):
		return self.insurance_name

class SecondaryInsurance(models.Model):
	patient = models.ForeignKey(Patient,related_name='secondary', on_delete=models.CASCADE, null=True, blank=True)
	# insurance_type = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True)
	insurance_name = models.CharField(max_length=256, null=True, blank=True)
	relation_to_patient = models.CharField(max_length=128, null=True, blank=True)
	policy_holder_name = models.CharField(max_length=256, null=True, blank=True)
	insurance_phone = models.CharField(max_length=256, null=True, blank=True)
	policy = models.CharField(max_length=256, null=True, blank=True)
	group = models.CharField(max_length=256, null=True, blank=True)
	# rx_bin = models.CharField(max_length=256, null=True, blank=True)
	# pcn = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		return self.insurance_name

class MedicalInsurance(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	policy_holder_name = models.CharField(max_length=256, null=True, blank=True)
	policy = models.CharField(max_length=256, null=True, blank=True)
	insurance_name = models.CharField(max_length=256, null=True, blank=True)
	insurance_phone = models.CharField(max_length=256, null=True, blank=True)
	group = models.CharField(max_length=256, null=True, blank=True)
	# req_fields = models.BooleanField(default=False)

class SecondaryMedicalInsurance(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	policy_holder_name = models.CharField(max_length=256, null=True, blank=True)
	policy = models.CharField(max_length=256, null=True, blank=True)
	insurance_name = models.CharField(max_length=256, null=True, blank=True)
	insurance_phone = models.CharField(max_length=256, null=True, blank=True)
	group = models.CharField(max_length=256, null=True, blank=True)

class PatientPrescriber(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	# prescriber = models.ForeignKey(Prescriber, on_delete=models.SET_NULL, null=True, blank=True)
	req_fields = models.BooleanField(default=False)

class PatientDiagnosis(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	# diagnosis = models.ManyToManyField(Diagnosis, blank=True)

class OrderInfo(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	# prescriber = models.ForeignKey(Prescriber, on_delete=models.CASCADE, null=True, blank=True)
	date_written = models.DateField(null=True, blank=True)
	date_received = models.DateField(null=True, blank=True)
	need_by = models.DateField(null=True, blank=True)
	# rx_origin = models.CharField(max_length=256, null=True, blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	days = models.IntegerField(null=True, blank=True)
	# drug = models.ForeignKey(Drug, on_delete=models.CASCADE, null=True, blank=True)
	# sig = models.CharField(max_length=256, null=True, blank=True)
	
	# refill = models.IntegerField(null=True, blank=True)
	# fill = models.IntegerField(null=True, blank=True)
	# rx = models.CharField(max_length=256, null=True, blank=True)
	# wac = models.CharField(max_length=256, null=True, blank=True)
	# init_value = models.CharField(max_length=256, null=True, blank=True)
	# refill_value = models.CharField(max_length=256, null=True, blank=True)
	# daw = models.CharField(max_length=256, null=True, blank=True)
	# rx_serial = models.CharField(max_length=256, null=True, blank=True)
	# req_fields = models.BooleanField(default=False)

class PatientAttachment(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	category = models.CharField(max_length=256, null=True, blank=True)
	attachment = models.FileField(upload_to='attachments',null=True, blank=True)
	note = models.TextField(null=True, blank=True)


class HighScore(models.Model):
	created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
	player_name = models.CharField(max_length=50,null=True, blank=True)  
	score = models.CharField(max_length=50,null=True, blank=True) 


