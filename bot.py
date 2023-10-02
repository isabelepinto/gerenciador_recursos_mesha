import pyautogui
import time

# variaveis
nome_pasta = "gerenciador_recursos_mesha"

pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')

pyautogui.PAUSE = 1

# inicando a pesquisa da pasta
pyautogui.press('win')
pyautogui.write(nome_pasta)
pyautogui.press('enter')

