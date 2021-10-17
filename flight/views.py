from audioop import reverse

import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from flight.models import Flight
from flight.models import Ticket
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse


#信息列表处理函数 django版本写法
def index(request):
    flights = Flight.objects.all()
    print(type(flights))
    return render(request,"bookflight.html", locals())

def testadd(request):
    Flight.objects.create(flightid='CA003',planeid='001')
    return index(request)

def myticket(request):
    username = request.session['username']
    tickets = Ticket.objects.filter(userid=username)
    for i in range(len(tickets)):
        check = Flight.objects.filter(flightid=tickets[i].flightid)
        # if(check is not None):
        if check[0].isdelay and check[0].isdelay!=None:
            messages.error(request,'您预订的航班{}已发出延误提醒 请注意'.format(check[0].flightid))
        # if(check[0]):
        #     print("delay detected")
    return render(request, "tickets.html", locals())

def bookTicket(request):
    if request.method == 'GET':
        isVip = request.session['isVip']
        flight_id = request.GET.get("flightid")
        return render(request, 'booking.html', {'flightid': flight_id,'isVip':isVip})
    else:
        username = request.session['username']
        flight_id = request.POST.get("flightid",'')
        booking_name = request.POST.get("booking_name",'')
        booking_num = request.POST.get("booking_num",'')
        check = Flight.objects.filter(flightid=flight_id)
        isVip = request.session['isVip']
        print(check[0].seatleft)
        print(type(booking_num))
        if check[0].seatleft==None or int(check[0].seatleft) < int(booking_num) :
            messages.error(request,'余票不足 请重新确认订票数量')
            return redirect('/flight/')
        else:
            Flight.objects.filter(flightid = flight_id).update(seatleft = check[0].seatleft-int(booking_num))
            if isVip:
                tmoney = 2000*0.9
            else:
                tmoney = 2000
            Ticket.objects.create(userid=username, flightid=flight_id, money=tmoney,airportid=check[0].origin)  # 数据库增加操作
            messages.success(request,'订票成功')
        return redirect('/flight/myticket/')

def delTicket(request):
    del_id = request.GET.get("ticketid")
    Ticket.objects.filter(ticketid = del_id).delete()   #操作数据库 删除操作
    messages.success(request,'删除成功')
    return redirect('/flight/myticket/')

