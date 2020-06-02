# 導入 browser 的 document 及 html 物件
from browser import document, alert

def action1(ev):
    alert("Hello !")

document["box1"].bind("click", action1)


