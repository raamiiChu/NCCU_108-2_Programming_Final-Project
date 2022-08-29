list1=[]#行程
dict1={}#行程:[日期]
dict2={}#日期:[行程]
def delete():
    date=input("請選擇要刪除的日期(格式:月份日期,XXOO):")
    while True:#判定輸入的資料是否正確
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
            for x in dict2[date]:
                del list1[list1.index(x)]
            for y in dict2[date]: 
                dict1[y].remove(date)
            del dict2[date]
            print('刪除成功')
        else:
            print('取消刪除')
def write():
    print('='*60)
    date=input("請選擇要編輯的日期(格式:月份日期,XXOO):")
    while True:#判定輸入的資料是否正確
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

    print('當日行程:',dict2.get(date,'無'))
    print('='*50)
    thing=str(input("請寫入您要記錄的事項:"))
    try:
        dict2[date]
    except:
        
        dict2[date]=[thing]
    else:
        
        dict2[date].append(thing)

    try:
        dict1[thing]
    except:
        dict1[thing]=[date]
    else:
        dict1[thing].append(date)
    finally:
        list1.append(thing)        
        print('已將行程排入',dict2.get(date))
        
        '''print(list1) #這三行用於檢查
        print(dict1)
        print(dict2)'''

def search():
    print('='*60)
    search=str(input('輸入要查詢的行程:'))
    #字典不能用count，所以改用串列
    if list1.count(search)>=1:
        print(search,':')
        for date in dict1[search]:
            print('\t',date)
    else:
        print(search,': 查無此行程')
    
while True:
    ask=-1
    print('='*70)
    print('1:寫入行程\n2:查詢行程\n\n3:刪除行程0:結束')
    question=input('輸入想要執行的項目:')
    while question!='0' and question!='1' and question!='2' and question!='3':
        question=input('輸入有誤，請輸入「0~3」:')
    if question=='0':
        break
    elif question=='1':
        while ask!='0':
            write()
            print('='*40)
            ask=input('若要返回主選單，輸入「0」\n若要繼續，請輸入任意字串:')
    elif question=='2':
        while ask!='0':
            search()
            print('='*40)
            ask=input('若要返回主選單，輸入「0」\n若要繼續，請輸入任意字串:')
    elif question=='3':
        while ask!='0':
            delete()
            print('='*40)
            ask=input('若要返回主選單，輸入「0」\n若要繼續，請輸入任意字串:')
    
