import xbmcgui
import xbmc
import xbmcaddon
import random
import os

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path')

#Lista de palabras
palabras = [
    {"en": "apple", "es": "manzana"},
    {"en": "burglar", "es": "ladrón"},
    {"en": "coal", "es": "carbón"},
    {"en": "coins", "es": "monedas"},
    {"en": "keyboard", "es": "teclado"},
    {"en": "keychain", "es": "llavero"},
    {"en": "ladybug", "es": "mariquita"},
    {"en": "lock", "es": "candado"},
    {"en": "puppy", "es": "cachorro"},
    {"en": "toadstool", "es": "seta"},
    {"en": "wolf", "es": "lobo"}
]

def reproducir_audio(nombre):
    """Reproduce un archivo de audio local."""
    ruta_sonido = os.path.join(addon_path, "resources", "sounds", f"{nombre}.mp3")
    if os.path.exists(ruta_sonido):
        xbmc.executebuiltin(f'PlayMedia("{ruta_sonido}")')

def mostrar_imagen(nombre):
    """Muestra la imagen correspondiente a la palabra."""
    ruta_img = os.path.join(addon_path, "resources", "images", f"{nombre}.jpg")
    if os.path.exists(ruta_img):
        win = xbmcgui.WindowDialog()
        img = xbmcgui.ControlImage(0, 0, 1280, 720, ruta_img)
        win.addControl(img)
        win.show()
        xbmc.sleep(2000)
        win.close()

dialog = xbmcgui.Dialog()
puntaje = 0

dialog.ok("Traductor ingles-español", "¡Bienvenido al juego de traducir palabras!")

for i in range(5):
    palabra = random.choice(palabras)
    mostrar_imagen(palabra['en'])
    reproducir_audio(palabra['en'])

    respuesta = dialog.input(f"Traduce al español: {palabra['en']}")
    if respuesta.lower().strip() == palabra['es']:
        puntaje += 1
        dialog.notification("Correcto", f"{palabra['en']} = {palabra['es']}", xbmcgui.NOTIFICATION_INFO, 1500)
    else:
        dialog.notification("Incorrecto", f"Era: {palabra['es']}", xbmcgui.NOTIFICATION_ERROR, 2000)

dialog.ok("Fin del juego", f"Tu puntación: {puntaje}/5")
