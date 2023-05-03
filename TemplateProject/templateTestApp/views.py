from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    msg = "Hello Guest ...!!! Very very good "
    h = int(date.strftime('%H'))
    if h<12 :
        msg+="morning !!!"
    elif h<16 :
        msg+= "afternoon !!!"
    elif h < 21:
        msg+= "evening !!!"
    else :
        msg+= "night !!!"
    
    date_tag = {'insert_date':date,'insert_msg':msg}
    return render(request , 'testApp/wish.html',context=date_tag)