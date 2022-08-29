import basic_mod  #導入模組
import tkinter
from tkinter import messagebox
def back():
    while True:
        win = tkinter.Tk() #產生主視窗
        win.title('詢問')
        win.geometry('0x0')
        global ask
        ask=messagebox.askquestion('詢問','是否返回主選單？') #跳出詢問訊息框
        try:        
            win.destroy()        #點擊完後主視窗自動關閉        
        except:
            continue             
        else:
            break
    

basic_mod.inport()     #匯入資料(名稱用import會搞混，所以改inport)
while True: 
    ask=''  
    print('='*70)
    print('1:寫入行程\n2:查詢行程\n3:修改行程\
          \n4:刪除行程\n0:結束')
    question=input('輸入想要執行的項目:')
    while question!='0' and question!='1' and question!='2'\
          and question!='3' and question!='4':     #若要新增功能，這裡要記得改
        question=input('輸入有誤，請輸入「0~4」:') #「」內也要改
    if question=='0':
        break
    elif question=='1':
        while ask!='yes':
            basic_mod.write()   #寫入
            back()
    elif question=='2':
        while ask!='yes':
            basic_mod.search()  #查詢
            back()
    elif question=='3':
        while ask!='yes':
            basic_mod.rewrite() #修改
            back()
    elif question=='4':
        while ask!='yes':
            basic_mod.delete()  #刪除
            back()
basic_mod.export() #輸出資料
