# 導入 browser 的 document 及 html 物件
# from browser import document, alert, console, load

# tone = window.Tone




# def action1(ev):
#     alert("Hello !")
#     print("Hello2 !")
#     synth = new tone.Synth().toMaster()
#     //play music
#     synth.triggerAttackRelease('C4', '8n')

# document["box1"].bind("click", action1)


from browser import document, window

THREE = window.THREE

camera = THREE.PerspectiveCamera.new(75, 1, 1, 10000)
camera.position.z = 1000
scene = THREE.Scene.new()
geometry = THREE.CubeGeometry.new(200, 200, 200)
material = THREE.MeshBasicMaterial.new({"color": "#ff0000", "wireframe": True})
mesh = THREE.Mesh.new(geometry, material)
scene.add(mesh)

renderer = THREE.WebGLRenderer.new()
renderer.setSize(444, 444)

document <= renderer.domElement
renderer.render(scene, camera)

def animate(i):
    # note: three.js includes requestAnimationFrame shim
    window.requestAnimationFrame(animate)

    mesh.rotation.x += 0.01
    mesh.rotation.y += 0.02

    renderer.render(scene, camera)   

animate(0)