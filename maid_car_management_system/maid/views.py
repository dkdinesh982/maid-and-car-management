from django.shortcuts import render
import traceback
from rest_framework import status
# Create your views here.
from .models import *
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
# from django.core.paginator import Paginator
from django.core import paginator
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from maid.filter import UserFilter
class SocietyViewSet(viewsets.ViewSet):

    def list(self,request):
        search=request.GET.get('search')
        if search:
            try:
                
                societydata=Society.objects.filter(Q(city__icontains=search))
                page = request.GET.get('page')
                

                paginator = Paginator(societydata,10)
                
                total_page= paginator.num_pages
                
                try:
                    societydatas = paginator.page(page)
                except PageNotAnInteger:
                    societydatas = paginator.page(1)
                except EmptyPage:
                    societydatas = paginator.page(paginator.num_pages)
                societydatasearch=[]

                
                for societydata in societydatas:
                    societydatasearch.append({

                        'society_name':societydata.society_name,
                        'sector_area':societydata.sector_area,
                        'city':societydata.city,
                        'state':societydata.state,
                        'pincode':societydata.pincode,
                        'no_of_towers':societydata.no_of_towers,
                        'tower':societydata.tower,
                    })
                return Response({'response':societydatasearch,'total_no_of_pages':total_page,'status':status.HTTP_200_OK,'message':True})
            except Exception as error:
                traceback.print_exc()
                return Response({'message':str(error),'status':status.HTTP_200_OK,'message':False})
        else:
            try:

                society_list = Society.objects.all()
                page = request.GET.get('page')
                

                paginator = Paginator(society_list,10)
                
                total_page= paginator.num_pages
                
                try:
                    societys = paginator.page(page)
                except PageNotAnInteger:
                    societys = paginator.page(1)
                except EmptyPage:
                    societys = paginator.page(paginator.num_pages)
                userdatalist=[]
                for societydata in societys:
                    userdatalist.append({
                        'id':societydata.id,
                        'society_name':societydata.society_name,
                        'sector_area':societydata.sector_area,
                        'city':societydata.city,
                        'state':societydata.state,
                        'pincode':societydata.pincode,
                        'no_of_towers':societydata.no_of_towers,
                        # 'tower':societydata.tower,
                    })
                
                    
                return Response({'response':userdatalist,'total_pages':total_page,'status':status.HTTP_200_OK,'success':True})
            except Exception as error:
                traceback.print_exc()
                return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})
    def create(self,request):
        
        try:
           
            societydata=MyUser.objects.get(email=request.user)
           
            datasociiety=Society()
            datasociiety.society=societydata
            datasociiety.society_name=request.data.get('society_name')
            datasociiety.sector_area=request.data.get('sector_area')
            datasociiety.city=request.data.get('city')
            datasociiety.state=request.data.get('state')
            datasociiety.pincode=request.data.get('pincode')
            datasociiety.no_of_towers=request.data.get('no_of_towers')
            # datasociiety.tower=request.data.get('tower')

            datasociiety.save()
            return Response({'response':'data created successfully','status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})
    def update(self,request,pk=None):
        try:
            society_name=request.data.get('society_name')
            if not request.data.get('society_name'):
                return Response({'response':'Enter the society name','success':True,'status':status.HTTP_200_OK})
            societydata=Society.objects.get(id=pk)
            
            societydata.society_name=society_name
            sector_area=request.data.get('sector_area')
            if not sector_area:
                return Response({'response':'Enter the sector area','success':True,'status':status.HTTP_200_OK})

            societydata.sector_area=sector_area
            
            
            city=request.data.get('city')
            if not city:
                return Response({'response':'Enter the city','success':True,'status':status.HTTP_200_OK})

            societydata.city=city
            
            state=request.data.get('state')
            if not state:
                return Response({'response':'Enter the state','success':True,'status':status.HTTP_200_OK})
            societydata.state=state
            pincode=request.data.get('pincode')
            if not pincode:
                return Response({'response':'Enter the pincode','success':True,'status':status.HTTP_200_OK})

            societydata.pincode=pincode
            no_of_towers=request.data.get('no_of_towers')
            if not no_of_towers:
                return Response({'response':'Enter the no_of_towers','success':True,'status':status.HTTP_200_OK})
            societydata.no_of_towers=no_of_towers
            # tower=request.data.get('tower')
            # if not tower:
            #     return Response({'response':'Enter the tower','success':True,'status':status.HTTP_200_OK})
            
            # societydata.tower=tower
            # 
            societydata.save()
            return Response({'data':'updated successfully','status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})
    def destroy(self,request,pk=None):
        try:
            society=Society.objects.filter(id=pk).delete()
            return Response({'response':'society data successfully deleted','status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})

    def retrieve(self,request,pk=None):
        try:

            societyretrievedata=Society.objects.get(id=pk)
            societyretrievedata_list=[{
                'id':societyretrievedata.id,
                'society_name':societyretrievedata.society_name,
                'sector_area':societyretrievedata.sector_area,
                'city':societyretrievedata.city,
                'state':societyretrievedata.state,
                'pincode':societyretrievedata.pincode,
                'no_of_towers':societyretrievedata.no_of_towers,
                # 'tower':societyretrievedata.tower
            }]
            
            return Response({'response':societyretrievedata_list,'status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})


class ResidentsViewSet(viewsets.ViewSet):
    def list(self,request):
        search=request.GET.get('search')
        type=request.GET.get('type')
        if type:
            try:
                # residentsdata=Residents.objects.filter(Q(city__icontains=search))
               
                
                residentsdata=Residents.objects.filter(Q(type__icontains=type)) 
                page = request.GET.get('page')
                

                paginator = Paginator(residentsdata,2)
                
                total_page= paginator.num_pages
                
                try:
                    residentsdata = paginator.page(page)
                except PageNotAnInteger:
                    residentsdata = paginator.page(1)
                except EmptyPage:
                    residentsdata = paginator.page(paginator.num_pages)
                residentsdatasearchtypelist=[]
                for residentsdata in residentsdata:
                    residentsdatasearchtypelist.append({
                        'mobile_number':residentsdata.mobile_number,
                        'total_family_member':residentsdata.total_family_member,
                        'flat_no':residentsdata.flat_no,
                        'flat_type':residentsdata.flat_type,
                        'type':residentsdata.type,
                        'agreement':residentsdata.agreement,
                        'owner_name':residentsdata.owner_name,
                        'owner_number':residentsdata.owner_number,
                        'id_proof':residentsdata.id_proof.url,
                        'city':residentsdata.city,
                    })
                
                return Response({'messsage':residentsdatasearchtypelist,'total_no_pages':total_page,'message':True,'status':status.HTTP_200_OK})
            except Exception as error:
                traceback.print_exc()
                return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
       
        else:


            if search:
                try:
                    
                    residentsdata=Residents.objects.filter(Q(city__icontains=search))
                    page = request.GET.get('page')
                    

                    paginator = Paginator(residentsdata,2)
                    
                    total_page= paginator.num_pages
                    
                    try:
                        residentsdata = paginator.page(page)
                    except PageNotAnInteger:
                        residentsdata = paginator.page(1)
                    except EmptyPage:
                        residentsdata = paginator.page(paginator.num_pages)
                    residentsdatasearchlist=[]
                    for residentsdata in residentsdata:
                        residentsdatasearchlist.append({
                            'mobile_number':residentsdata.mobile_number,
                            'total_family_member':residentsdata.total_family_member,
                            'flat_no':residentsdata.flat_no,
                            'flat_type':residentsdata.flat_type,
                            'type':residentsdata.type,
                            'agreement':residentsdata.agreement,
                            'owner_name':residentsdata.owner_name,
                            'owner_number':residentsdata.owner_number,
                            'id_proof':residentsdata.id_proof.url,
                            'city':residentsdata.city,
                        })
                    return Response({'response':residentsdatasearchlist,'total_no_pages':total_page,'message':True,'status':status.HTTP_200_OK})
                except Exception as error:
                    traceback.print_exc()
                    return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
    
            else:
                    
                try:
                    residents_data=Residents.objects.all()
                    page = request.GET.get('page')

                    paginator = Paginator(residents_data,10)
                    total_page= paginator.num_pages
                    try:
                        users = paginator.page(page)
                    except PageNotAnInteger:
                        users = paginator.page(1)
                    except EmptyPage:
                        users = paginator.page(paginator.num_pages)
                    residents_data_list=[]
                    for residents_data in users:
                        residents_data_list.append({
                            'id':residents_data.id,
                            'mobile_number':residents_data.mobile_number,
                            'total_family_member':residents_data.total_family_member,
                            'flat_no':residents_data.flat_no,
                            'flat_type':residents_data.flat_type,
                            'type':residents_data.type,
                            'agreement':residents_data.agreement,
                            'owner_name':residents_data.owner_name,
                            'owner_number':residents_data.owner_number,
                            'id_proof':residents_data.id_proof.url,
                            'city':residents_data.city,

                        })
                    return Response({'response':residents_data_list,'total_pages':total_page,'status':status.HTTP_200_OK,'success':True})
                
                except Exception as error:
                    traceback.print_exc()
                    return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})
                
    def create(self,request):
        try:
            regident_data=MyUser.objects.get(email=request.user)
            residents_data=Residents()
            residents_data.residents=regident_data
            residents_data.mobile_number=request.data.get('mobile_number')
            residents_data.total_family_member=request.data.get('total_family_member')
            residents_data.flat_no=request.data.get('flat_no')
            residents_data.flat_type=request.data.get('flat_type')
            residents_data.type=request.data.get('type')
            residents_data.agreement=request.data.get('agreement')
            residents_data.owner_name=request.data.get('owner_name')
            residents_data.owner_number=request.data.get('owner_number')
            residents_data.id_proof=request.data.get('id_proof')
            residents_data.city=request.data.get('city')
            residents_data.save()
            return Response({'response':'created successfully','status':status.HTTP_200_OK,'success':True}) 
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})
    def update(self,request,pk=None):
        try:
            residentsdata=Residents.objects.get(id=pk)
            mobile_number=request.data.get('mobile_number')
            if not mobile_number:
                return Response({'response':'please enter the mobile_number ','success':True,'status':status.HTTP_200_OK})
            residentsdata.mobile_number=mobile_number
            total_family_member=request.data.get('total_family_member')
            if not total_family_member:
                return Response({'response':'please enter the total_family_member ','success':True,'status':status.HTTP_200_OK})
            residentsdata.total_family_member=total_family_member
            flat_no=request.data.get('flat_no')
            if not flat_no:
                return Response({'response':'please enter the flat_no ','success':True,'status':status.HTTP_200_OK})
            residentsdata.flat_no=flat_no
            flat_type=request.data.get('flat_type')
            if not flat_type:
                return Response({'response':'please enter the flat_type ','success':True,'status':status.HTTP_200_OK})
            residentsdata.flat_type=flat_type
            type=request.data.get('type')
            if not type:
                return Response({'response':'please enter the type ','success':True,'status':status.HTTP_200_OK})
            residentsdata.type=type
            agreement=request.data.get('agreement')
            if not agreement:
                return Response({'response':'please enter the agreement ','success':True,'status':status.HTTP_200_OK})
            residentsdata.agreement=agreement
            owner_name=request.data.get('owner_name')
            if not owner_name:
                return Response({'response':'please enter the owner_name ','success':True,'status':status.HTTP_200_OK})
            residentsdata.owner_name=owner_name
            owner_number=request.data.get('owner_number')
            if not owner_number:
                return Response({'response':'please enter the owner_number ','success':True,'status':status.HTTP_200_OK})
            residentsdata.owner_number=owner_number
            id_proof=request.data.get('id_proof')
            if not id_proof:
                return Response({'response':'please enter the id_proof ','success':True,'status':status.HTTP_200_OK})
            residentsdata.id_proof=id_proof
            city=request.data.get('city')
            if not city:
                return Response({'response':'please enter the city ','success':True,'status':status.HTTP_200_OK})
            residentsdata.city=city
            residentsdata.save()
            return Response({'response':'data updated successfully','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def destroy(self,request,pk=None):
        try:
            data=Residents.objects.get(id=pk).delete()
            return Response({'response':'data deleted successfully','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def retrieve(self,request,pk=None):
        try:
            residentsdata=Residents.objects.get(id=pk)
            residentsdata_list=[{
                'mobile_number':residentsdata.mobile_number,
                'total_family_member':residentsdata.total_family_member,
                'flat_no':residentsdata.flat_no,
                'flat_type':residentsdata.flat_type,
                'type':residentsdata.type,
                'agreement':residentsdata.agreement,
                'owner_name':residentsdata.owner_name,
                'owner_number':residentsdata.owner_number,
                'id_proof':residentsdata.id_proof.url,
                'city':residentsdata.city,
                    
            }]
            return Response({'response':residentsdata_list,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
        


class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        search=request.GET.get('search')
        type=request.GET.get('type')
        if type:
            employeedatasearch=Employee.objects.filter(Q(service_provider__icontains=type))
            page = request.GET.get('page')

            paginator = Paginator(employeedatasearch,10)
            total_page= paginator.num_pages
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)

            employeedatasearch_list=[]
            for employeedatasearch in employeedatasearch:
                employeedatasearch_list.append({
                    'id':employeedatasearch.id,
                    'name':employeedatasearch.name,
                    'age':employeedatasearch.age,
                    'cuurent_Address':employeedatasearch.current_address,
                    'adhar_no':employeedatasearch.adhar_no,
                    'police_verfication,':employeedatasearch.police_verfication,
                    'service_provider':employeedatasearch.service_provider,
                    'type':employeedatasearch.type
                })
            return Response({'response':employeedatasearch_list,'total_no_of_pages':total_page,'message':True,'status':status.HTTP_200_OK})
        else:
                
            if search:
                employeedatasearch=Employee.objects.filter(Q(name__icontains=search))
                page = request.GET.get('page')

                paginator = Paginator(employeedatasearch,10)
                total_page= paginator.num_pages
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    users = paginator.page(1)
                except EmptyPage:
                    users = paginator.page(paginator.num_pages)

                employeedatasearch_list=[]
                for employeedatasearch in employeedatasearch:
                    employeedatasearch_list.append({
                        'id':employeedatasearch.id,
                        'name':employeedatasearch.name,
                        'age':employeedatasearch.age,
                        'current_address':employeedatasearch.current_address,
                        'adhar_no':employeedatasearch.adhar_no,
                        'police_verfication,':employeedatasearch.police_verfication,
                        'service_provider':employeedatasearch.service_provider,
                        'type':employeedatasearch.type
                    })
                return Response({'response':employeedatasearch_list,'total_no_of_pages':total_page,'message':True,'status':status.HTTP_200_OK})
            else:

                try:
                    employee_data=Employee.objects.all()
                    page = request.GET.get('page')

                    paginator = Paginator(employee_data,10)
                    total_page= paginator.num_pages
                    try:
                        users = paginator.page(page)
                    except PageNotAnInteger:
                        users = paginator.page(1)
                    except EmptyPage:
                        users = paginator.page(paginator.num_pages)
                    employee_data_list=[]
                    for employee_data in users:
                        employee_data_list.append({
                            'id':employee_data.id,
                            # 'employee_image':employee_data.employee_image.url,
                            'name':employee_data.name,
                            'age':employee_data.age,
                            'cuurent_Address':employee_data.current_address,
                            'adhar_no':employee_data.adhar_no,
                            'police_verfication,':employee_data.police_verfication,
                            'service_provider':employee_data.service_provider,
                            'type':employee_data.type
                        })
                    return Response({'response':employee_data_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
                except Exception as error:
                    traceback.print_exc()
                    return Response({'message':str(error),'success':False,'status':status.HTTP_200_OK})
    def create(self,request):
        try:
            # resident_data=Residents.objects.get(id=request.data.get('resident_id'))
            # society_data=Society.objects.get(id=request.data.get('society_id'))
            # Society.objects.get()
            employee=Employee()
            employee.employee_image=request.data.get('employee_image')
            employee.name=request.data.get('name')
            employee.current_address=request.data.get('current_address')
            employee.age=request.data.get('age')
            employee.adhar_no=request.data.get('adhar_no')
            employee.police_verfication=request.data.get('police_verfication')
            employee.service_provider=request.data.get('service_provider')
            employee.type=request.data.get('type')
            employee.landlord_address=request.data.get('landlord_address')
            employee.landlord_number=request.data.get('landlord_number')
            employee.landlard_permanetaddress=request.data.get('landlard_permanetaddress')
            employee.land_family_no=request.data.get('land_family_no')
            employee.emergency_no=request.data.get('emergency_no')
            employee.society_name=request.data.get('society_name')
            employee.tower=request.data.get('tower')
            employee.flat_type=request.data.get('flat_type')
            
            employee.save()
            return Response({'response':'created data successfully','message':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({"message": str(error), "success": False}, status=status.HTTP_200_OK)
        
    def retrieve(self,request,pk=None):
        try:
            employeedataretrieve=Employee.objects.get(id=pk)
            empdatalist={
                'id':employeedataretrieve.id,
                'name':employeedataretrieve.name,
                'age':employeedataretrieve.age,
                'current_address':employeedataretrieve.current_address,
                'adhar_no':employeedataretrieve.adhar_no,
                'police_verfication':employeedataretrieve.police_verfication,
                'service_provider':employeedataretrieve.service_provider,
                'type':employeedataretrieve.type,
                'landlord_address':employeedataretrieve.landlord_address,
                'landlord_number':employeedataretrieve.landlord_number,
                'emergency_no':employeedataretrieve.emergency_no,
                'landlard_permanetaddress':employeedataretrieve.landlard_permanetaddress,
                'land_family_no':employeedataretrieve.land_family_no,
                'society_name':employeedataretrieve.society_name,
                'flat_type':employeedataretrieve.flat_type,
                'tower':employeedataretrieve.tower,
            }
            # data=[{
            #     'rersonal_details':empdatalist,
            #     'landlord_details':landlord_list,
            #     'work_details':work_detail_list,
            # }]
            return Response({'employee_retrieve':empdatalist,'status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'messsage':str(error),'message':False,'status':status.HTTP_200_OK})
    def destroy(self,request,pk=None):
        try:
            employeedata=Employee.objects.filter(id=pk).delete()
            return Response({'message':'delete employee data','status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK})
    def update(self,request,pk=None):
        
        try:
            employeedataupdate=Employee.objects.get(id=pk)
            name=request.data.get('name')
            if not name:
                return Response({'response':'enter tha name','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.name=name
            age=request.data.get('age')
            if not age:
                return Response({'response':'enter tha age','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.age=age
            current_address=request.data.get('current_address')
            if not current_address:
                return Response({'response':'enter tha current_address','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.current_address=current_address
            adhar_no=request.data.get('adhar_no')
            if not adhar_no:
                return Response({'response':'enter tha adhar_no','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.adhar_no=adhar_no
            police_verfication=request.data.get('police_verfication')
            if not police_verfication:
                return Response({'response':'enter tha police_verfication','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.police_verfication=police_verfication
            service_provider=request.data.get('service_provider')
            if not service_provider:
                return Response({'response':'enter tha service_provider','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.service_provider=service_provider
            type=request.data.get('type')
            if not type:
                return Response({'response':'enter tha type','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.type=type
            landlord_address=request.data.get('landlord_address')
            if not landlord_address:
                return Response({'response':'enter tha landlord_address','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.landlord_address=landlord_address
            landlard_permanetaddress=request.data.get('landlard_permanetaddress')
            if not landlard_permanetaddress:
                return Response({'response':'enter tha landlard_permanetaddress','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.landlard_permanetaddress=landlard_permanetaddress
            land_family_no=request.data.get('land_family_no')
            if not land_family_no:
                return Response({'response':'enter tha land_family_no','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.land_family_no=land_family_no
            emergency_no=request.data.get('emergency_no')
            if not emergency_no:
                return Response({'response':'enter tha emergency_no','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.emergency_no=emergency_no
            society_name=request.data.get('society_name')
            if not society_name:
                return Response({'response':'enter tha society_name','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.society_name=society_name

            tower=request.data.get('tower')
            if not tower:
                return Response({'response':'enter tha tower','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.tower=tower
            flat_type=request.data.get('flat_type')
            if not flat_type:
                return Response({'response':'enter tha flat_type','success':True,'status':status.HTTP_200_OK})
            employeedataupdate.flat_type=flat_type
            employeedataupdate.save()
            return Response({'response':'updated successfully','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
        


class DashBoardViewSet(viewsets.ViewSet):
    def list(self,request):
        try:
            total_sosiety=0
            socirty_count=0
            societydata=Society.objects.all()
            for societydata in societydata:
                socirty_count+=1
            total_sosiety +=socirty_count
            regidents_data=Residents.objects.all()
            regidents_data_list=[]
            for residentsdata in regidents_data:
                regidents_data_list.append({
                    'id':residentsdata.id,
                    'mobile_number':residentsdata.mobile_number,
                    'total_family_member':residentsdata.total_family_member,
                    'flat_no':residentsdata.flat_no,
                    'flat_type':residentsdata.flat_type,
                    'type':residentsdata.type,
                    'agreement':residentsdata.agreement,
                    'owner_name':residentsdata.owner_name,
                    'owner_number':residentsdata.owner_number,
                    'id_proof':residentsdata.id_proof.url,
                    'city':residentsdata.city,
                })

            regidet_count=0
            total_count=0
            for regidents_data in regidents_data:
                regidet_count+=1
            total_count+=regidet_count
            empdata=Employee.objects.all()
            all_emp_list=[]
            empdata_list=[]
            for emp_data in empdata:
                all_emp_list.append({
                'name':emp_data.name,
                    'service_provider':emp_data.service_provider,

                })
                empdata_list.append({
                    'id':emp_data.id,
                            'name':emp_data.name,
                            'age':emp_data.age,
                            'cuurent_Address':emp_data.current_address,
                            'adhar_no':emp_data.adhar_no,
                            'police_verfication,':emp_data.police_verfication,
                            'service_provider':emp_data.service_provider,
                            'type':emp_data.type
                })
            total_emp=0
            emp_count=0
            for empdata in empdata:
                emp_count+=1
            total_emp+=emp_count
            dashdata=[{
                'total_society':total_sosiety,
                'total_regident':total_count,
                'total_employee':total_emp,
                'target_amount':"50,0000",
                "all_employee_list":all_emp_list[:5],
                # 'society_list':societydata_list,
                'employee_list':empdata_list[:5],
                'residents_data':regidents_data_list[:5],

            }]
         
            return Response({'response':dashdata,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})


class AttendanceViewSet(viewsets.ViewSet):
    def create(self,request):
        try:
            emp=Employee.objects.get(id=request.data.get('emp_id'))
            attendance=Attendance()
            attendance.employee=emp
            attendance.attandance=request.data.get('attandance')
            attendance.date_fields=request.data.get('date_fields')
            # attendance.month=request.data.get('month')
            attendance.save()
            return Response({'response':'created successfully data','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def list(self,request):
        try:
            search=request.GET.get('search')
            name=request.GET.get('name')
            month=request.GET.get('month')
            if month and name:
                attendancedataname=Attendance.objects.filter(Q(date_fields__month=month)&Q(employee__name=name))
                # page = request.GET.get('page')

                # paginator = Paginator(attendancedataname,10)
                # total_page= paginator.num_pages
                # try:
                #     attendancedataname = paginator.page(page)
                # except PageNotAnInteger:
                #     attendancedataname = paginator.page(1)
                # except EmptyPage:
                #     attendancedataname = paginator.page(paginator.num_pages)
                attendancedataname_list=[]
                total_days=0
                present_days = 0
                present_day = 0
                absent_days=0
                absentday=0
                count=0
                for attendancedata in attendancedataname:
                    if attendancedata.attandance == 'p':
                        present_days += 1
                    elif attendancedata.attandance == 'a':
                        absent_days+=1
                    else:
                        pass
                
                    attendancedataname_list.append({
                        'id':attendancedata.id,
                        'name':attendancedata.employee.name,
                            'attandance':attendancedata.attandance,
                        #  'month':attendancedata.month,
                            'date_fields':attendancedata.date_fields,

                    })
                        
                    count+=1
                total_days+=count
                present_day+=present_days
                absentday+=absent_days
                dadalist=[{
                    'attendance_details':attendancedataname_list,
                     'present_day':present_day,
                     'absent_days':absent_days,
                     'total_days_count':total_days,
                }]
                return Response({'response':dadalist,'success':True,'status':status.HTTP_200_OK})
            else:

                
                attendancedata=Attendance.objects.filter(Q(date_fields__month=search))
                page = request.GET.get('page')

                paginator = Paginator(attendancedata,10)
                total_page= paginator.num_pages
                try:
                    attendancedata = paginator.page(page)
                except PageNotAnInteger:
                    attendancedata = paginator.page(1)
                except EmptyPage:
                    attendancedata = paginator.page(paginator.num_pages)
                attendancedata_list=[]
                for attendancedata in attendancedata:
                    attendancedata_list.append({
                        'id':attendancedata.employee.id,
                        'name':attendancedata.employee.name,
                        'age':attendancedata.employee.age,
                        'cuurent_Address':attendancedata.employee.current_address,
                        'adhar_no':attendancedata.employee.adhar_no,
                        'police_verfication,':attendancedata.employee.police_verfication,
                        'service_provider':attendancedata.employee.service_provider,
                        'type':attendancedata.employee.type,
                        # 'emp_name':attendancedata.employee.name,
                        'attandance':attendancedata.attandance,
                        'date_fields':attendancedata.date_fields,
                        # 'month':attendancedata.month,
                        
                    })
                
                return Response({'response':attendancedata_list,'total_page':total_page,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def retrieve(self,request,pk=None):
        try:
            empdata_data=Employee.objects.filter(id=pk)
            empdata_data_list=[]
            employee_list=[]
            for empdata_data in empdata_data:
                employee_list=[{
                    'id':empdata_data.id,
                    'name':empdata_data.name,
                    'age':empdata_data.age,
                    'current_address':empdata_data.current_address,
                    'adhar_no':empdata_data.adhar_no,
                    'police_verfication':empdata_data.police_verfication,
                    'service_provider':empdata_data.service_provider,
                    'type':empdata_data.type
                }]
                for eempdata_datadd in empdata_data.employee.all():
                    
                    empdata_data_list.append({

                        
                        'attandance':eempdata_datadd.attandance,
                        'months':eempdata_datadd.date_fields.month,
                        'day':eempdata_datadd.date_fields.day,
                        
                        
                    })
                data=[{
                    'employee':employee_list,
                    'attendance':empdata_data_list,
                    
                }]
            return Response({'response':data,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})


class Request_backupViewSet(viewsets.ViewSet):
    def list(self,request):
        try:
            search=request.GET.get('search')
            type=request.GET.get('type')
            service=request.GET.get('service')
            if search:
                requestbackupdata=Request_backup.objects.filter(Q(username__icontains=search))
                page = request.GET.get('page')

                paginator = Paginator(requestbackupdata,10)
                total_page= paginator.num_pages
                try:
                    requestbackupdata = paginator.page(page)
                except PageNotAnInteger:
                    requestbackupdata = paginator.page(1)
                except EmptyPage:
                    requestbackupdata = paginator.page(paginator.num_pages)
                print("pppppppp",requestbackupdata)
                requestbackupdata_list=[]
                for requestbackupdata in requestbackupdata:
                    requestbackupdata_list.append({
                        'employee_name':requestbackupdata.emp_request.name,
                        'age':requestbackupdata.emp_request.age,
                        'mobile':requestbackupdata.emp_request.emergency_no,
                        'service':requestbackupdata.emp_request.service_provider,
                        'type':requestbackupdata.emp_request.type,
                        'pay_amount':requestbackupdata.pay_amount,
                        'user_name':requestbackupdata.username,
                        'mobile_number':requestbackupdata.mobile_number,
                        'society_name':requestbackupdata.society_request.society_name,
                        'tower':requestbackupdata.society_request.tower,
                        'flat_no':requestbackupdata.resident_request.flat_no,
                        'types':requestbackupdata.resident_request.type,
                    })
                return Response({'response':requestbackupdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
            # else:
            #     type=request.GET.get('type')
        # service=request.GET.get('service')
            elif service:
                servicedata=Request_backup.objects.filter(Q(emp_request__service_provider=service)) 
                page = request.GET.get('page')

                paginator = Paginator(servicedata,10)
                total_page= paginator.num_pages
                try:
                    servicedata = paginator.page(page)
                except PageNotAnInteger:
                    servicedata = paginator.page(1)
                except EmptyPage:
                    servicedata = paginator.page(paginator.num_pages)
                servicedata_list=[]
                for servicedata in servicedata:
                    servicedata_list.append({
                        'employee_name':servicedata.emp_request.name,
                        'age':servicedata.emp_request.age,
                        'mobile':servicedata.emp_request.emergency_no,
                        'service':servicedata.emp_request.service_provider,
                        'type':servicedata.emp_request.type,
                        'pay_amount':servicedata.pay_amount,
                        'user_name':servicedata.username,
                        'mobile_number':servicedata.mobile_number,
                        'society_name':servicedata.society_request.society_name,
                        'tower':servicedata.society_request.tower,
                        'flat_no':servicedata.resident_request.flat_no,
                        'types':servicedata.resident_request.type,
                    })
                return Response({'response':servicedata_list,'total_page':total_page,'success':True,'status':status.HTTP_200_OK})
                #     else:

            elif type:
                residentdata_list=[]
                residentdata=Request_backup.objects.filter(Q(resident_request__type=type))
                page = request.GET.get('page')

                paginator = Paginator(residentdata,10)
                total_page= paginator.num_pages
                try:
                    residentdata = paginator.page(page)
                except PageNotAnInteger:
                    residentdata = paginator.page(1)
                except EmptyPage:
                    residentdata = paginator.page(paginator.num_pages)
                for residentdata in residentdata:
                    residentdata_list.append({
                        'id':residentdata.id,
                        'employee_name':residentdata.emp_request.name,
                        'age':residentdata.emp_request.age,
                        'mobile':residentdata.emp_request.emergency_no,
                        'service':residentdata.emp_request.service_provider,
                        'type':residentdata.emp_request.type,
                        'pay_amount':residentdata.pay_amount,
                        'user_name':residentdata.username,
                        'mobile_number':residentdata.mobile_number,
                        'society_name':residentdata.society_request.society_name,
                        'tower':residentdata.society_request.tower,
                        'flat_no':residentdata.resident_request.flat_no,
                        'types':residentdata.resident_request.type,
                    })
                    
                return Response({'response':residentdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
            else:
                requestdata=Request_backup.objects.all()
                page = request.GET.get('page')

                paginator = Paginator(requestdata,5)
                total_page= paginator.num_pages
                try:
                    requestdata = paginator.page(page)
                except PageNotAnInteger:
                    requestdata = paginator.page(1)
                except EmptyPage:
                    requestdata = paginator.page(paginator.num_pages)
                requestdata_list=[]
                for requestdata in requestdata:
                    requestdata_list.append({
                        'employee_name':requestdata.emp_request.name,
                        'age':requestdata.emp_request.age,
                        'mobile':requestdata.emp_request.emergency_no,
                        'service':requestdata.emp_request.service_provider,
                        'type':requestdata.emp_request.type,
                        'pay_amount':requestdata.pay_amount,
                        'user_name':requestdata.username,
                        'mobile_number':requestdata.mobile_number,
                        'society_name':requestdata.society_request.society_name,
                        'tower':requestdata.society_request.tower,
                        'flat_no':requestdata.resident_request.flat_no,
                        'types':requestdata.resident_request.type,
                        

                    })
                return Response({'request_backup':requestdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def create(self,request):
        try:
            requestemployee=Employee.objects.get(id=request.data.get('employee_id'))
            requestsociety=Society.objects.get(id=request.data.get('society_id'))
            requestresidents=Residents.objects.get(id=request.data.get('resident_id'))

            requestbackup=Request_backup()
            requestbackup.emp_request=requestemployee
            requestbackup.society_request=requestsociety
            requestbackup.resident_request=requestresidents
            requestbackup.username=request.data.get('username')
            requestbackup.pay_amount=request.data.get('pay_amount')
            requestbackup.mobile_number=request.data.get('mobile_number')
            requestbackup.save()
            return Response({'response':'created successfully','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
class Sortlist_Request_backup(viewsets.ViewSet):
    def list(self,request):
        try:
            search=request.GET.get('search')
            type=request.GET.get('type')
            service=request.GET.get('service')
            if search:
                requestbackupdata=Request_backup.objects.filter(Q(username__icontains=search))
                page = request.GET.get('page')

                paginator = Paginator(requestbackupdata,10)
                total_page= paginator.num_pages
                try:
                    requestbackupdata = paginator.page(page)
                except PageNotAnInteger:
                    requestbackupdata = paginator.page(1)
                except EmptyPage:
                    requestbackupdata = paginator.page(paginator.num_pages)
                print("pppppppp",requestbackupdata)
                requestbackupdata_list=[]
                for requestbackupdata in requestbackupdata:
                    requestbackupdata_list.append({
                        'user_name':requestbackupdata.username,
                        'mobile_number':requestbackupdata.mobile_number,
                        'society_name':requestbackupdata.society_request.society_name,
                        'tower':requestbackupdata.society_request.tower,
                        'flat_no':requestbackupdata.resident_request.flat_no,
                        'types':requestbackupdata.resident_request.type,
                        'employee_name':requestbackupdata.emp_request.name,
                        'employee_age':requestbackupdata.emp_request.age,
                        'employee_mobile':requestbackupdata.emp_request.emergency_no,
                        'service':requestbackupdata.emp_request.service_provider,
                        'type':requestbackupdata.emp_request.type,
                        'pay_amount':requestbackupdata.pay_amount,
                        
                    })
                return Response({'response':requestbackupdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
            # else:
                # type=request.GET.get('type')
                # service=request.GET.get('service')
            elif service:
                servicedata=Request_backup.objects.filter(Q(emp_request__service_provider=service)) 
                page = request.GET.get('page')

                paginator = Paginator(servicedata,10)
                total_page= paginator.num_pages
                try:
                    servicedata = paginator.page(page)
                except PageNotAnInteger:
                    servicedata = paginator.page(1)
                except EmptyPage:
                    servicedata = paginator.page(paginator.num_pages)
                servicedata_list=[]
                for servicedata in servicedata:
                    servicedata_list.append({
                        'user_name':servicedata.username,
                        'mobile_number':servicedata.mobile_number,
                        'society_name':servicedata.society_request.society_name,
                        'tower':servicedata.society_request.tower,
                        'flat_no':servicedata.resident_request.flat_no,
                        'types':servicedata.resident_request.type,
                        'employee_name':servicedata.emp_request.name,
                        'employee_age':servicedata.emp_request.age,
                        'employee_mobile':servicedata.emp_request.emergency_no,
                        'service':servicedata.emp_request.service_provider,
                        'type':servicedata.emp_request.type,
                        'pay_amount':servicedata.pay_amount,
                        
                    })
                return Response({'shortlished_response':servicedata_list,'total_page':total_page,'success':True,'status':status.HTTP_200_OK})
                # else:

            elif type:
                residentdata_list=[]
                residentdata=Request_backup.objects.filter(Q(resident_request__type=type))
                page = request.GET.get('page')

                paginator = Paginator(residentdata,10)
                total_page= paginator.num_pages
                try:
                    residentdata = paginator.page(page)
                except PageNotAnInteger:
                    residentdata = paginator.page(1)
                except EmptyPage:
                    residentdata = paginator.page(paginator.num_pages)
                for residentdata in residentdata:
                    residentdata_list.append({
                        'id':residentdata.id,
                        'user_name':residentdata.username,
                        'mobile_number':residentdata.mobile_number,
                        'society_name':residentdata.society_request.society_name,
                        'tower':residentdata.society_request.tower,
                        'flat_no':residentdata.resident_request.flat_no,
                        'types':residentdata.resident_request.type,
                        'employee_name':residentdata.emp_request.name,
                        'employee_age':residentdata.emp_request.age,
                        'employee_mobile':residentdata.emp_request.emergency_no,
                        'service':residentdata.emp_request.service_provider,
                        'type':residentdata.emp_request.type,
                        'pay_amount':residentdata.pay_amount,
                        
                    })
                    
                return Response({'shortlished_response':residentdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
            else:
                requestdata=Request_backup.objects.all()
                page = request.GET.get('page')

                paginator = Paginator(requestdata,2)
                total_page= paginator.num_pages
                try:
                    requestdata = paginator.page(page)
                except PageNotAnInteger:
                    requestdata = paginator.page(1)
                except EmptyPage:
                    requestdata = paginator.page(paginator.num_pages)
                requestdata_list=[]
                for requestdata in requestdata:
                    requestdata_list.append({
                        'user_name':requestdata.username,
                        'mobile_number':requestdata.mobile_number,
                        'society_name':requestdata.society_request.society_name,
                        'tower':requestdata.society_request.tower,
                        'flat_no':requestdata.resident_request.flat_no,
                        'types':requestdata.resident_request.type,
                        'employee_name':requestdata.emp_request.name,
                        'employee_age':requestdata.emp_request.age,
                        'employee_mobile':requestdata.emp_request.emergency_no,
                        'service':requestdata.emp_request.service_provider,
                        'type':requestdata.emp_request.type,
                        'pay_amount':requestdata.pay_amount,
                        
                        

                    })
                return Response({'shortlished_response':requestdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
        
class ReplacementBackupViewSet(viewsets.ViewSet):
    def list(self,request):
        try:
            search=request.GET.get('search')
            service=request.GET.get('service')
            type=request.GET.get('type')
            if search:
                requestbackupdata=Request_backup.objects.filter(Q(username__icontains=search))
                page = request.GET.get('page')

                paginator = Paginator(requestbackupdata,10)
                total_page= paginator.num_pages
                try:
                    requestbackupdata = paginator.page(page)
                except PageNotAnInteger:
                    requestbackupdata = paginator.page(1)
                except EmptyPage:
                    requestbackupdata = paginator.page(paginator.num_pages)
                print("pppppppp",requestbackupdata)
                requestbackupdata_list=[]
                for requestbackupdata in requestbackupdata:
                    requestbackupdata_list.append({
                        'user_name':requestbackupdata.username,
                        'mobile_number':requestbackupdata.mobile_number,
                        'society_name':requestbackupdata.society_request.society_name,
                        'tower':requestbackupdata.society_request.tower,
                        'flat_no':requestbackupdata.resident_request.flat_no,
                        'types':requestbackupdata.resident_request.type,
                        'employee_name':requestbackupdata.emp_request.name,
                        'employee_age':requestbackupdata.emp_request.age,
                        'employee_mobile':requestbackupdata.emp_request.emergency_no,
                        'service':requestbackupdata.emp_request.service_provider,
                        'type':requestbackupdata.emp_request.type,
                        'pay_amount':requestbackupdata.pay_amount,
                        
                    })
                return Response({'response':requestbackupdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
            # else:
                # type=request.GET.get('type')
                # service=request.GET.get('service')
            elif service:
                servicedata=Request_backup.objects.filter(Q(emp_request__service_provider=service)) 
                page = request.GET.get('page')

                paginator = Paginator(servicedata,5)
                total_page= paginator.num_pages
                try:
                    servicedata = paginator.page(page)
                except PageNotAnInteger:
                    servicedata = paginator.page(1)
                except EmptyPage:
                    servicedata = paginator.page(paginator.num_pages)
                servicedata_list=[]
                for servicedata in servicedata:
                    servicedata_list.append({
                        'user_name':servicedata.username,
                        'mobile_number':servicedata.mobile_number,
                        'society_name':servicedata.society_request.society_name,
                        'tower':servicedata.society_request.tower,
                        'flat_no':servicedata.resident_request.flat_no,
                        'types':servicedata.resident_request.type,
                        'employee_name':servicedata.emp_request.name,
                        'employee_age':servicedata.emp_request.age,
                        'employee_mobile':servicedata.emp_request.emergency_no,
                        'service':servicedata.emp_request.service_provider,
                        'type':servicedata.emp_request.type,
                        'pay_amount':servicedata.pay_amount,
                        
                    })
                return Response({'response':servicedata_list,'total_page':total_page,'success':True,'status':status.HTTP_200_OK})
                # else:

            elif type:
                residentdata_list=[]
                residentdata=Request_backup.objects.filter(Q(resident_request__type=type))
                page = request.GET.get('page')

                paginator = Paginator(residentdata,5)
                total_page= paginator.num_pages
                try:
                    residentdata = paginator.page(page)
                except PageNotAnInteger:
                    residentdata = paginator.page(1)
                except EmptyPage:
                    residentdata = paginator.page(paginator.num_pages)
                for residentdata in residentdata:
                    residentdata_list.append({
                        'id':residentdata.id,
                        'user_name':residentdata.username,
                        'mobile_number':residentdata.mobile_number,
                        'society_name':residentdata.society_request.society_name,
                        'tower':residentdata.society_request.tower,
                        'flat_no':residentdata.resident_request.flat_no,
                        'types':residentdata.resident_request.type,
                        'employee_name':residentdata.emp_request.name,
                        'employee_age':residentdata.emp_request.age,
                        'employee_mobile':residentdata.emp_request.emergency_no,
                        'service':residentdata.emp_request.service_provider,
                        'type':residentdata.emp_request.type,
                        'pay_amount':residentdata.pay_amount,
                        
                    })
                    
                return Response({'response':residentdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
            else:
                requestdata=Request_backup.objects.all()
                page = request.GET.get('page')

                paginator = Paginator(requestdata,5)
                total_page= paginator.num_pages
                try:
                    requestdata = paginator.page(page)
                except PageNotAnInteger:
                    requestdata = paginator.page(1)
                except EmptyPage:
                    requestdata = paginator.page(paginator.num_pages)
                requestdata_list=[]
                for requestdata in requestdata:
                    requestdata_list.append({
                        'user_name':requestdata.username,
                        'mobile_number':requestdata.mobile_number,
                        'society_name':requestdata.society_request.society_name,
                        'tower':requestdata.society_request.tower,
                        'flat_no':requestdata.resident_request.flat_no,
                        'types':requestdata.resident_request.type,
                        'employee_name':requestdata.emp_request.name,
                        'employee_age':requestdata.emp_request.age,
                        'employee_mobile':requestdata.emp_request.emergency_no,
                        'service':requestdata.emp_request.service_provider,
                        'type':requestdata.emp_request.type,
                        'pay_amount':requestdata.pay_amount,
                        
                        

                    })
                return Response({'request_replacement':requestdata_list,'total_pages':total_page,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def retrieve(self,request,pk=None):
        try:
            requestdata=Request_backup.objects.get(id=pk)
            # page = request.GET.get('page')

            # paginator = Paginator(requestdata,10)
            # total_page= paginator.num_pages
            # try:
            #     requestdata = paginator.page(page)
            # except PageNotAnInteger:
            #     requestdata = paginator.page(1)
            # except EmptyPage:
            #     requestdata = paginator.page(paginator.num_pages)
            request_data_list=[{
                # 'id':requestdata.id,
                'user_name':requestdata.username,
                'mobile_number':requestdata.mobile_number,
                # 'society_id':requestdata.society_request.id,
                'society_name':requestdata.society_request.society_name,
                'tower':requestdata.society_request.tower,
                # 'resident_id':requestdata.resident_request.id,
                'flat_no':requestdata.resident_request.flat_no,
                'types':requestdata.resident_request.type,
                # 'employee_id':requestdata.emp_request.id,
                'employee_name':requestdata.emp_request.name,
                'employee_age':requestdata.emp_request.age,
                'employee_mobile':requestdata.emp_request.emergency_no,
                'service':requestdata.emp_request.service_provider,
                'type':requestdata.emp_request.type,
                'pay_amount':requestdata.pay_amount,
                    
            }]
            return Response({'response':request_data_list,'success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
    def update(self,request,pk=None):
        try:
            employee_id=request.data.get('employee_id')
            if not employee_id:
                return Response({'response':'please enther the  employee_id','success':True,'status':status.HTTP_200_OK})
            employeedata=Employee.objects.get(id=employee_id)
            
            
            society_id=request.data.get('society_id')
            if not society_id:
                return Response({'response':'please enther the  society_id','success':True,'status':status.HTTP_200_OK})
            societydata=Society.objects.get(id=society_id)
            
            resident_id=request.data.get('resident_id')
            if not resident_id:
                return Response({'response':'please enther the  resident_id','success':True,'status':status.HTTP_200_OK})

            residentydata=Residents.objects.get(id=resident_id)
            
            username=request.data.get('username')
            if not username:
                return Response({'response':'please enther the  username','success':True,'status':status.HTTP_200_OK})
            pay_amount=request.data.get('pay_amount')
            if not pay_amount:
                return Response({'response':'please enther the  pay_amount','success':True,'status':status.HTTP_200_OK})
            mobile_number=request.data.get('mobile_number')
            if not mobile_number:
                return Response({'response':'please enther the  mobile_number','success':True,'status':status.HTTP_200_OK})

            requestdata=Request_backup.objects.get(id=pk)
            requestdata.emp_request=employeedata
            requestdata.society_request=societydata
            requestdata.resident_request=residentydata
            requestdata.username=username

            requestdata.pay_amount=pay_amount
            requestdata.mobile_number=mobile_number
            requestdata.save()
            return Response({'response':'updated successfully'})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
class ReportViewSet(viewsets.ViewSet):
    def list(self,request):
        try:
            type=request.GET.get('type')
            employee=request.GET.get('employee')
            payment=request.GET.get('payment')
            analysis=request.GET.get('analysis')
            society=request.GET.get('society')
            # name=request.GET.get('name')
            # month=request.GET.get('month')
            if type:
                residentdata=Residents.objects.filter(Q(type__icontains=type))
                page = request.GET.get('page')

                paginator = Paginator(residentdata,5)
                total_page= paginator.num_pages
                try:
                    residentdata = paginator.page(page)
                except PageNotAnInteger:
                    residentdata = paginator.page(1)
                except EmptyPage:
                    residentdata = paginator.page(paginator.num_pages)
                residentdata_list=[]
                for residentdata  in residentdata:
                    residentdata_list.append({
                        'id':residentdata.id,
                        'mobile_number':residentdata.mobile_number,
                        'total_family_member':residentdata.total_family_member,
                        'flat_no':residentdata.flat_no,
                        'flat_type':residentdata.flat_type,
                        'type':residentdata.type,
                        'agreement':residentdata.agreement,
                        'owner_name':residentdata.owner_name,
                        'owner_number':residentdata.owner_number,
                        'id_proof':residentdata.id_proof.url,
                        'city':residentdata.city,
                    })
                return Response({'resident_report_list':residentdata_list,'total_page':total_page,'success':True,'status':status.HTTP_200_OK})
            elif employee:
                
                employeedatasearch=Employee.objects.filter(Q(service_provider__icontains=employee))
                page = request.GET.get('page',)

                paginator = Paginator(employeedatasearch,2)
                total_page= paginator.num_pages
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    users = paginator.page(1)
                except EmptyPage:
                    users = paginator.page(paginator.num_pages)

                employeedatasearch_list=[]
                for employeedatasearch in employeedatasearch:
                    employeedatasearch_list.append({
                        'id':employeedatasearch.id,
                        'name':employeedatasearch.name,
                        'age':employeedatasearch.age,
                        'cuurent_Address':employeedatasearch.current_address,
                        'adhar_no':employeedatasearch.adhar_no,
                        'police_verfication,':employeedatasearch.police_verfication,
                        'service_provider':employeedatasearch.service_provider,
                        'type':employeedatasearch.type
                    })
                return Response({'employee_report':employeedatasearch_list,'total_no_of_pages':total_page,'message':True,'status':status.HTTP_200_OK})
            
            # elif month:
                
            #     attendancedata=Attendance.objects.filter(Q(employee__name=name)&Q(date_fields__month=month))
            #     attendancedata_list=[]
            #     total_present_day=0
            #     count=0
            #     present=0
            #     total_present=0
            #     total_absent=0
            #     absent=0
            #     for attendancedata in attendancedata:
            #         attendancedata_list.append({
            #             'id':attendancedata.id,
            #             'attandance':attendancedata.attandance,
            #             'date_fields':attendancedata.date_fields
            #         })
            #         if attendancedata.attandance=='p':
            #             present+=1
            #         else:
            #             absent+=1
            #         count+=1

            #     total_present_day+=count
            #     total_present+=present
            #     total_absent+=absent
            #     return Response({'response':attendancedata_list,'total_present_day':total_present_day,'total_present':total_present,'total_absent':total_absent})
            elif payment:
                requestbackup_data=Request_backup.objects.filter(Q(emp_request__name=payment))
                requestbackup_data_list=[]
                page = request.GET.get('page')

                paginator = Paginator(requestbackup_data,5)
                total_page= paginator.num_pages
                try:
                    requestbackup_data = paginator.page(page)
                except PageNotAnInteger:
                    requestbackup_data = paginator.page(1)
                except EmptyPage:
                    requestbackup_data = paginator.page(paginator.num_pages)
                print("pppppppp",requestbackup_data)
                total_payment=0
                for requestbackup_data in requestbackup_data:
                    requestbackup_data_list.append({
                        'id':requestbackup_data.id,
                        'employee_name':requestbackup_data.emp_request.name,
                        'employee_age':requestbackup_data.emp_request.age,
                        'employee_mobile':requestbackup_data.emp_request.emergency_no,
                        'service':requestbackup_data.emp_request.service_provider,
                        'type':requestbackup_data.emp_request.type,
                        'pay_amount':requestbackup_data.pay_amount,
                        
                    })
                    total_payment+=int(requestbackup_data.pay_amount)
                return Response({'payment_response':requestbackup_data_list,'total_payment':total_payment,'total_page':total_page,'message':True,'status':status.HTTP_200_OK})
            elif analysis:
                employeedatasearch=Employee.objects.filter(Q(name__icontains=analysis))
                page = request.GET.get('page',)

                paginator = Paginator(employeedatasearch,2)
                total_page= paginator.num_pages
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    users = paginator.page(1)
                except EmptyPage:
                    users = paginator.page(paginator.num_pages)

                employeedatasearch_list=[]
                for employeedatasearch in employeedatasearch:
                    employeedatasearch_list.append({
                        'id':employeedatasearch.id,
                        'name':employeedatasearch.name,
                        'age':employeedatasearch.age,
                        'cuurent_Address':employeedatasearch.current_address,
                        'adhar_no':employeedatasearch.adhar_no,
                        'police_verfication,':employeedatasearch.police_verfication,
                        'service_provider':employeedatasearch.service_provider,
                        'type':employeedatasearch.type
                    })
                return Response({'data_analysis':employeedatasearch_list,'total_no_of_pages':total_page,'message':True,'status':status.HTTP_200_OK})
            elif society:
                societydata=Society.objects.filter(Q(city__icontains=society))
                page = request.GET.get('page')
                

                paginator = Paginator(societydata,3)
                
                total_page= paginator.num_pages
                
                try:
                    societydatas = paginator.page(page)
                except PageNotAnInteger:
                    societydatas = paginator.page(1)
                except EmptyPage:
                    societydatas = paginator.page(paginator.num_pages)
                societydatasearch=[]

                
                for societydata in societydatas:
                    societydatasearch.append({

                        'society_name':societydata.society_name,
                        'sector_area':societydata.sector_area,
                        'city':societydata.city,
                        'state':societydata.state,
                        'pincode':societydata.pincode,
                        'no_of_towers':societydata.no_of_towers,
                        'tower':societydata.tower,
                    })
                return Response({'society_report':societydatasearch,'total_no_of_pages':total_page,'status':status.HTTP_200_OK,'message':True})
            else:
                return Response({'report_response':'please enter the filter query','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})







        
        
# class Generate_ReportViewSet(viewsets.ViewSet):
#     def list(self,request):
#         resident=request.GET.get('resident')
#         employee=request.GET.get('employee')
#         payment=request.GET.get('payment')

#         if resident:
#             report_data=Generate_Report.objects.filter(Q(society_generate__tower=resident))
#             residentsdata_list=[]
#             for reportdata in report_data:
#                 residentsdata_list.append({
#                'full_name':reportdata.resident_generate.residents.name,
#                'mobile_number':reportdata.resident_generate.mobile_number,
#                'total_family_member':reportdata.resident_generate.total_family_member,
#                'tower':reportdata.society_generate.tower,
#                'flat_no':reportdata.resident_generate.flat_no,
#                'flat_type':reportdata.resident_generate.flat_type,
#                'type':reportdata.resident_generate.type,
#                'agreement':reportdata.resident_generate.agreement,
#                'owner_name':reportdata.resident_generate.owner_name,
#                'owner_number':reportdata.resident_generate.owner_number,
#                'id_proof':reportdata.resident_generate.id_proof.url



#                 })
#             return Response({'response':residentsdata_list})
#         elif employee:
#             generate_employee=Generate_Report.objects.filter(Q(employee_generate__police_verfication=employee))
#             generate_employee_list=[]
#             for generate_employee in generate_employee:
#                 generate_employee_list.append({
#                     'name':generate_employee.employee_generate.name,
#                     'age':generate_employee.employee_generate.age,
#                     'current_address':generate_employee.employee_generate.current_address,
#                     'adhar_no':generate_employee.employee_generate.adhar_no,
#                     'police_verfication':generate_employee.employee_generate.police_verfication,
#                     'service_provider':generate_employee.employee_generate.service_provider,
#                     'type':generate_employee.employee_generate.type
#                 })
#             return Response({'response':generate_employee_list})
#         elif payment:
#             payment_employee=Generate_Report.objects.filter(Q(employee_generate__service_provider=payment))
#             payment_employee_list=[]
#             for generate_employee in payment_employee:
#                 payment_employee_list.append({
#                     'name':generate_employee.employee_generate.name,
#                     # 'age':generate_employee.employee_generate.age,
#                     # 'current_address':generate_employee.employee_generate.current_address,
#                     # 'adhar_no':generate_employee.employee_generate.adhar_no,
#                     # 'police_verfication':generate_employee.employee_generate.police_verfication,
#                     'service_provider':generate_employee.employee_generate.service_provider,
#                     'service_type':generate_employee.employee_generate.type,
#                     'flat_no':generate_employee.resident_generate.flat_no,
#                 })
#             return Response({'response':payment_employee_list})
#         else:
            
#             rreport_data=Generate_Report.objects.all()
#             residentsdata_list=[]
#             for reportdata in rreport_data:
#                 residentsdata_list.append({
#                'full_name':reportdata.resident_generate.residents.name,
#                'mobile_number':reportdata.resident_generate.mobile_number,
#                'total_family_member':reportdata.resident_generate.total_family_member,
#                'tower':reportdata.society_generate.tower,
#                'flat_no':reportdata.resident_generate.flat_no,
#                'flat_type':reportdata.resident_generate.flat_type,
#                'type':reportdata.resident_generate.type,
#                'agreement':reportdata.resident_generate.agreement,
#                'owner_name':reportdata.resident_generate.owner_name,
#                'owner_number':reportdata.resident_generate.owner_number,
#                'id_proof':reportdata.resident_generate.id_proof.url

#                 })
#             return Response({'response':residentsdata_list})
#     def create(self,request):
#         resident_id=Residents.objects.get(id=request.data.get('resident_id'))
#         society_id=Society.objects.get(id=request.data.get('society_id'))
#         employee_id=Employee.objects.get(id=request.data.get('employee_id'))
#         start_date=request.data.get('start_date')
#         end_date=request.data.get('end_date')
#         report=Generate_Report()
#         report.resident_generate=resident_id
#         report.society_generate=society_id
#         report.employee_generate=employee_id
#         report.start_date=start_date
#         report.end_date=end_date
#         report.save()
#         return Response({'response':'created data successfully'})



# class GenerateReportViewSet(viewsets.ViewSet):
#     def list(self,request):
#         residentdata=request.GET.get('resident')
#         empdata=request.GET.get('employee')
#         payment=request.GET.get('payment')
#         analysis=request.GET.get('analysis')
#         name=request.GET.get('name')
#         month=request.GET.get('month')
        
#         if residentdata:
#             report_data=GenerateReport.objects.filter(Q(society_generate__tower=residentdata))
#             residentsdata_list=[]
#             for reportdata in report_data:
#                 residentsdata_list.append({
#                'full_name':reportdata.resident_generate.residents.name,
#                'mobile_number':reportdata.resident_generate.mobile_number,
#                'total_family_member':reportdata.resident_generate.total_family_member,
#                'tower':reportdata.society_generate.tower,
#                'flat_no':reportdata.resident_generate.flat_no,
#                'flat_type':reportdata.resident_generate.flat_type,
#                'type':reportdata.resident_generate.type,
#                'agreement':reportdata.resident_generate.agreement,
#                'owner_name':reportdata.resident_generate.owner_name,
#                'owner_number':reportdata.resident_generate.owner_number,
#                'id_proof':reportdata.resident_generate.id_proof.url



#                 })
#             return Response({'generate_resident':residentsdata_list,'success':True,'status':status.HTTP_200_OK})
#         elif empdata:
#             generate_employee=GenerateReport.objects.filter(Q(employee_generate__service_provider=empdata))
#             generate_employee_list=[]
#             for generate_employee in generate_employee:
#                 generate_employee_list.append({
#                     'name':generate_employee.employee_generate.name,
#                     'age':generate_employee.employee_generate.age,
#                     'current_address':generate_employee.employee_generate.current_address,
#                     'adhar_no':generate_employee.employee_generate.adhar_no,
#                     'police_verfication':generate_employee.employee_generate.police_verfication,
#                     'service_provider':generate_employee.employee_generate.service_provider,
#                     'type':generate_employee.employee_generate.type
#                 })
#             return Response({'response':generate_employee_list,'success':True,'status':status.HTTP_200_OK})
#         elif name and month:
#             attendancedataname=GenerateReport.objects.filter(Q(attendance_generate__date_fields__month=month)&Q(attendance_generate__employee__name=name))
#             # page = request.GET.get('page')

#             # paginator = Paginator(attendancedataname,10)
#             # total_page= paginator.num_pages
#             # try:
#             #     attendancedataname = paginator.page(page)
#             # except PageNotAnInteger:
#             #     attendancedataname = paginator.page(1)
#             # except EmptyPage:
#             #     attendancedataname = paginator.page(paginator.num_pages)
#             attendancedataname_list=[]
#             total_days=0
#             present_days = 0
#             present_day = 0
#             absent_days=0
#             absentday=0
#             count=0
#             kkk=[]
#             for attendancedata in attendancedataname:
#                 if attendancedata.attendance_generate.attandance == 'p':
#                     present_days += 1
#                 elif attendancedata.attendance_generate.attandance == 'a':
#                     absent_days+=1
#                 else:
#                     pass
            
#                 attendancedataname_list.append({
#                     'id':attendancedata.id,
#                     'name':attendancedata.attendance_generate.employee.name,
#                     'attandance':attendancedata.attendance_generate.attandance,
#                     'month':attendancedata.attendance_generate.month,
#                     'date_fields':attendancedata.attendance_generate.date_fields,

#                 })
                    
#                 count+=1
#             total_days+=count
#             present_day+=present_days
#             absentday+=absent_days
#             dadalist=[{
#                 'attendance_details':attendancedataname_list,
#                     'present_day':present_day,
#                     'absent_days':absent_days,
#                     'total_days_count':total_days,
#                     'kkkkkkkk':kkk,
#             }]
#             return Response({'response':dadalist,'success':True,'status':status.HTTP_200_OK})
#         elif payment:
            
            
#             payment_employee=GenerateReport.objects.filter(Q(requestbackup_generate__emp_request__service_provider=payment))
#             payment_employee_list=[]
#             for generate_employee in payment_employee:
               
#                 payment_employee_list.append({
#                     'id':generate_employee.id,
#                     'username':generate_employee.requestbackup_generate.username,
#                     'service':generate_employee.requestbackup_generate.emp_request.service_provider,
#                     'service_type':generate_employee.requestbackup_generate.emp_request.type,
#                     'flat_type':generate_employee.requestbackup_generate.emp_request.flat_type,
#                     'present/absent':generate_employee.attendance_generate.attandance,
#                     'pay_amount':generate_employee.requestbackup_generate.pay_amount
#                 })
            
#             return Response({'response':payment_employee_list,'success':True,'status':status.HTTP_200_OK})
#         elif analysis:
#             # flat_no=request.GET.get('flat_no')
#             analysis=GenerateReport.objects.filter(Q(requestbackup_generate__emp_request__service_provider=analysis))
#             analysis_list=[]
#             for analysis in analysis:
#                 analysis_list.append({
#                     'flat_no':analysis.requestbackup_generate.resident_request.flat_no,
#                     'family_member':analysis.requestbackup_generate.resident_request.total_family_member,
#                     'service_provider':analysis.requestbackup_generate.emp_request.service_provider,
#                     'amount':analysis.requestbackup_generate.pay_amount,
                    
#                 })
#             return Response({'response':analysis_list,'success':True,'status':status.HTTP_200_OK})
#         else:
#             rreport_data=GenerateReport.objects.all()
#             residentsdata_list=[]
#             for reportdata in rreport_data:
#                 residentsdata_list.append({
#                 'full_name':reportdata.resident_generate.residents.name,
#                 'mobile_number':reportdata.resident_generate.mobile_number,
#                 'total_family_member':reportdata.resident_generate.total_family_member,
#                 'tower':reportdata.society_generate.tower,
#                 'flat_no':reportdata.resident_generate.flat_no,
#                 'flat_type':reportdata.resident_generate.flat_type,
#                 'type':reportdata.resident_generate.type,
#                 'agreement':reportdata.resident_generate.agreement,
#                 'owner_name':reportdata.resident_generate.owner_name,
#                 'owner_number':reportdata.resident_generate.owner_number,
#                 'id_proof':reportdata.resident_generate.id_proof.url
#                 })
#             return Response({'generate_reports':residentsdata_list,'success':True,'status':status.HTTP_200_OK})
#     def create(self,request):
#         try:

#             resident_id=Residents.objects.get(id=request.data.get('resident_id'))
#             society_id=Society.objects.get(id=request.data.get('society_id'))
#             employee_id=Employee.objects.get(id=request.data.get('employee_id'))
#             attend_id=Attendance.objects.get(id=request.data.get('attend_id'))
#             print('aaaaaaaaaaa',attendance_id)
#             requestbackup_id=Request_backup.objects.get(id=request.data.get('requestbackup_id'))

#             generatereport=GenerateReport()
#             generatereport.resident_generate=resident_id
#             generatereport.society_generate=society_id
#             generatereport.employee_generate=employee_id

#             generatereport.attendance_generate=attend_id
#             generatereport.requestbackup_generate=requestbackup_id
#             generatereport.start_date=request.data.get('start_date')
#             generatereport.end_date=request.data.get('end_date')
#             generatereport.save()
#             return Response({'response':'created data successfully','success':True,'status':status.HTTP_200_OK})
#         except Exception as error:
#             traceback.print_exc()
#             return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})