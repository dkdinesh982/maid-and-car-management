from django.db import models

from autheticate.models import *

class Society(models.Model):
    society=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name = 'society')
    society_name=models.CharField(max_length=100)
    sector_area=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    state=models.CharField(max_length=256)
    pincode=models.CharField(max_length=6)
    no_of_towers=models.IntegerField()
    tower=models.CharField(max_length=100)
    def __str__(self):
        return self.sector_area

class Residents(models.Model):
    residents=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name = 'residents')
    mobile_number=models.CharField(max_length=13)
    total_family_member=models.CharField(max_length=256)
    flat_no=models.IntegerField()
    flat_type=models.CharField(max_length=256)
    type_choice=(
        ('tenat','tenat'),
        ('owner','owner')
    )
    type=models.CharField(choices=type_choice,max_length=10)
    agreement=models.CharField(max_length=100,null=True)
    owner_name=models.CharField(max_length=256,null=True)
    owner_number=models.CharField(max_length=13,null=True)
    
    id_proof=models.FileField(upload_to='idproof_images')
    city=models.CharField(max_length=256)
    def __str__(self):
        return self.residents.name

class Employee(models.Model):
    # employee_image=models.ImageField(upload_to='employee_images',null=True,blank=True)
    # employeeresidents=models.ForeignKey(Residents,on_delete=models.CASCADE,related_name = 'employeeresidents')
    # employeesociety=models.ForeignKey(Society,on_delete=models.CASCADE,related_name = 'employeesociety')
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    current_address=models.CharField(max_length=256)
    adhar_no=models.IntegerField()
    police_verfication=models.CharField(max_length=13)
    provider_choice=(
        ('maids','maids'),
        ('cook','cook'),
        ('child_care','child_care'),
        ('elder_care','elder_care'),
        ('car_cleaner','car_cleaner'),
        ('driver','driver')
    )
    service_provider=models.CharField(choices=provider_choice,max_length=10)
    employee_type=(
        ('24 hours','24 hours'),
        ('12 hours','12 hours'),
        ('part_time','part_time'),
    )
    type=models.CharField(choices=employee_type,max_length=10)

    landlord_address=models.CharField(max_length=100,null=True)
    landlord_number=models.IntegerField()
    landlard_permanetaddress=models.CharField(max_length=100,null=True)
    land_family_no=models.CharField(max_length=13,null=True)
    emergency_no=models.CharField(max_length=13,null=True)
    society_name=models.CharField(max_length=100)
    tower=models.IntegerField()
    flat_type=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee')
    attandance_choice=(
        ('a','a'),
        ('p','p')
    )
    attandance=models.CharField(choices=attandance_choice,max_length=10)
    date_fields=models.DateField()
    month=models.CharField(max_length=15)
    def __str__(self):
        return self.employee.name
class Request_backup(models.Model):
    emp_request=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='emp_request')
    society_request=models.ForeignKey(Society,on_delete=models.CASCADE,related_name='society_request')
    resident_request=models.ForeignKey(Residents,on_delete=models.CASCADE,related_name='resident_request')
    username=models.CharField(max_length=100)
    pay_amount=models.CharField(max_length=10)
    mobile_number=models.CharField(max_length=100)
    def __str__(self):
        return self.username

# class Generate_Report(models.Model):
#     resident_generate=models.ForeignKey(Residents,on_delete=models.CASCADE,related_name='resident_generate')
#     society_generate=models.ForeignKey(Society,on_delete=models.CASCADE,related_name='society_generate')
#     employee_generate=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_generate')
#     start_date=models.DateField()
#     end_date=models.DateField()


# class GenerateReport(models.Model):

#     resident_generate=models.ForeignKey(Residents,on_delete=models.CASCADE,related_name='resident_generate')
#     society_generate=models.ForeignKey(Society,on_delete=models.CASCADE,related_name='society_generate')
#     employee_generate=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_generate')
#     attendance_generate=models.ForeignKey(Attendance,on_delete=models.CASCADE,related_name='attendance_generate')
#     requestbackup_generate=models.ForeignKey(Request_backup,on_delete=models.CASCADE,related_name='requestbackup_generate')
#     start_date=models.DateField()
#     end_date=models.DateField()
