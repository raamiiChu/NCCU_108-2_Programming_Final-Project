import datetime#導入datetime模組
import pickle    #導入pickle模組
                 
#pickle模組參考網址
#https://clay-atlas.com/blog/2020/03/28/%e4%bd%bf%e7%94%a8-pickle-%e6%a8%a1%e7%b5%84%e4%bf%9d%e5%ad%98-python-%e8%b3%87%e6%96%99/
#https://morvanzhou.github.io/tutorials/python-basic/basic/13-08-pickle/

#list1=[]行程
#list2=[]日期
#list3=[]種類
#list4=[]跟誰
#dict1={}行程:[日期]
#dict2={}日期:[行程]

#種類字典
#ct1={}日期:[工作行程]
#ct2={}日期:[學業行程]
#ct3={}日期:[娛樂行程]
#ct4={}日期:[其他行程]

'''檢查用
    print(dict1)
    print(dict2)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(ct1)
    print(ct2)
    print(ct3)
    print(ct4)
'''
#日期:國立節日
dict3={'0101':'元旦','0228':'和平紀念日','0401':'愚人節','0501':'勞動節',\
       '0808':'父親節','0928':'教師節','1010':'國慶日','1031':'萬聖節',\
       '1225':'行憲紀念日','0308':'婦女節','0329':'青年節',\
       '1025':'臺灣光復節','1112':'國父誕辰紀念日'}
#行程類別
dict4={'工作':'ct1', '學業':'ct2', '娛樂':'ct3', '其他':'ct4'}

def inport():#讀取檔案
    try:#檢查全部檔案是否存在(可讀取)
        #建立字典、串列
        with open('dict1.pickle','rb') as file:
            global dict1
            dict1=pickle.load(file)
        with open('dict2.pickle','rb') as file:
            global dict2
            dict2=pickle.load(file)
        with open('list1.pickle','rb') as file:
            global list1
            list1=pickle.load(file)
        with open('list2.pickle','rb') as file:
            global list2
            list2=pickle.load(file)
        with open('list3.pickle','rb') as file:
            global list3
            list3=pickle.load(file)
        with open('list4.pickle','rb') as file:
            global list4
            list4=pickle.load(file)
        with open('ct1.pickle','rb') as file:
            global ct1
            ct1=pickle.load(file)
        with open('ct2.pickle','rb') as file:
            global ct2
            ct2=pickle.load(file)
        with open('ct3.pickle','rb') as file:
            global ct3
            ct3=pickle.load(file)
        with open('ct4.pickle','rb') as file:
            global ct4
            ct4=pickle.load(file)
    except:#若不行，建立新檔案
        dict1=dict2=ct1=ct2=ct3=ct4={}
        list1=list2=list3=list4=[]
        export()
        inport()
    
def export():#輸出檔案
    with open('dict1.pickle', 'wb') as file:
        pickle.dump(dict1,file)
    with open('dict2.pickle', 'wb') as file:
        pickle.dump(dict2,file)
    with open('list1.pickle', 'wb') as file:
        pickle.dump(list1,file)
    with open('list2.pickle', 'wb') as file:
        pickle.dump(list2,file)
    with open('list3.pickle', 'wb') as file:
        pickle.dump(list3,file)
    with open('list4.pickle', 'wb') as file:
        pickle.dump(list4,file)
    with open('ct1.pickle', 'wb') as file:
        pickle.dump(ct1,file)
    with open('ct2.pickle', 'wb') as file:
        pickle.dump(ct2,file)
    with open('ct3.pickle', 'wb') as file:
        pickle.dump(ct3,file)
    with open('ct4.pickle', 'wb') as file:
        pickle.dump(ct4,file)
    

def print_dict2date(x):#打印訊息用的
    for i in dict2[x]:
        print('\t'*2,i)

def check_dict3(date):#判斷是否為節日
    ax=str(date.month) #屬性:月
    ay=str(date.day)   #屬性:天
    if len(str(date.month))==1: #若月為個位數，前方補'0' ex.1 -> 01
        ax='0'+str(date.month)
    if len(str(date.day))==1:   #若日為個位數，前方補'0' ex.9 -> 09
        ay='0'+str(date.day)
    if ax+ay in dict3:          #若該日期有在字典中，因出對應節日
        print(dict3[ax+ay])
        

#判定輸入的日期是否正確，之後要判斷日期可以直接用這個函數(date=check_date())
def check_date():
    print('='*60)
    year=input("請輸入要編輯的年份:")
    while True:
        try:                            
            datetime.date(int(year),1,1)
            #判斷輸入的年份是否符合曆法
        except:
            year=input("輸入錯誤，請輸入要編輯的年份:")
            continue
        else:
            break
    month=input("請輸入要編輯的月份:")  
    while not month.isdigit() or int(month)>12 or int(month)<1:
        #判斷輸入的月份是否符合曆法
        month=input("輸入錯誤，請輸入要編輯的月份:")
    day=input("請輸入要編輯的日子:")
    while True:
        try:                            
            datetime.date(int(year),int(month),int(day))
            #判斷輸入的日子是否符合曆法
        except:
            day=input("輸入錯誤，請輸入要編輯的日子:")
            continue
        else:
            break
    return datetime.date(int(year),int(month),int(day))#回傳日期

def write():#寫入
    date=check_date() #判定輸入的日期是否正確
    print('='*50)
    check_dict3(date) #將日期帶入，判斷是否為節日
    print(date,'行程:',dict2.get(date,'無'))
    print('='*50)
    thing=str(input("請寫入您要記錄的事項:"))
    category=str(input("請輸入您的行程種類，1=工作, 2=學業, 3=娛樂, 4=其他："))

    while True: #檢查機制
        if category=="1" or category=="2" or category=="3" or category=="4":
            break
        else:
            category=str(input("請重新輸入您的行程種類，1=工作, 2=學業, 3=娛樂, 4=其他："))
            
    who=str(input("請寫入此事項的關係人，若沒有請直接輸入Enter:"))#人
    
    if category=="1":
        try:
            ct1[date].append(thing)#檢查字典中是否已經有該key值
        except:
            ct1[date]=[thing]#沒有則新增
           
    if category=="2":
        try:
            ct2[date].append(thing)
        except:
            ct2[date]=[thing]
           
    if category=="3":
        try:
            ct3[date].append(thing)
        except:
            ct3[date]=[thing]
                
    if category=="4":
        try:
            ct4[date].append(thing)
        except:
            ct4[date]=[thing]

    try:
        dict2[date].append(thing)
    except:
        dict2[date]=[thing]

    try:
        dict1[thing].append(date)
    except:
        dict1[thing]=[date]
    finally:
        if category == "1" :
            category = "工作"
        elif category == "2" :
             category = "學業"
        elif category == "3" :
             category = "娛樂"
        elif category == "4" :
            category = "其他"
        list1.append(thing)     #在串列中增加行程
        list2.append(date)      #在串列中增加日期
        list3.append(category)  #在串列中增加種類
        list4.append(who)       #在串列中增加關係人
        print('='*50)
        print('已將行程排入')
        print(date,':')
        print_dict2date(date)#將日期帶入函數

def search():#查詢
    print(dict1)
    print(dict2)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(ct1)
    print(ct2)
    print(ct3)
    print(ct4)
    print('='*60)
    asksearch=input('輸入要查詢的項目(0:行程,1:日期,2:種類,3:關係人)：')
    while asksearch!='0' and asksearch!='1' and asksearch!='2' and asksearch!='3': #檢查機制
        asksearch=input('輸入錯誤(0:行程,1:日期,2:種類,3:關係人)：?')
    if asksearch=='0': #查詢該行程在哪一天
        search=str(input('輸入要查詢的行程:'))
        print('='*60)
        if list1.count(search)>=1: #檢查串列中是否有該行程
            people=[i for i,x in enumerate(list1) if x==search]
            
            for i in people :
                print("-"*30)
                print("行程為：",list1[i])
                print("日期為：",list2[i])
                print("種類為：",list3[i])
                print("跟誰：",list4[i])
                print("-"*30)    
        else:
            print(search,': 查無此行程')
    elif asksearch=='1':  #查詢當天有哪些行程
        date=check_date() #判定輸入的日期是否正確
        print('='*60)
        check_dict3(date) #將日期帶入，判斷是否為節日
        try:
            dict2[date]
        except:
            print(date,':','無行程')
        else:
            if int(len(dict2[date]))==0:  #避免有行程被刪除後導致的空串列
                print(date,':','無行程')
            else:
                print(date,':')
                print_dict2date(date) #將日期帶入函數，印出訊息
    elif asksearch=='2':
        sel=str(input("請輸入您查詢的行程種類，1=工作, 2=學業, 3=娛樂, 4=其他："))
        while True:
            if sel=="1" or sel=="2" or sel=="3" or sel=="4": #檢查機制
                break
            else:
                sel=str(input("請重新輸入查詢的行程種類，1=工作, 2=學業, 3=娛樂, 4=其他："))
        if sel=="1" and len(ct1)>=1:
            for date,thing in ct1.items(): #日期、行程
                if thing==[]: #避免空串列
                    continue
                else:
                    print(date,'的行程：',', '.join(thing))
                    #印出該種類的所有對應行程
        elif sel=="2" and len(ct2)>=1:
            for date,thing in ct2.items():
                if thing==[]:
                    continue
                else:
                    print(date,'的行程：',', '.join(thing))
        elif sel=="3" and len(ct3)>=1:
            for date,thing in ct3.items():
                if thing==[]:
                    continue
                else:
                    print(date,'的行程：',', '.join(thing))
        elif sel=="4" and len(ct4)>=1:#檢查串列中是否有該行程
            for date,thing in ct4.items():
                if thing==[]:
                    continue
                else:
                    print(date,'的行程：',', '.join(thing))
        else:
            print('無行程')
    if asksearch=='3': #查詢相關關係人
        search=str(input('輸入關係人:'))
        print('='*60)
        if list4.count(search)>=1: #檢查串列中是否有該行程
            people=[i for i,x in enumerate(list4) if x==search]
            
            for i in people :
                print("-"*30)
                print("行程為：",list1[i])
                print("日期為：",list2[i])
                print("種類為：",list3[i])
                print("跟誰：",list4[i])
                print("-"*30)    
        else:
            print(search,': 查無此人')

def rewrite():#修改
    date=check_date() #判定輸入的日期是否正確
    print('='*60)
    check_dict3(date) #將日期帶入，判斷是否為節日
    print('當日行程:',dict2.get(date,'查無資料'))
    try:
        dict2[date]
    except:
        print('無資料可修改')
    else:
        askchange=input('是否修改(0:是,1:否)?')
        while askchange!='0' and askchange!='1':
            askchange=input('輸入錯誤(0:是,1:否)?')
        if askchange=='0': 
            try:
                rewrite_change=input('輸入要刪除的行程:')
                dict2[date].remove(rewrite_change) #測試是否能移除
            except:
                print('無此行程，請再次輸入:') #不行，代表沒有該行程
            else: 
                rewrite_thing=input('輸入要新增的行程:')#可以，繼續修改(dict2已移除行程)
                rewrite_ct=input("請輸入修改後的行程種類，1=工作, 2=學業, 3=娛樂, 4=其他：")
                while rewrite_ct!="1" and rewrite_ct!="2" and rewrite_ct!="3" and rewrite_ct!="4":
                    rewrite_ct=input("請重新輸入您的行程種類，1=工作, 2=學業, 3=娛樂, 4=其他：")
                rewrite_who=input('請寫入此事項的關係人，若沒有請直接輸入Enter:')
                #刪除字典中的行程串列的對應索引值
                if dict4.get(list3[list1.index(rewrite_change)])=='ct1':
                    del ct1[date][ct1[date].index(rewrite_change)]
                elif dict4.get(list3[list1.index(rewrite_change)])=='ct2':
                    del ct2[date][ct2[date].index(rewrite_change)]
                elif dict4.get(list3[list1.index(rewrite_change)])=='ct3':
                    del ct3[date][ct3[date].index(rewrite_change)]
                elif dict4.get(list3[list1.index(rewrite_change)])=='ct4':
                    del ct4[date][ct4[date].index(rewrite_change)]

                #新增新的行程種類
                if rewrite_ct=='1':
                    try:
                        ct1[date].append(rewrite_thing)
                    except:
                        ct1[date]=[rewrite_thing]
                elif rewrite_ct=='2':
                    try:
                        ct2[date].append(rewrite_thing)
                    except:
                        ct2[date]=[rewrite_thing]
                elif rewrite_ct=='3':
                    try:
                        ct3[date].append(rewrite_thing)
                    except:
                        ct3[date]=[rewrite_thing]
                elif rewrite_ct=='4':
                    try:
                        ct4[date].append(rewrite_thing)
                    except:
                        ct4[date]=[rewrite_thing]
                        
                list2.remove(date)                 #把日期移到最後面
                list2.append(date)
                
                del list3[list1.index(rewrite_change)] #刪除list3的種類
                if rewrite_ct == "1" :#新增更改後的種類
                    list3.append('工作')
                elif rewrite_ct == "2" :
                    list3.append('學業')
                elif rewrite_ct == "3" :
                    list3.append('娛樂')
                elif rewrite_ct == "4" :
                    list3.append('其他')

                del list4[list1.index(rewrite_change)] #刪除list4的關係人
                list4.append(rewrite_who)          #新增更改後的關係人
                list1.remove(rewrite_change)       #list1移除
                list1.append(rewrite_thing)        #加在list1串列最後方
                dict1[rewrite_change].remove(date) #移除dict1的日期
                dict2[date].append(rewrite_thing)  #加在dict2串列最後方
                try: #同樣是寫入行程，故與write函數中的功能相同
                    dict1[rewrite_thing]
                except:
                    dict1[rewrite_thing]=[date]
                else:
                    dict1[rewrite_thing].append(date) #加在dict1串列最後方
                print('修改成功')
                print('='*60)
                print(date,':')
                print_dict2date(date)#將日期帶入函數
        else:
            print('取消修改')

def delete():#刪除
    date=check_date() #判定輸入的日期是否正確
    print('='*60)
    check_dict3(date) #將日期帶入，判斷是否為節日
    print('當日行程:',dict2.get(date,'查無資料'))
    try:
        dict2[date] #檢查當天是否有行程
    except:
        print('無資料可刪除') #沒有則直接結束
    else:
        askdel=input('是否刪除(0:是,1:否)?') #詢問是否要刪除
        while askdel!='0' and askdel!='1':
            askdel=input('輸入錯誤(0:是,1:否)?')
        if askdel=='0': #確定刪除
            askdel_2=input('刪除數量(0:全部,1:一個)?')
            while askdel_2!='0' and askdel_2!='1':
                askdel_2=input('輸入錯誤(0:全部,1:一個)?')
            if askdel_2=='0': #刪除全部
                for x in dict2[date]:
                                             #利用索引值刪除
                    del list2[list1.index(x)]#刪除串列中的日期
                    del list3[list1.index(x)]#刪除串列中的種類
                    del list4[list1.index(x)]#刪除串列中的跟誰
                    del list1[list1.index(x)]#刪除串列中的行程
                    #list1一定要在最後刪除，否則前三行會因找不到索引值而刪除失敗
                for y in dict2[date]: #移除行程對應的日期(可能會留下空串列)
                    dict1[y].remove(date)
                for x in dict2[date]: #刪除種類字典的對應值
                                      #當天可能有多個行程，故用for迴圈
                    while True:
                        try:
                            del ct1[date] #嘗試是否能刪除，不論成功與否皆結束迴圈
                        except:
                            break
                        else:
                            break
                    while True:
                        try:
                            del ct2[date]
                        except:
                            break
                        else:
                            break
                    while True:
                        try:
                            del ct3[date]
                        except:
                            break
                        else:
                            break
                    while True:
                        try:
                            del ct4[date]
                        except:
                            break
                        else:
                            break
                del dict2[date] #刪除當日所有行程
                print('刪除成功')
                   
            else: #刪除一個
                while True:
                    delete=str(input('請選擇你要刪除的事項:'))
                    try:
                        dict2[date].remove(delete) #嘗試是否可移除
                        dict1[delete].remove(date)        
                    except:
                        print('查無此行程')
                        continue
                    else:
                        #尋找該行程是哪個種類
                        if dict4.get(list3[list1.index(delete)])=='ct1':
                            del ct1[date][ct1[date].index(delete)]
                            #刪除字典中的行程串列的對應索引值
                        elif dict4.get(list3[list1.index(delete)])=='ct2':
                            del ct2[date][ct2[date].index(delete)]
                        elif dict4.get(list3[list1.index(delete)])=='ct3':
                            del ct3[date][ct3[date].index(delete)]
                        elif dict4.get(list3[list1.index(delete)])=='ct4':
                            del ct4[date][ct4[date].index(delete)]
                                                      #利用索引值刪除
                        del list2[list1.index(delete)]#刪除串列中的日期
                        del list3[list1.index(delete)]#刪除串列中的種類
                        del list4[list1.index(delete)]#刪除串列中的跟誰
                        del list1[list1.index(delete)]#刪除串列中的行程
                        #list1一定要在最後刪除，否則前三行會因找不到索引值而刪除失敗
                        print('='*60)
                        print('刪除成功')
                        print(date,':')
                        print_dict2date(date) #將日期帶入函數
                        break
        else: #取消刪除
            print('取消刪除')
    
