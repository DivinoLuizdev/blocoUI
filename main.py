import subprocess
import pyautogui
import time
import os

# Espera para evitar ações antes do Notepad abrir
time.sleep(1)

# Abre o bloco de notas
subprocess.Popen("notepad.exe")

# Aguarda o bloco de notas abrir
time.sleep(1)

# Escreve "Bom dia"
pyautogui.write("Bom dia")

# Faz o caminho do arquivo baseado na pasta do script
caminho = os.path.join(os.getcwd(), "bomdia.txt")

# CTRL + S para salvar
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

# Digita o caminho e salva
pyautogui.write(caminho)
time.sleep(1)

# Pressiona Enter para salvar
pyautogui.press('enter')

print(f"Arquivo salvo em: {caminho}")
