import pyfiglet
from termcolor import colored
import os
import time


textwelcome = pyfiglet.figlet_format("Sistema da qualidade do ar", width=100)
add = pyfiglet.figlet_format("Adicionar Amostra", width=100)
alter = pyfiglet.figlet_format("Alterar Amostra", width=100)
delete = pyfiglet.figlet_format("Excluir Amostra", width=100)
classificar = pyfiglet.figlet_format("Classificar Qualidade do Ar", width=100)
leave = pyfiglet.figlet_format("Saindo do sistema...", width=100)
optioninvalid = pyfiglet.figlet_format("Escolha invalida", width=100)
added = pyfiglet.figlet_format("Amostra adicionada", width=100)

initializationFirstStep = pyfiglet.figlet_format("Inicializando.", width=100)
initializationSecondStep = pyfiglet.figlet_format("Inicializando..", width=100)
initializationThirdStep = pyfiglet.figlet_format("Inicializando...", width=100)

print(colored(textwelcome, 'green', attrs=["bold", "blink"]))

systemOn = True

dbOn = False

while(dbOn == False):
  time.sleep(1)
  print(colored('Inicializando.', 'blue'))
  time.sleep(1)
  print(colored('Inicializando..', 'blue'))
  time.sleep(1)
  print(colored('Inicializando...', 'blue'))
  time.sleep(2)
  dbOn = True


while(systemOn):
  os.system('cls' if os.name == 'nt' else 'clear')


  print("------------MENU--------------")
  print()
  choice = int(input(
  """
      
  [1]: ADICIONAR AMOSTRA
  [2]: ALTERAR AMOSTRA
  [3]: EXCLUIR AMOSTRA
  [4]: CLASSIFICAR QUALIDADE DO AR
  [5]: SAIR

  ESCOLHA UMA OPÇÃO: """))

  if(choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(optioninvalid, 'white'))
    time.sleep(2)
  if(choice == 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(add, 'blue'))
    mp10 = int(input("INSIRA O VALOR DO MP10: "))
    mp25 = int(input("INSIRA O VALOR DO MP2,5: "))
    o3 = int(input("INSIRA O VALOR DO O3: "))
    co = int(input("INSIRA O VALOR DO CO: "))
    no2 = int(input("INSIRA O VALOR DO NO2: "))
    so2 = int(input("INSIRA O VALOR DO SO2: "))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(added, 'green'))
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
  if(choice == 2):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(alter, 'yellow'))
    teste = input("SELECIONE A AMOSTRA: ")
  if(choice == 3):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(delete, 'red', attrs=["bold"]))
    teste = input("SELECIONE A AMOSTRA: ")
  if(choice == 4):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(classificar, 'white'))

    mp10 = int(input("INSIRA O VALOR DO MP10: "))
    mp25 = int(input("INSIRA O VALOR DO MP2,5: "))
    o3 = int(input("INSIRA O VALOR DO O3: "))
    co = int(input("INSIRA O VALOR DO CO: "))
    no2 = int(input("INSIRA O VALOR DO NO2: "))
    so2 = int(input("INSIRA O VALOR DO SO2: "))

    if(mp10 > 0 and mp10 <= 50 and mp25 > 0 and mp25 <= 25 and o3 > 0 and o3 <= 100 and co > 0 and co <= 9 and no2 > 0 and no2 <= 200 and so2 > 0 and so2 <= 20):
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Qualidade do ar está", colored("boa", 'green'))
      time.sleep(2)
    if (mp10 > 50 and mp10 <= 100 and mp25 > 25 and mp25 <= 50 and o3 > 100 and o3 <= 130 and co > 9 and co <= 11 and no2 > 200 and no2 <= 240 and so2 > 20 and so2 <= 40 ):
      os.system('cls' if os.name == 'nt' else 'clear')
      print ("Qualidade do ar está", colored("moderada", 'light_yellow' ))
      print("""
  
      Pessoas de grupos sensiveis (crianças, idosos e
      pessoas com doenças respiratórias e cardiacas)
      podem apresentar sintomas como tosse seca e
      cansaço. A população, em geral, não é afetada.
      """)
      time.sleep(7)
    if (mp10 > 100 and mp10 <= 150 and mp25 > 50 and mp25 <= 75 and o3 > 130 and o3 <= 160 and co > 11 and co <= 13 and no2 > 240 and no2 <= 320 and so2 > 40 and so2 <= 365 ):
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Qualidade do ar está", colored("ruim", 'yellow' ))
      print("""
  
      Toda a população pode apresentar sintomas como
      tosse seca, cansaço, ardor nos olhos, nariz e
      garganta. Pessoas de grupos sensiveis (crianças,
      idosos e pessoas com doenças respiratórias e cardiacas)
      podem apresentar efeitos mais sérios na saúde.
      """)
      time.sleep(7)
    if (mp10 > 150 and mp10 <= 250 and mp25 > 75 and mp25 <= 125 and o3 > 160 and o3 <= 200 and co > 13 and co <= 15 and no2 > 320 and no2 <= 1130 and so2 > 365 and so2 <= 800 ):
      os.system('cls' if os.name == 'nt' else 'clear')
      print ("Qualidade do ar está", colored("muito ruim", 'red' ))
      print("""
  
      Toda a população pode apresentar agravamento dos
      sintomas como tosse seca, cansaço, ardor nos alhos,
      nariz e garganta e ainda falta de an e respiração
      ofegante. Efeitos ainda mais graves à saúde de
      grupos sensiveis (crianças, idosos e pessoas com
      doenças respiratórias e cardiacas).
      """)
      time.sleep(7)
    if (mp10 > 250 and mp25 > 125 and o3 > 200 and co > 15 and no2 > 1130 and so2 > 800):
      os.system('cls' if os.name == 'nt' else 'clear')
      print ("Qualidade do ar está", colored("péssima", 'magenta' ))
      print("""
  
      Toda a população pode apresentar agravamento dos
      sintomas como tosse seca, cansaço, ardor nos alhos,
      nariz e garganta e ainda falta de an e respiração
      ofegante. Efeitos ainda mais graves à saúde de
      grupos sensiveis (crianças, idosos e pessoas com
      doenças respiratórias e cardiacas).
      """)
      time.sleep(7)
  if(choice == 5):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(leave, 'red'))
    systemOn = False