from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from pcalc.models import Pcalc_info
from .forms import Pcalc_infoForm
from .apps import PcalcConfig

def index(request): 
    form = Pcalc_infoForm()   
    return render(request, 'pcalc/data_form.html',{'form':form})

def calc(request): 
    request.POST.get("submit")
    m=''
    y1=''
    y2=''
    st1=''
    st2=''
    st3=''
    temp1=''
    temp2=''
    temp3=''
    mess=''
    mess2=''
    if request.method == 'POST':
        form = Pcalc_infoForm(request.POST or None)
        if form.is_valid():
            s = form.cleaned_data.get("sex")
            y1 = form.cleaned_data.get("year_born")
            y2 = form.cleaned_data.get("year_begin")
            st1 = form.cleaned_data.get("ts01")
            st2 = form.cleaned_data.get("ts91")
            st3 = form.cleaned_data.get("ts14")
            temp1= form.cleaned_data.get("szar2")
            temp2= form.cleaned_data.get("szar5")
            p1=(int(st1),int(st2),int(temp1),int(temp2)) # данные для периода до 2001
            temp1=''
            temp1=form.cleaned_data.get("szar14")
            p2=(int(st3),int(temp1)) # данные для периода 2002-2014
            # расчет возраста выхода на пенсию
            ap=(61,56) # пенсионный возраст на 2020 год
            apl=(50,45) # льготный пенсионный возраст по 1-му списку
            kyl=(1970,1975) # граничные года рождения по 1-му списку
            ky=((1959,1964),(1962,1967)) # граничные года рождения,
                 #попадающие в переходный период увеличения пенс. возраста
            y=int(y1)
            m=int(s)
            year=2020
            lg=[0,0,0,0,0] # флаги наличия льгот: северные (i=0,1), сельхоз (i=2), вредные производства(i=3,4)
            # извлекаем информацию о льготах по вредным спискам.
            temp1=''
            temp1=form.cleaned_data.get("stl1")
            if int(temp1)>=10-2.5*m: lg[3]=1
            temp1=''
            temp1=form.cleaned_data.get("stl2")
            if int(temp1)>=12.5-2.5*m: lg[4]=1
            if lg[3] or lg[4]:
                if lg[3]:
                    year=y+apl[m]
                    if y<kyl[m]: mess="Люди этого возраста уже вышли на пенсию по Первому списку!"
                    else:
                        mess="Возраст выхода на пенсию - "+str(apl[m])+" лет/года"
                        mess2="Год выхода на пенсию " + str(year)
                elif lg[4]:
                    year=y+apl[m]+5
                    if y<kyl[m]+5: mess="Люди этого возраста уже вышли на пенсию по Второму списку!"
                    else:
                        mess="Возраст выхода на пенсию - "+str(apl[m]+5)+" лет/года"
                        mess2="Год выхода на пенсию " + str(year)
            else:
                if y<ky[0][m]: mess="Люди этого возраста уже вышли на пенсию!"
                elif y>=ky[0][m] and y<=ky[1][m]:
                    mess="Возраст выхода на пенсию - "+str(ap[m]+y-ky[0][m])+" лет/года"
                    year=2020+2*(y-ky[0][m])  
                    mess2="Год выхода на пенсию " + str(year)
                else:
                    mess="Возраст выхода на пенсию - "+str(ap[m]+4)+" лет/года"
                    year=y+ap[m]+4 
                    mess2="Год выхода на пенсию " + str(year)
            st_15 = year-max(int(y2),2015) # стаж за период с 2015 года считается от года начала работы в периоде до года выхода на пенсию;
            temp1=''
            temp1=form.cleaned_data.get("szar15")
            temp2=''
            temp2=form.cleaned_data.get("sam")
            temp3 =form.cleaned_data.get("ssam") 
           
            # льготные баллы
            st1=''
            st1=form.cleaned_data.get("army")
            st_15-=float(st1) # вычитаем из стажа годы службы
            db=0
            db+=float(st1)*1.8; # доп. баллы за армию
            st1=''
            st1=form.cleaned_data.get("child")
            ch=min(int(st1),4)
            st_15-=ch*1.5 # вычитаем из стажа годы ухода за детьми
            if ch>0:
                for i in range(1, ch+1):
                    koef=min(i,3)   # за 4-го ребенка баллов как за третьего
                    db+=koef*1.8*1.5           # доп. баллы за детей
                
            st1=''
            st1=form.cleaned_data.get("other")
            st_15-=float(st1) # вычитаем из стажа годы ухода за инвалидами и лицами старше 80 лет
            p3=(st_15,int(temp1),int(temp2),int(temp3))# данные периода с 2015
            db+=float(st1)*1.8; # доп. баллы за уход
            db=round(db,2)
            # извлекаем информацию о северных и селхоз льготах
            temp1=''
            temp1=form.cleaned_data.get("stn1")
            if int(temp1)>=15: lg[0]=1
            temp1=''
            temp1=form.cleaned_data.get("stn2")
            if int(temp1)>=20: lg[1]=1
            temp1=''
            temp1=form.cleaned_data.get("sts")
            if int(temp1)>=30: lg[2]=1
            p=0
            pb=0
            stag=0
            mess3=""
            if mess2:    
                pensia_info=PcalcConfig.calc_pension(p1,p2,p3,year,db,lg,m)
                pb= round(pensia_info[0],1) # пенсионные баллы
                p = round(pensia_info[1],2) # размер пенсии
                stag = round(pensia_info[2],1)# общий трудовой/страховой стаж
                mess3= pensia_info[3]  # информация о невыполнении условий назначения пенсии (недостаточный стаж и/или мало пенсионных баллов)
            
            context= {'form': form, 'mess': mess, 'mess2': mess2, 'pb': pb,'p':p,'db': db, 'stag': stag,'mess3': mess3}
            return render(request, 'pcalc/resalt.html',context) 

        else:
            return HttpResponseNotAllowed(['POST'])
        
       
   

