from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_page_message
from utils import send_three_template
from utils import send_two_template
import random

full = 40
foodtype = 0
#foodlist = ["飯","麵","湯","橘子","柳丁"]
foodlist = ["麥當勞","肯德基","西提"]
def choosefood():
    global foodlist
    if len(foodlist) > 0:
        thefood = random.sample(foodlist,1)
        restr = "你就吃 "+thefood[0]+" 吧"
    elif len(foodlist) == 0:
        restr = "沒東西啦，耍我！"
    return restr

def listallfood():
    restr = "你的食物清單裡有:\n"
    for food in foodlist:
        restr = restr + food+"\n"
    return restr

def deleteafood(food):
    global foodlist
    if foodlist.count(food) > 0:
        foodlist.remove(food)
        return 1
    elif foodlist.count(food) == 0:
        return 0

def appendafood(food):
    global foodlist
    if foodlist.count(food) > 0:
       return "清單裡面已經有了啦吼！"
    elif foodlist.count(food) == 0:
       foodlist.append(food)
       return "新增好囉！"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
#state1
    def user_misunderstand(self,event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower() != 'go to state1':
                print ("asdasdasd")
                sender_id = event['sender']['id']
                response = send_text_message(sender_id,"我聽不懂你的意思喔")
               
 
    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
#        sender_id = event['sender']['id']
#        response = send_text_message(sender_id,"我聽不懂你的意思喔")
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

#about
    def is_going_to_about(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹你自己'
        return False

    def on_enter_about(self, event):
        print("I'm entering about")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "我就是一隻鴨肉飯")
        send_three_template(sender_id,"不過你可以試著問我","帶我去你的粉專吧","想吃東西嗎","幫我想我等等要吃什麼")
        self.go_back()    
		
    def on_exit_about(self):
        print('Leaving about')

#startmsg
    def is_going_to_startmsg(self,event):
        if event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '開始使用'
        return False

    def on_enter_startmsg(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "嘗試跟我說些什麼吧")
        self.go_back()

    def on_exit_startmsg(self):
        print('Leaving startmsg')
#page
    def is_going_to_page(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '帶我去你的粉專吧'
        elif event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '帶我去你的粉專吧'

        return False

    def on_enter_page(self, event):
        print("I'm entering page")
        sender_id = event['sender']['id']
        responese = send_page_message(sender_id, "好啊但是沒有任何東西吧嘻嘻")
        self.go_back()

    def on_exit_page(self):
        print('Leaving page')
#eating
    def is_going_to_eating(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '想吃東西嗎'
        elif event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '想吃東西嗎'

        return False

    def on_enter_eating(self, event):
        global full
        print("I'm eating page")
        sender_id = event['sender']['id']
        responese = send_three_template(sender_id, "我現在飽足度"+str(full)+",快餵我吃呀,你要餵我吃...(鍵入“算了”以取消)","蘋果","可樂","義大利麵")


    def on_exit_eating(self,event):
        print('Leaving eating')

    def noeating(self,event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == '算了':
                sender_id = event['sender']['id']
                response = send_text_message(sender_id,"太過分了，你是要讓我餓到吃自己嗎？")
                return True
        return False
#eating2
    def is_going_to_eating2(self,event):
        global foodtype
        global foodname
        if event.get("message"):
            foodname = event['message']['text']
            if foodname.lower() == '蘋果':
                foodtype = 1
                return True
            elif foodname.lower() == '可樂':
                foodtype = 2
                return True
            elif foodname.lower() == '義大利麵':
                foodtype = 3
                return True
        elif event.get("postback"):
            foodname = event['postback']['title']
            if foodname.lower() == '蘋果':
                foodtype = 1
                return True
            elif foodname.lower() == '可樂':
                foodtype = 2
                return True
            elif foodname.lower() == '義大利麵':
                foodtype = 3
                return True


        return False

    def on_enter_eating2(self, event):
        global foodtype
        global full
        global foodname
        print("I'm eating2")
        sender_id = event['sender']['id']
        print(foodtype)        
        if foodtype == 1:
            full+=40
        elif foodtype == 2:
            full+=20
        elif foodtype == 3:
            full+=50

        if full >= 100:
            full = 100
            responese = send_text_message(sender_id,"我已經吃飽了啦，飽足度"+str(full))
        else:
            responese = send_text_message(sender_id,foodname+"也太好吃了吧，我的飽足度已經增加到 "+str(full)+" 了喔")
        self.go_back()
#        self.go_back()

    def on_exit_eating2(self):
        print('Leaving eating2')
#meal
    def is_going_to_meal(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '幫我想我等等要吃什麼'
        elif event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '幫我想我等等要吃什麼'

        return False

    def on_enter_meal(self, event):
        global full
        print("I'm entering meal")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"現在飽足度："+str(full))
        responese = send_two_template(sender_id, "確定要嗎？幫你想可是需要消耗我能量的（飽足度-50)","要","不要好了")
    
    def on_exit_meal(self,event):
        print('Leaving meal')

    def nowantmeal(self,event):
        print("in meal test")
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == '不要好了':
                sender_id = event['sender']['id']
                response = send_text_message(sender_id,"好！你自己說的！")
                return True
            elif text.lower() == '要' and full < 50:
                sender_id = event['sender']['id']
                response = send_text_message(sender_id,"我還在餓肚子啦!")
                return True
        if event.get("postback"):
            text = event['postback']['title']
            if text.lower() == '不要好了':
                sender_id = event['sender']['id']
                response = send_text_message(sender_id,"好！你自己說的！")
                return True
            elif text.lower() == '要' and full < 50:
                sender_id = event['sender']['id']
                response = send_text_message(sender_id,"我還在餓肚子啦!")
                return True

        return False
#meallist       
    def is_going_to_meallist(self,event):
        global full
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == '要' and full >= 50:
                full -= 50
#                send_id = event['sender']['id']
#                response = send_text_message(sender_id,"我的飽足度只剩"+str(full)+"喔")
                return True
        elif event.get("postback"):
            text = event['postback']['title']
            if text.lower() == '要' and full >= 50:
                full -= 50
#                send_id = event['sender']['id']
#                response = send_text_message(sender_id,"我的飽足度只剩"+str(full)+"喔")

                return True

        return False

    def on_enter_meallist(self, event):
        global full
        print("I'm entering meallist")
        sender_id = event['sender']['id']
        sendstr = listallfood()
        responese = send_text_message(sender_id,"飽足度："+str(full)+"\n"+sendstr)
        responese = send_three_template(sender_id, "你要？","新增","刪除","就這樣吧")
    
    def on_exit_meallist(self,event):
        print('Leaving meallist')
    
    def listthatok(self,event):
        print("in meallist test")
        if event.get("message"):
            text = event['message']['text']
            if text.lower() == '就這樣吧':
                sender_id = event['sender']['id']
                sendstr = choosefood()
                print(sendstr)
                response = send_text_message(sender_id,str(sendstr))
                return True 
        if event.get("postback"):
            text = event['postback']['title']
            if text.lower() == '就這樣吧':
                sender_id = event['sender']['id']
                sendstr = choosefood()
                print(sendstr)
                response = send_text_message(sender_id,str(sendstr))
                return True 
        return False
#addmeallist
    def is_going_to_addmeallist(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '新增'
        elif event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '新增'

        return False

    def on_enter_addmeallist(self, event):
        print("I'm entering addmeallist")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"接著輸入你要增加的東東!")
    
    def on_exit_addmeallist(self,event):
        print('Leaving addmeallist')

    def addafood(self,event):
        global foodlist
        print("in addmeallist test")
        if event.get("message"):
            text = event['message']['text']
            sender_id = event['sender']['id']
            sendstr = appendafood(text)
            response = send_text_message(sender_id,sendstr)
            return True                                                     
        return False

#delmeallist
    def is_going_to_delmeallist(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '刪除'
        elif event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '刪除'

        return False

    def on_enter_delmeallist(self, event):
        print("I'm entering delmeallist")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"接著輸入你要刪除的東東!")
    
    def on_exit_delmeallist(self,event):
        print('Leaving delmeallist')

    def delafood(self,event):
        print("in delmeallist test")
        if event.get("message"):
            text = event['message']['text']
            sender_id = event['sender']['id']
            if deleteafood(text) > 0:
                response = send_text_message(sender_id,"刪除掉囉")
                return True
            elif deleteafood(text) == 0:
                response = send_text_message(sender_id,"清單裡沒有耶，確認一下吧！")
                return True                                                     
        return False


