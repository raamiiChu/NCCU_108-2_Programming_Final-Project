import basic_mod  #導入模組
def back():
    print('='*40)
    global ask
    ask=input('若要返回主選單，輸入「0」\n若要繼續，請輸入任意字串:')

basic_mod.inport()
while True: 
    ask=''  #ask共用一個即可
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
        while ask!='0':
            basic_mod.write()
            back()
    elif question=='2':
        while ask!='0':
            basic_mod.search()
            back()
    elif question=='3':
        while ask!='0':
            basic_mod.rewrite()
            back()
    elif question=='4':
        while ask!='0':
            basic_mod.delete()
            back()

basic_mod.export()
