from rest_framework import serializers
from . models import (Pharmacy,Patient,PrimaryInsurance,SecondaryInsurance,
						PatientPrescriber,OrderInfo,PatientAttachment,User,HighScore)



class UserSerializer(serializers.ModelSerializer):



	def validate_password(self,value):
		if value.isalnum():
			raise serializers.ValidationError('password must have atleast one special character.')   
		return value



	# def validate_username(self,value):
	# 	print(value,'vvvvv')		
	# 	if len(value) > 0: 
	# 		return value[0].upper() + value[1:]
	# 	else:
	# 		return ''

	def validate_username(self,value):
		print(value,'vvvvvvv')
		if len(value)>1:
			return value.capitalize()
		else:
			return ''	
		

	class Meta:
		model = User
		fields = '__all__'




class PharmacySerializer(serializers.ModelSerializer):
	class Meta:
		model = Pharmacy
		fields = '__all__'

class PrimaryInsuranceSerializer(serializers.ModelSerializer):

	class Meta:
		model = PrimaryInsurance
		fields = '__all__'
			

class PrimaryInsurance_Serializer(serializers.ModelSerializer):

	# patient = PatientSerializer()

	class Meta:
		model = PrimaryInsurance
		fields = '__all__'
		depth=5

class SecondaryInsuranceSerializer(serializers.ModelSerializer):
	class Meta:
		model = SecondaryInsurance
		fields = '__all__'  



class PatientSerializer(serializers.ModelSerializer):

	class Meta:
		model = Patient
		fields = '__all__'
		read_only_fields = ['address_2',"address_1"]
		


class Patient_Serializer(serializers.ModelSerializer):

	primary = PrimaryInsuranceSerializer(many=True)
	secondary = SecondaryInsuranceSerializer(many=True)
	

	class Meta:
		model = Patient
		fields = '__all__'
		depth = 2
		


class HighScoreSerializer(serializers.BaseSerializer):
  def to_representation(self,instance):
	  return ({'score':instance.score,'player_name':instance.player_name})



# class HighScoreSerializer(serializers.BaseSerializer):
# 	def to_internal_value(self, data):
# 		score = data.get('score')
# 		player_name = data.get('player_name')
# 		# team = data.get('team')

# 		if not score:
# 			raise serializers.ValidationError({'score': 'This field is required.'})

# 		if not player_name:
# 			raise serializers.ValidationError({'player_name': 'This field is required.'})

# 		if len(player_name) > 10:
# 			raise serializers.ValidationError({
# 				'player_name': 'May not be more than 10 characters.'
# 			})

# 		return {
#             'score': int(score),
#             'player_name': player_name
#         }
	   
# 	def to_representation(self,instance):
# 		return ({'score':instance.score,'player_name':instance.player_name})

	# def create(self, validated_data):
	# 	print(validated_data,"validated_data")
	# 	return HighScore.objects.create(**validated_data)   

