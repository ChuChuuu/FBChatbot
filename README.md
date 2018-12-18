# 鴨肉飯寵物機器人
* 沒事可以餵餵他，叫他幫你想想等一下要吃什麼
* 將程式藉由heroku部署在雲端上，所以不需要在本機端開著server
## FSM diagram
![](https://i.imgur.com/bidCF86.png)

## How to run and interact with the chatbot
會有按鈕提示選項，也可以手動輸入
* 首先第一次打開機器人畫面會有歡迎畫面
![](https://i.imgur.com/aPsTM1V.png)
* 按下開始後
![](https://i.imgur.com/vYKRxZ0.png)
* 輸入“介紹你自己”會說自己會做什麼
![](https://i.imgur.com/hGchJFv.png)
* “帶我去粉專後”會有連結按下後傳送至粉專
![](https://i.imgur.com/iTZsJ8Q.png)
* “想吃東西嗎”會告訴你現在的飽足度（一百為上限），並且選不同食物餵他會有不同飽足度增加
![](https://i.imgur.com/8UrLwLO.png)
    * 可以選取食物
![](https://i.imgur.com/69fO50y.png)
    * 若是超過一百時
![](https://i.imgur.com/gvNgTf7.png)
    * 不想餵食可以打“算了”
![](https://i.imgur.com/2JvKYvb.png)
* 也可以叫他幫你決定你等等要吃啥，飽足度不夠則需要先餵飽她
![](https://i.imgur.com/x6JDtgQ.png)
    * 飽足度夠時會跟你說現在飽足度剩多少並且可以新增刪除清單，選“就這樣吧”會幫你選出你該吃什麼
![](https://i.imgur.com/Nil9r7o.png)
        * 新增與刪除（已新增為例），不能新增已經有的也不能刪除沒有的
![](https://i.imgur.com/1lEV63E.png)
        * 新增已有時，不允許
![](https://i.imgur.com/QyY0TaI.png)
        * 要幫你選時輸入“就這樣吧”，則幫你選出一個
![](https://i.imgur.com/iFYm2UW.png)
    * 飽足度不夠時會要你先餵飽
![](https://i.imgur.com/fPc4hLt.png)
    * 也可以選不要好了，則取消
![](https://i.imgur.com/IHh0GD2.png)
