from django.contrib import messages
from django.shortcuts import render

# Create your views here.
import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from sims.models import User
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse


# Create your views here.
# 信息列表处理函数
# def index(request):
#     conn = pymysql.connect(host="118.31.60.105", user="FlightDB", passwd="flightdb", db="flightdb", port=3306)
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM User")
#         users = cursor.fetchall()
#         print(users)
#     return render(request, 'user/index.html', {'users': users})

#信息列表处理函数 django版本写法
def index(request):
    users = User.objects.all()
    print(type(users))
    return render(request,"user/index.html", locals())


def homepage(request):
    return render(request, "index.html", locals())

def authToast(request):
    messages.error(request,'无权限访问')
    # return render(request,'index.html')
    return HttpResponseRedirect('/')

# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'student/add.html')
    else:
        student_no = request.POST.get('student_no', '')
        student_name = request.POST.get('student_name', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO sims_student (student_no,student_name) "
                           "values (%s,%s)", [student_no, student_name])
            conn.commit()
        return redirect('../')

# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,student_no,student_name FROM sims_student where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'student/edit.html', {'student': student})
    else:
        id = request.POST.get("id")
        student_no = request.POST.get('student_no', '')
        student_name = request.POST.get('student_name', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE sims_student set student_no=%s,student_name=%s where id =%s",
                           [student_no, student_name, id])
            conn.commit()
        return redirect('../')

# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM sims_student WHERE id =%s", [id])
        conn.commit()
    return  redirect('../')
