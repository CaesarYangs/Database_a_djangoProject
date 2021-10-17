
import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from airport.models import Airport
from aircompany.models import Aircompany
from django.contrib import messages
from airport.models import Flight
from aircompany.models import Plane

from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse

class aircompany:
    accode = ''

#信息列表处理函数 django版本写法
def index(request):
    aircompanies = Aircompany.objects.all()
    return render(request,"aircompany.html", locals())

def companyManage(request):
    aircompany.accode = request.GET.get("accode")
    company_flights = Flight.objects.filter(flightid__contains=aircompany.accode)
    return render(request, "companyflight.html", locals())

#机场进行航班票务信息管理
def ticketmanage(request):
    if request.method == 'GET':
        flight_id = request.GET.get("flightid")
        flight = Flight.objects.get(flightid=flight_id)
        return render(request,"aircompany/aircompany_ticket_manage.html",{'flight':flight})
    else:
        flight_id = request.POST.get("flightid", '')
        flight_name = request.POST.get("flight_name",'')
        flight_utime = request.POST.get("flight_utime", '')
        flight_dtime = request.POST.get("flight_dtime", '')
        flight_origin = request.POST.get("flight_origin", '')
        flight_destination = request.POST.get("flight_destination", '')
        flight_seatleft = request.POST.get("flight_seatleft", '')


        Flight.objects.filter(flightid=flight_id).update(flightname=flight_name)
        Flight.objects.filter(flightid=flight_id).update(seatleft=flight_seatleft)
        Flight.objects.filter(flightid=flight_id).update(origin=flight_origin)
        Flight.objects.filter(flightid=flight_id).update(destination=flight_destination)

        company_flights = Flight.objects.filter(flightid__contains=aircompany.accode)
        messages.success(request,'修改成功')
        return render(request, "companyflight.html", locals())


def addflight(request):
    if request.method == 'GET':
        return render(request,"aircompany/add_flight.html",{'accode':aircompany.accode})
    else:
        flight_id = request.POST.get("flightid", '')
        flight_planeid = request.POST.get("planeid",'')
        flight_name = request.POST.get("flight_name", '')
        flight_utime = request.POST.get("flight_utime", '')
        flight_dtime = request.POST.get("flight_dtime", '')
        flight_origin = request.POST.get("flight_origin", '')
        flight_destination = request.POST.get("flight_destination", '')
        flight_seatleft = request.POST.get("flight_seatleft", '')
        Flight.objects.create(flightid=flight_id,planeid=flight_planeid,flightname=flight_name,utime=flight_utime,dtime=flight_dtime,origin=flight_origin,destination=flight_destination,isdelay=0,seatleft=flight_seatleft)

        messages.success(request, '添加航班成功')
        company_flights = Flight.objects.filter(flightid__contains=aircompany.accode)
        return render(request, "companyflight.html", locals())

def planeManage(request):
    company_planes = Plane.objects.filter(companyid=aircompany.accode)
    return render(request, "aircompany/planes.html", locals())

def planesEdit(request):
    if request.method == 'GET':
        plane_id = request.GET.get("planeid")
        plane = Plane.objects.get(planeid = plane_id)
        return render(request,"aircompany/plane_manage.html",{'plane':plane})
    else:
        plane_planeid = request.POST.get("planeid",'')
        plane_companyid = request.POST.get("companyid",'')
        plane_planemodel = request.POST.get("planemodel",'')
        plane_name = request.POST.get("name",'')
        plane_npeople = request.POST.get("npeople",'')

        Plane.objects.filter(planeid=plane_planeid).update(companyid=plane_companyid)
        Plane.objects.filter(planeid=plane_planeid).update(planemodel=plane_planemodel)
        Plane.objects.filter(planeid=plane_planeid).update(name=plane_name)
        Plane.objects.filter(planeid=plane_planeid).update(npeople=plane_npeople)

        company_planes = Plane.objects.filter(companyid=aircompany.accode)
        messages.success(request,'修改成功')
        return render(request, "aircompany/planes.html", locals())

def addPlane(request):
    if request.method == 'GET':
        return render(request,"aircompany/add_plane.html",{'accode':aircompany.accode})
    else:
        plane_planeid = request.POST.get("planeid", '')
        plane_planemodel = request.POST.get("planemodel", '')
        plane_name = request.POST.get("name", '')
        plane_npeople = request.POST.get("npeople", '')

        Plane.objects.create(planeid = plane_planeid,companyid = aircompany.accode,planemodel=plane_planemodel,name=plane_name,npeople=plane_npeople)
        company_planes = Plane.objects.filter(companyid=aircompany.accode)
        messages.success(request,'添加飞机成功')
        return render(request, "aircompany/planes.html", locals())