# 導入 browser 的 document 及 html 物件
from browser import document, alert, console, load
load("https://cdnjs.cloudflare.com/ajax/libs/tone/14.7.3/Tone.js")
Tone = window.Tone




def action1(ev):
    alert("Hello !")
    print("Hello2 !")
    synth = new Tone.Synth().toMaster()
    //play music
    synth.triggerAttackRelease('C4', '8n')

document["box1"].bind("click", action1)