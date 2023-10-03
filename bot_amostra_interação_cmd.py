import pyautogui
from time import sleep

"""
Para rodar esse código é necessário ter o pyautogui instalado, pode ser feito isso com pip install pyautogui

O código tem um tempo de pausa maior para facilitar a visualização, em um caso de RPA do dia a dia, não teria essas pausas para otimização do código.

Além disso, é uma loja fictícia, então muitas funções estão limitadas e ainda podem ser desenvolvidas, essa código todo, bem como os outros arquvios foram criados apenas em um dia por ser um processo seletivo de urgência e necessidade de retorno rápida.
"""

# variaveis
nome_pasta = "gerenciador_recursos_mesha"

pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')

pyautogui.PAUSE = 2

# inicando a pesquisa da pasta
pyautogui.press('win')
pyautogui.write(nome_pasta)
pyautogui.press('enter')

# abrindo cmd
sleep(1)
x, y, largura, altura = pyautogui.locateOnScreen('locais_path.png')
sleep(1)

pyautogui.click((x + largura / 2), (y + altura / 2))
pyautogui.write("cmd")
pyautogui.press('enter')

# instalando pandas
pyautogui.write("pip install pandas")
pyautogui.press('enter')

# rodando código manipulando_site.py
pyautogui.write("python raw\manipulando_site.py")
pyautogui.press('enter')
sleep(2)

pyautogui.alert('Entrando no menu cliente')
# escolhendo menu clientes e listando produtos
pyautogui.write("1")
pyautogui.press('enter')
sleep(1)
pyautogui.alert('Validando as opções do menu cliente')
pyautogui.write("1") # Listar Produtos
pyautogui.press('enter')

sleep(2)
pyautogui.write("2") # Listar Meus Pedidos
pyautogui.press('enter')
pyautogui.write("1")
pyautogui.press('enter')

sleep(2)
pyautogui.write("3") # Listar Meus Pagamentos
pyautogui.press('enter')
pyautogui.write("1")
pyautogui.press('enter')

sleep(2)
pyautogui.write("4") # voltando ao menu inicial
pyautogui.press('enter')

sleep(1)
# voltando ao menu inicial e escolhendo o menu da loja e listar clientes
pyautogui.alert('Entrando no menu da loja')
pyautogui.write("2")
pyautogui.press('enter')
sleep(1)
pyautogui.alert('Validandoas opções do menu da loja')
sleep(2)
pyautogui.write("6") # Listar Clientes
pyautogui.press('enter')

pyautogui.write("7") # Listar Pedidos
pyautogui.press('enter')

pyautogui.write("8") # Listar produtos
pyautogui.press('enter')

sleep(2)
pyautogui.write("9") # Listar Pagamentos
pyautogui.press('enter')


sleep(2)
pyautogui.write("10") # Gerar Relatório
pyautogui.press('enter')

pyautogui.alert('Saindo...')
# saindo do programa
sleep(2)
pyautogui.write("11")
pyautogui.press('enter')
sleep(1)
pyautogui.write("3")
pyautogui.press('enter')


# fechando cmd
x, y, largura, altura = pyautogui.locateOnScreen('fechar_cmd.png')
pyautogui.click(x + largura / 2, y + altura / 2)


pyautogui.alert('O código terminou, ainda temos muitas melhorias pela frente. Obrigada!')