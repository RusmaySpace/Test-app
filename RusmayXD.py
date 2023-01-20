from colorama import *

init(autoreset=True)

def Pi():
  print()
  print(Fore.LIGHTRED_EX + "Вы выбрали: число пи.")
  print()
  print(Fore.RESET + "Число ПИ примерно равно: 3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989")
  print(Fore.LIGHTGREEN_EX + "И это еще ДАЛЕКО не конец, правда прикольно?)")
  print()
  P()
def Contacts():
  print()
  print("МОИ КОНТАКТЫ:")
  print()
  print(Fore.LIGHTBLUE_EX + "VK ", Fore.RESET + "— @rusmayxd")
  print(Fore.LIGHTMAGENTA_EX + "Discord ", Fore.RESET + "— RusmayXD#9626")
  print(Fore.LIGHTCYAN_EX + "Telegram ", Fore.RESET + "— Rusmay")
  print()
  P()
def P():
  print()
  print(Fore.RESET + "Команды:")
  print(Fore.RESET + "Чтоб вернуться в основное лобби, напишите — \"меню\".")
  print(Fore.RESET + "Хотите повторить запрос? Введите команду — \"повторить\".")
  print(Fore.RESET + "Если вы закончили работу, введите слово \"конец\" для закрытия программы.")
  print()
  end = str(input(Fore.RESET + "Что дальше? Введите команду: " + Fore.LIGHTRED_EX))
  if end in "меню":
    welcome()
  elif end in "повторить":   
    if Z in "1":
      Info()
    elif Z in "2":
      Disk()
    elif Z in "3":
      Pi()
    elif Z in "4":
      Contacts()
    else:
      print()
      print("Что-то пошло не так. Возможно вы ввели некорректный номер запроса или поставили лишний пробел.")
      print()
      G()
  elif end in "конец":
    print()
    print(Fore.LIGHTGREEN_EX + "Спасибо за тест моей программы, до новых встреч!")
    print()
  else:
    print()
    print(Fore.RED + "Я не понял вашу команду, возможно вы ошиблись в её написании, или поставили лишний пробел. Доступные команды: меню, повторить и конец.")
    print()
    print("Попробуйте еще раз!")
    P()
def G():
  Z = str(input(Fore.RESET + "Введите номер вашего запроса: " + Fore.CYAN))
  if Z in "1":
    Info()
  elif Z in "2":
    Disk()
  elif Z in "3":
    Pi()
  elif Z in "4":
    Contacts()
  else:
    print()
    print("Что-то пошло не так. Возможно вы ввели некорректный номер запроса или поставили лишний пробел.")
    print()
    G()
def Info():
  print()
  print(Fore.LIGHTRED_EX + "Вы выбрали: информацию о вас.")
  print()
  name = str(input("Введите ваше имя: " + Fore.CYAN))
  sex = str(input(Fore.RESET + "Теперь ваш пол (Р.П., полностью): " + Fore.CYAN))
  zodiac = str(input(Fore.RESET +"Ваш знак зодиака: " + Fore.CYAN))
  age = int(input(Fore.RESET + "Как насчет возраста (числом)? " + Fore.CYAN))
  print()
  print(Fore.YELLOW + "==========================================")
  print("Обработка информации")
  import time
  time.sleep(1)
  print("Обработка информации..")
  time.sleep(1)
  print("Обработка информации...")
  time.sleep(1)
  print(Fore.YELLOW + "==========================================")
  print()
  print("Вас зовут - " + name, end = '' ",")
  print(" вы " + sex, "пола.")
  print("Ваш знак зодиака - " + zodiac, end = '' "." )
  if (age%10 == 1):
    print(" Вам", + age, "год.")
  elif (age%10 == 2 and age != 12) or (age%10 == 4):
    print(" Вам", + age, "года.")
  else:
    print(" Вам", + age, "лет.")
    print()
  print()
  print(Fore.RESET + "Команды:")
  print(Fore.RESET + "Чтоб вернуться в основное лобби, напишите - \"меню\".")
  print(Fore.RESET + "Хотите повторить запрос? Введите команду — \"повторить\".")
  print(Fore.RESET + "Если вы закончили работу, введите слово \"конец\" для закрытия программы.")
  print()
  end = str(input(Fore.RESET + "Что дальше? Введите команду: " + Fore.LIGHTRED_EX))
  if end in "меню":
    welcome()
  elif end in "повторить":
    if Z in "1":
      Info()
    elif Z in "2":
      Disk()
    elif Z in "3":
      Pi()
    elif Z in "4":
      Contacts()
  elif end in "конец":
    print(Fore.LIGHTGREEN_EX + "Спасибо за тест моей программы, до новых встреч!")
  else:
    print()
    print(Fore.RED + "Я не понял вашу команду, возможно вы ошиблись в её написании, или поставили лишний пробел. Доступные команды: меню, повторить и конец.")
    print()
    print("Попробуйте еще раз!")
    P()

def Disk():
  print()
  print(Fore.LIGHTRED_EX + "Вы выбрали: расчет по формуле дискриминанта.")
  print()
  print("Напоминаю, формула дискриминанта выглядит следующим образом: D = b2 − 4ac")
  print()
  da = int(input(Fore.RESET + "Введите значение a: " + Fore.CYAN))
  db = int(input(Fore.RESET + "Введите значение b: " + Fore.CYAN))
  dc = int(input(Fore.RESET + "Введите значение c: " + Fore.CYAN))
  print()
  sum = (db**2 - 4 * da * dc)
  print("D = ", + sum)
  print()
  print(Fore.RESET + "Команды:")
  print(Fore.RESET + "Чтоб вернуться в основное лобби, напишите - \"меню\".")
  print(Fore.RESET + "Хотите повторить запрос? Введите команду — \"повторить\".")
  print(Fore.RESET + "Если вы закончили работу, введите слово \"конец\" для закрытия программы.")
  print()
  end = str(input(Fore.RESET + "Что дальше? Введите команду: " + Fore.LIGHTRED_EX))
  if end in "меню":
    welcome()
  elif end in "повторить":
    if Z in "1":
      Info()
    elif Z in "2":
      Disk()
    elif Z in "3":
      Pi()
    elif Z in "4":
      Contacts()
  elif end in "конец":
    print(Fore.LIGHTGREEN_EX + "Спасибо за тест моей программы, до новых встреч!")
  else:
    print()
    print(Fore.RED +"Я не понял вашу команду, возможно вы ошиблись в её написании, или поставили лишний пробел. Доступные команды: меню, повторить и конец.")
    print()
    print("Попробуйте еще раз!")
    P()
def welcome():
  print()
  print(Fore.LIGHTRED_EX + "v2.33 by RusmayXD")
  print()
  print("Доступные запросы:")
  print("1. Информация о вас.")
  print("2. Автоматический расчет по формуле дискриминанта.")
  print("3. Число Пи.")
  print("4. Мои контакты.")
  print()
  global Z
  Z = str(input(Fore.RESET + "Введите номер вашего запроса: " + Fore.CYAN))
  if Z in "1":
    Info()
  elif Z in "2":
    Disk()
  elif Z in "3":
    Pi()
  elif Z in "4":
    Contacts()
  else:
    print()
    print("Что-то пошло не так. Возможно вы ввели некорректный номер запроса или поставили лишний пробел.")
    print()
    G()
welcome()