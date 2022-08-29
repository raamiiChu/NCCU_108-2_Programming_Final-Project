list1=[]#行程
dict1={}#行程:[日期]
dict2={}#日期:[行程]
dict3={'0101':'元旦','0211':'除夕','0212':'春節開始','0216':'春節結束','0226':'元宵節',\
       '0228':'和平紀念日','0401':'愚人節','0404':'清明節+兒童節','0501':'勞動節','0509':'母親節',\
       '0614':'端午節','0808':'父親節','0921':'中秋節','0928':'教師節','1010':'國慶日',\
       '1031':'萬聖節','1225':'行憲紀念日','0301':'和平記念日補假','0308':'婦女節','0329':'青年節',\
       '0402':'兒童節補假','0430':'勞動節補假','0822':'中元節','0920':'中秋節補假','1011':'國慶日補假',\
       '1014':'重陽節','1025':'臺灣光復節','1112':'國父誕辰紀念日','1221':'冬至','1231':'元旦補假','0621':'夏至',}#日期:節日
'''print(list1) #這三行可用於檢查
        print(dict1)
        print(dict2)'''
#判定輸入的資料是否正確，之後要判斷日期可以直接用這個函數(date=check_date())
def check_date():
    print('='*60)
    date=input("請選擇要編輯的日期(格式:月份日期,XXOO):")
    while True:
        if len(date)!=4 or (not date.isdigit()):
            date=input('請輸入四位數的日期:')
        elif int(date[0:2])<1 or int(date[0:2])>12:
            date=input('不存在的日期，請重新輸入:')
        elif (date[0:2]=='01' or date[0:2]=='03' or date[0:2]=='05'\
            or date[0:2]=='07'or date[0:2]=='08' or date[0:2]=='10'\
            or date[0:2]=='12') and (int(date[2:4])>31 or int(date[2:4])<1):
            date=input('不存在的日期，請重新輸入:')
        elif (date[0:2]=='04' or date[0:2]=='06' or date[0:2]=='09'\
            or date[0:2]=='11') and (int(date[2:4])>30 or int(date[2:4])<1):
            date=input('不存在的日期，請重新輸入:')
        elif date[0:2]=='02' and (int(date[2:4])>29 or int(date[2:4])<1):
            date=input('不存在的日期，請重新輸入:')
        else:
            break
    return date


def write():
    date=check_date()
    if date in dict3:#判斷是否為節日
        n=dict3[date]
        print(n)
    print('當日行程:',dict2.get(date,'無'))
    print('='*50)
    thing=str(input("請寫入您要記錄的事項:"))
    try:
        dict2[date]#檢查字典中是否已經有該key值
    except:
        dict2[date]=[thing]#沒有則新增
    else:
        dict2[date].append(thing)#有則附加上去

    try:
        dict1[thing]#與上一個同樣原理
    except:
        dict1[thing]=[date]
    else:
        dict1[thing].append(date)
    finally:
        list1.append(thing)#在行程串列中增加行程
        print('已將行程排入',dict2.get(date))
        

def search():#查詢
    print('='*60)
    asksearch=input('輸入要查詢的項目(0:行程,1:日期)')
    while asksearch!='0' and asksearch!='1':
        asksearch=input('輸入錯誤(0:行程,1:日期)?')
    if asksearch=='0':
        search=str(input('輸入要查詢的行程:'))
        #字典不能用count，所以改用串列
        if list1.count(search)>=1:#檢查串列中是否有該行程
            print(search,':')
            for date in dict1[search]:
                print('\t',date)
        else:
            print(search,': 查無此行程')
    else:
        date=check_date()
        if date in dict3:#判斷是否為節日
            n=dict3[date]
            print(n)
        try:
            dict2[date]
        except:
            print(date,':','無行程')
        else:
            if int(len(dict2[date]))==0:
                print(date,':','無行程')
            else:
                print(date,':')
                for thing in dict2[date]:
                    print('\t',thing)

def rewrite():
    date=check_date()
    if date in dict3:#判斷是否為節日
        n=dict3[date]
        print(n)
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
                rewrite_change=input('輸入要刪除的行程')
                dict2[date].remove(rewrite_change) #測試是否能移除
            except:
                print('無此行程，請再次輸入') #不行，代表沒有該行程
            else: 
                rewrite_thing=input('輸入要新增的行程')#可以，繼續修改(dict2已移除行程)
                list1.remove(rewrite_change)       #list1移除
                list1.append(rewrite_thing)        #加在list1串列最後方
                dict1[rewrite_change].remove(date) #移除dict1
                dict2[date].append(rewrite_thing)  #加在dict2串列最後方
                try: #同樣是寫入行程，故與write函數中的功能相同
                    dict1[rewrite_thing]
                except:
                    dict1[rewrite_thing]=[date]
                else:
                    dict1[rewrite_thing].append(date) #加在dict1串列最後方
                print('修改成功')
        else:
            print('取消修改')


def delete():
    date=check_date()
    if date in dict3:#判斷是否為節日
        n=dict3[date]
        print(n)
    print('當日行程:',dict2.get(date,'查無資料'))
    try:
        dict2[date]
    except:
        print('無資料可刪除')
    else:
        askdel=input('是否要刪除(0:是,1:否)?')
        while askdel!='0' and askdel!='1':
            askdel=input('輸入錯誤(0:是,1:否)?')
        if askdel=='0':
            askdel_2=input('刪除數量(0:全部,1:一個)?')
            while askdel!='0' and askdel!='1':
                askdel_2=input('輸入錯誤(0:全部,1:一個)?')
            if askdel_2=='0': #刪除全部
                for x in dict2[date]:
                    del list1[list1.index(x)]#刪除串列中的行程
                for y in dict2[date]: #移除行程對應的日期(可能會留下空串列)
                    dict1[y].remove(date)
                del dict2[date]#刪除當日所有行程
            else: #刪除一個
                delete=str(input('請選擇你要刪除的事項:'))
                try:
                    dict2[date].remove(delete)
                    dict1[delete].remove(date)
                    del list1[list1.index(delete)]
                except:
                    print('查無此行程')
                else:
                    print('刪除成功')
                    print('刪除後的行程:',dict2[date])
        else:
            print('取消刪除')

