import keyboard
import subprocess

palabra = []

def apagar_compu():
    palabra_escrita = "".join(palabra)
    palabras =  ["porno","xxx","porni","pornno","culos","sexo","tetas","teta"]

    for p in palabras:
      palabra_encontrada = palabra_escrita.find(p) 
      if palabra_encontrada !=  -1:
        subprocess.call(["shutdown", "/s", "/t", "0"])
        break 

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        print(f'Tecla presionada: {e.name}')
        if e.name == "backspace":
            if palabra: 
                palabra.pop()
        else:
            palabra.append(e.name)
            
            apagar_compu()

keyboard.hook(on_key_event)
keyboard.wait()