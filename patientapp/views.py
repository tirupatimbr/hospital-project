from django.shortcuts import render
from . models import (Pharmacy,Patient,PrimaryInsurance,SecondaryInsurance,PatientPrescriber,
                        OrderInfo,PatientAttachment,User,HighScore)

from . serializers import (PharmacySerializer,
                           PatientSerializer,Patient_Serializer,
                           PrimaryInsuranceSerializer,PrimaryInsurance_Serializer,
                           UserSerializer,HighScoreSerializer
                            )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import Http404
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.authtoken.models import Token

from rest_framework import permissions




from patientapp.schema import (CustomLoginSchema,PharmaLoginSchema,
                                PatientLoginSchema,PrimaryLoginSchema,UserLoginSchema,login_schema)

from rest_framework.decorators import api_view, renderer_classes,schema,permission_classes

# from django.db.models.signals import post_save

@api_view(['GET'])
def api(request):
    return JsonResponse('API View',safe=False)



# @api_view(['GET'])
# def list_Pharmacy(request):
#   qs = Pharmacy.objects.all()
#   serializers = PharmacySerializer(qs,many=True)
#   return JsonResponse(serializers.data,safe=False)


# @api_view(['GET'])
# def Pharmacy_details(request,pk):
#   qs = Pharmacy.objects.get(id=pk)
#   serializers = PharmacySerializer(qs,many=False)
#   return JsonResponse(serializers.data,safe=False)



# @api_view(['GET'])
# def Pharmacy_create(request):
#   qs = Pharmacy.objects.all()
#   serializer = PharmacySerializer(data=request.data)
#   if serializer.is_valid():
#       serializer.save()
#   return JsonResponse(serializer.data,safe=False)



# @api_view(['PUT'])
# def Pharmacy_update(request,pk):
#   qs = Pharmacy.objects.get(id=pk)
#   serializer = PharmacySerializer(instance=qs,data=request.data)
#   if serializer.is_valid():
#       serializer.save()
#   return JsonResponse(serializer.data,safe=False)


class user_registration(APIView):

    """
    user registration

    """

    schema = CustomLoginSchema()

    def get(self,request,format=None):
        qs = User.objects.all()
        serializer = UserSerializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)

        # if User.objects.filter(username=username).exists():
        #     return Response('username already exists')


        password = request.data.get('password')

        if serializer.is_valid():
            
             
            data = serializer.save()
            data.password = make_password(password)
            data.is_active = True   
            data.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)       





class user_details(APIView):

    """
     user_details by id

    """

    schema = CustomLoginSchema()

    def get_object(self,pk):
        try:
            return User.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request, pk,format=None):
        qs = self.get_object(pk)
        serializer = UserSerializer(qs)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def put(self,request, pk,format=None):
        qs=self.get_object(pk)
        serializer = UserSerializer(qs,data=request.data)
        password = request.data.get('password')

        if serializer.is_valid():
            serializer.save()
            data = serializer.save()
            data.password = make_password(password)
            data.is_active = True

            
            data.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            



        



def authenticate(username=None,password=None):
    user = User.objects.get(username=username)
    print(user,'aaaaaaaaaaaaa') 
    return user.check_password(password)

# @schema(UserLoginSchema)

@api_view(['POST'])
@schema(login_schema)
def userlogin(request):
    if request.method == 'POST':

        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user_ins = User.objects.get(username=username)
            print(user_ins,'uuuuuuuuuuu')
        except:
            return JsonResponse({'success':False,'data':'admin or students not registered'})

        user = authenticate(username=username, password=password)
        print(user,'user')
        if user:

            token_qs,created = Token.objects.get_or_create(user_id=user_ins.id)
            user_qs = list(User.objects.filter(username=username).values())

            return Response([{'data': user_qs,"key":token_qs.key}], status=status.HTTP_200_OK)
        else:
            return Response([{"key":"Please provide valid credentials"}],status=status.HTTP_400_BAD_REQUEST)













class PharmacyList(APIView):

    """
    PharmacyList

    """

    schema = PharmaLoginSchema()

    def get(self,request,format=None):
        qs = Pharmacy.objects.all()
        serializers = PharmacySerializer(qs,many=True)
        return JsonResponse({'Success':True,'data':serializers.data})


    schema = PharmaLoginSchema()    
    def post(self,request,format=None):
        email = request.data.get('email')


        serializer = PharmacySerializer(data=request.data)
  

        # if Pharmacy.objects.filter(email=email).exists():
        #     return Response('email already exists')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Pharmacy_details(APIView):

    """
    Pharmacy_details by id
    
    """

    schema = PharmaLoginSchema()

    def get_object(self,pk):
        try:
            return Pharmacy.objects.get(id=pk)
        except:
            raise Http404
                        

    def get(self,request,pk,format=None):
        qs = self.get_object(pk)
        serializer = PharmacySerializer(qs)
        return Response(serializer.data)        

    def put(self,request,pk,format=None):
        qs = self.get_object(pk)
        serializer = PharmacySerializer(qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        qs = self.get_object(pk)
        qs.delete()
        return Response('phrmacy {} data deleted'.format(pk),status=status.HTTP_204_NO_CONTENT)


#******************************************************************
# from rest_framework.permissions import BasePermission


class BlocklistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.user_type =="admin")


# @schema('PatientLoginSchema')
class PatientList(APIView):
    # permission_classes = [BlocklistPermission]  

    
    schema = PatientLoginSchema()   
    def get(self,request,format=None):
        
        # if request.user.is_anonymous:
        #   return Response({'success':False,'data':'you have to give token'})

        # permission_classes = [BlocklistPermission,]   
    
        qs = Patient.objects.all()
        serializer = PatientSerializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    # @schema(PatientLoginSchema)
    def post(self,request,format=None):

        # if request.user.is_anonymous:
        #   return Response({'success':False,'data':'you have to give token'})

        # permission_classes = [BlocklistPermission]    

        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Patient_Details(APIView):

    # permission_classes = [BlocklistPermission,]

    schema = PatientLoginSchema()  
    def get_object(self,pk):
        try:
            return Patient.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        # if request.user.is_anonymous:
        #   return Response({'success':False,'data':'you have to give token'})

        # permission_classes = [BlocklistPermission]

        qs = self.get_object(pk)
        serializer = Patient_Serializer(qs)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,pk,format=None):

        # if request.user.is_anonymous:
        #   return Response({'success':False,'data':'you have to give token'})

        # permission_classes = [BlocklistPermission]


        qs = self.get_object(pk)
        serializer = Patient_Serializer(qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self,request,pk,format=None):
        qs = self.get_object(pk)
        qs.delete()
        return Response('patient {} data deleted'.format(pk),status=status.HTTP_204_NO_CONTENT)

    
#**************************************************



# class BlocklistPermission(permissions.BasePermission):
#   def has_permission(self, request, view):
#       print("hello")
#       return (request.user.user_type == 'admin')

@schema(PrimaryLoginSchema)
class PrimaryInsuranceList(APIView):

    # permission_classes = [BlocklistPermission]

    # schema = PrimaryLoginSchema()
    def get(self,request,format=None):

        # primary_id = request.GET.get('primary_id')

        # if primary_id:
        #   qs = PrimaryInsurance.objects.filter(id = primary_id ).values()
        #   serializer = PrimaryInsurance_Serializer(qs,many=True)

        #   return Response(serializer.data,status = status.HTTP_201_CREATED)

        qs = PrimaryInsurance.objects.all()
        serializer = PrimaryInsuranceSerializer(qs,many=True)

        return Response(serializer.data,status = status.HTTP_201_CREATED)

    def post(self,request,format=None):
        
        serializer = PrimaryInsuranceSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)

@schema(PrimaryLoginSchema)
class PrimaryInsurance_Details(APIView):
    # permission_classes = [BlocklistPermission]

    # schema = PrimaryLoginSchema()
    def get_object(self,pk):
        try:
            return PrimaryInsurance.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        qs = self.get_object(pk)
        serializer = PrimaryInsurance_Serializer(qs)
        return Response(serializer.data,status = status.HTTP_201_CREATED)
        
    def put(self,request,pk,format=None):
        qs = self.get_object(pk)
        serializer = PrimaryInsurance_Serializer(qs,data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        qs = self.get_object(pk)
        qs.delete()
        return Response('data deleted succesfully') 







# @api_view(['GET'])
# def high_score(request,pk):
#   instance = HighScore.objects.get(pk=pk)
#   serializer = HighScoreSerializer(instance)
#   return Response(serializer.data)


@api_view(['GET'])
def all_high_score(request):
    qs = HighScore.objects.order_by('-score')
    serializer = HighScoreSerializer(qs,many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def all_high_score(request):
#   serializer = HighScoreSerializer(data=request.data)
#   if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status = status.HTTP_201_CREATED)
#   return Response(serializer.errors)













# class PatientList(APIView):
    
#   def get(self,request,format=None):


#       qs = Patient.objects.all()
#       serializer = Patient_Serializer(qs,many=True)
#       return Response(serializer.data,status=status.HTTP_201_CREATED)

#   def post(self,request,format=None):

#       serializer = PatientSerializer(data=request.data)
#       if serializer.is_valid():
#           serializer.save()   
#           return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Patient_Details(APIView):

#   def get_object(self,pk):
#       try:
#           return Patient.objects.get(id=pk)
#       except:
#           raise Http404

#   def get(self,request,pk,format=None):
#       qs = self.get_object(pk)
#       serializer = Patient_Serializer(qs)
#       return Response(serializer.data,status=status.HTTP_201_CREATED)

#   def put(self,request,pk,format=None):
#       qs = self.get_object(pk)
#       serializer = PatientSerializer(qs,data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
#   def delete(self,request,pk,format=None):
#       qs = self.get_object(pk)
#       qs.delete()
#       return Response('patient {} data deleted'.format(pk),status=status.HTTP_204_NO_CONTENT)





# class UserLogin(APIView):

#     def authenticate(self,username=None,password=None):
#         user = User.objects.get(username=username)
#         print(user,'aaaaaaaaaaaaa') 
#         return user.check_password(password)



#     def post(self, request, format=None):
#             username = request.data.get("username")
#             password = request.data.get("password")

#             try:
#                 user_ins = User.objects.get(username=username)
#                 print(user_ins,'uuuuuuuuuuu')
#             except:
#                 return JsonResponse({'success':False,'data':'admin or students not registered'})

#             user = self.authenticate(username=username, password=password)
#             print(user,'user')
#             if user:

#                 token_qs,created = Token.objects.get_or_create(user_id=user_ins.id)
#                 user_qs = list(User.objects.filter(username=username).values())

#                 return Response([{'data': user_qs,"key":token_qs.key}], status=status.HTTP_200_OK)
#             else:
#                 return Response([{"key":"Please provide valid credentials"}],status=status.HTTP_400_BAD_REQUEST)
 
































