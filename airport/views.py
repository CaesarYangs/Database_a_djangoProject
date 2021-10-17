
import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from airport.models import Airport
from airport.models import Flight
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse

class airport:
    airportcode = ''


#信息列表处理函数 django版本写法
#进入机场管理首页 展示数据库表中的全部机场列表
def index(request):
    airports = Airport.objects.all()
    return render(request,"airports.html", locals())

#机场管理函数 点击对应链接进入各自的机场航班管理界面
def airportManagement(request):
    airport.airportcode = request.GET.get("airportcode")
    airport_flights = Flight.objects.filter(origin=airport.airportcode)|Flight.objects.filter(destination=airport.airportcode)
    return render(request, "airportflight.html", locals())

#选定给定的航班 机场发送延误通知
def sendDelayMessage(request):
    flight_id = request.GET.get("flightid")
    Flight.objects.filter(flightid=flight_id).update(isdelay=1)
    airport_flights = Flight.objects.filter(origin=airport.airportcode) | Flight.objects.filter(destination=airport.airportcode)
    messages.success(request,'航班延误提醒发送成功 所有订单均会受到提醒')
    return render(request, "airportflight.html", locals())

#选定给定的航班 机场发送取消延误通知
def cancelDelayMessage(request):
    flight_id = request.GET.get("flightid")
    Flight.objects.filter(flightid=flight_id).update(isdelay=0)
    airport_flights = Flight.objects.filter(origin=airport.airportcode) | Flight.objects.filter(destination=airport.airportcode)
    messages.success(request,'航班延误取消成功 所有订单均会受到提醒')
    return render(request, "airportflight.html", locals())

#机场发送对应的取消航班通知
def cancelFlight(request):
    flight_id = request.GET.get("flightid")
    Flight.objects.filter(flightid=flight_id).delete()
    airport_flights = Flight.objects.filter(origin=airport.airportcode) | Flight.objects.filter(destination=airport.airportcode)
    messages.success(request,'航班已取消')
    return render(request, "airportflight.html", locals())

#机场进行航班票务信息管理
def ticketmanage(request):
    if request.method == 'GET':
        flight_id = request.GET.get("flightid")
        flight = Flight.objects.get(flightid=flight_id)
        return render(request,"airport/airport_ticket_manage.html",{'flight':flight})
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
        airport_flights = Flight.objects.filter(origin=airport.airportcode) | Flight.objects.filter(destination=airport.airportcode)
        messages.success(request,'航班票务信息修改成功')
        return render(request, "airportflight.html", locals())