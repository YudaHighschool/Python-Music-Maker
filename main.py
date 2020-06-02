# 導入 browser 的 document 及 html 物件
from browser import document, alert, console

def action1(ev):
    alert("Hello !")
    print("Hello2 !")

document["box1"].bind("click", action1)
document["box1"].bind("click", lambda ev: print("Hellox !"))


