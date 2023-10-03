import pyautogui
from time import sleep

# variaveis
nome_pasta = "gerenciador_recursos_mesha"

pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')

pyautogui.PAUSE = 1

# inicando a pesquisa da pasta
pyautogui.press('win')
pyautogui.write(nome_pasta)
pyautogui.press('enter')

# abrindo cmd
x, y, largura, altura = pyautogui.locateOnScreen('locais_path.png')
pyautogui.click(x + largura / 2, y + altura / 2)
pyautogui.write("cmd")
pyautogui.press('enter')

pyautogui.write("cd raw")
pyautogui.press('enter')

# instalando pandas
pyautogui.write("pip install pandas")
pyautogui.press('enter')

# instalando json
pyautogui.write("pip install json")
pyautogui.press('enter')

# # rodando código criando_bd_loja.py caso o db ainda não esteja criado no seu computador
# pyautogui.write("criando_bd_loja.py")
# pyautogui.press('enter')

# rodando código manipulando_site.py
pyautogui.write("python manipulando_site.py")
pyautogui.press('enter')

sleep(2)
# escolhendo menu clientes e listando produtos
pyautogui.write("1")
pyautogui.press('enter')
sleep(1)
pyautogui.write("1")
pyautogui.press('enter')

sleep(2)
# voltando ao menu inicial e escolhendo o menu da loja e listar clientes
pyautogui.write("4")
pyautogui.press('enter')
sleep(2)
pyautogui.write("2")
pyautogui.press('enter')
sleep(1)
pyautogui.write("5")
pyautogui.press('enter')

# saindo do programa
sleep(2)
pyautogui.write("10")
pyautogui.press('enter')
sleep(1)
pyautogui.write("3")
pyautogui.press('enter')


# fechando cmd
x, y, largura, altura = pyautogui.locateOnScreen('fechar_cmd.png')
pyautogui.click(x + largura / 2, y + altura / 2)


pyautogui.alert('O código terminou, ainda temos muitas melhorias pela frente. Obrigada!')