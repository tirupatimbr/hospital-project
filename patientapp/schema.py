from rest_framework.schemas import AutoSchema,ManualSchema
import coreapi,coreschema


class CustomLoginSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        if method.lower() in ['post','put']:
            extra_fields = [
                coreapi.Field('username', required=True,location="formData",type="string"),
                coreapi.Field('password',required=True,location="formData", type="string"),
                coreapi.Field('phone_no', required=True,location="formData",type="string"),
                coreapi.Field('user_type',required=True,location="formData", type="string")]   
                   
        else:
            extra_fields = []
        serializer_fields = super().get_serializer_fields(path, method)
        return serializer_fields + extra_fields

class UserLoginSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        if method.lower() in ['get','post','put']:
            extra_fields = [
                coreapi.Field('username', required=True,location="formData",type="string"),
                coreapi.Field('password',required=True,location="formData", type="string"),]
              
        else:
            extra_fields = []
        serializer_fields = super().get_serializer_fields(path, method)
        return serializer_fields + extra_fields

class PharmaLoginSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        if method.lower() in ['post','put']:

            extra_fields = [
                coreapi.Field('pharmacy_name', required=True,location="formData",type="string"),
                coreapi.Field('email',required=True,location="formData", type="string"),
                coreapi.Field('phone', required=True,location="formData",type="string"),
                coreapi.Field('address_1',required=True,location="formData", type="string"),
                coreapi.Field('address_2', required=True,location="formData",type="string"),
                coreapi.Field('city',required=True,location="formData", type="string"),
                coreapi.Field('state', required=True,location="formData",type="string"),
                coreapi.Field('country',required=True,location="formData", type="string"),
                coreapi.Field('fax', required=True,location="formData",type="string"),
                coreapi.Field('pharmacy_id',required=True,location="formData", type="string")]                             
        else:
            extra_fields = []
        serializer_fields = super().get_serializer_fields(path, method)
        return serializer_fields + extra_fields

class PatientLoginSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        if method.lower() in ['post','put']:
            extra_fields = [
                coreapi.Field('first_name', required=True,location="formData",type="string"),
                coreapi.Field('last_name',required=True,location="formData", type="string"),
                coreapi.Field('patient_id', required=True,location="formData",type="string"),
                coreapi.Field('address_1',required=True,location="formData", type="string"),
                coreapi.Field('address_2', required=True,location="formData",type="string"),
                coreapi.Field('zip_code',required=True,location="formData", type="string"),
                coreapi.Field('city', required=True,location="formData",type="string"),
                coreapi.Field('pharmacy',required=True,location="formData", type="string"),
                ]                             
        else:
            extra_fields = []
        serializer_fields = super().get_serializer_fields(path, method)
        return serializer_fields + extra_fields


# class PrimaryLoginSchema(AutoSchema):

#     def get_serializer_fields(self, path, method):
#         if method.lower() in ['post','put']:
#             extra_fields = [
#                 coreapi.Field('insurance_name', required=True,location="formData",type="string"),
#                 coreapi.Field('relation_to_patient',required=True,location="formData", type="string"),
#                 coreapi.Field('policy_holder_name', required=True,location="formData",type="string"),
#                 coreapi.Field('insurance_phone',required=True,location="formData", type="string"),
#                 coreapi.Field('policy', required=True,location="formData",type="string"),
#                 coreapi.Field('group',required=True,location="formData", type="string"),
#                 coreapi.Field('patient', required=True,location="formData",type="string"),
#                 ]                             
#         else:
#             extra_fields = []
#         serializer_fields = super().get_serializer_fields(path, method)
#         return serializer_fields + extra_fields


PrimaryLoginSchema = AutoSchema(manual_fields=[
                coreapi.Field('insurance_name', required=True,location="formData",type="string"),
                coreapi.Field('relation_to_patient',required=True,location="formData", type="string"),
                coreapi.Field('policy_holder_name', required=True,location="formData",type="string"),
                coreapi.Field('insurance_phone',required=True,location="formData", type="string"),
                coreapi.Field('policy', required=True,location="formData",type="string"),
                coreapi.Field('group',required=True,location="formData", type="string"),
                coreapi.Field('patient', required=True,location="formData",type="string"),
                ])


login_schema = AutoSchema(manual_fields=[coreapi.Field("username",required=True,type="string",description="enter your username"),
                    coreapi.Field("password",required=True,type="string",description="enter your password"),])












































# # from rest_framework.schemas import AutoSchema,ManualSchema
# # import coreapi,coreschema
# # from drf_yasg import openapi
# # User_schema = AutoSchema(manual_fields=[coreapi.Field("user_type",required=True,type="string",description="enter username"),
# #                 coreapi.Field("phone_no",required=True,type="string",description="enter phoneno"),
# #                 coreapi.Field("business_name",required=True,type="string",description="enter Business_name"),
# #                 coreapi.Field("created_by",required=True,type="string",description="created_by"),
# #                 coreapi.Field("modified_by",required=True,type="string",description="modified_by"),])

# # branchs_schema = AutoSchema(manual_fields=[coreapi.Field("branch_name",required=True,type="string",description="enter branch_name"),
# #                 coreapi.Field("branch_location",required=True,type="string",description="enter branch_location"),])


# # Branch_Schema = openapi.Parameter(name="branch_name",in_=openapi.IN_BODY,type="string",description="enter branch_name",required=True),openapi.Parameter(name="branch_locations",in_=openapi.IN_BODY,type="string",description="enter branch_location",required=True),

