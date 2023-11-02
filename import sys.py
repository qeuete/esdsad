import os
import json
import csv

def create_save(): #создание сохр.джсон
    save_data = {}
    print("Создание нового сохранения")
    name = input("Введите ваше имя: ")
    date = input("Введите дату: ")
    Vibor1 = input("Введите свой первый выбор: ")
    Vibor2 = input("Введите свой второй выбор: ")
    Vibor3 = input("Введите свой третий выбор: ")
    Vibor4 = input("Введите свой четвертый выбор: ")

    save_data["name"] = name
    save_data["date"] = date
    save_data["Vibor1"] = Vibor1
    save_data["Vibor2"] = Vibor2
    save_data["Vibor3"] = Vibor3
    save_data["Vibor4"] = Vibor4

    with open("save.json", "w") as file:
        json.dump(save_data, file)
    print("Сохранение успешно")

def load_save(): #загрузка сохранения
    try:
        with open("save.json", "r") as file:
            save_data = json.load(file)

        print("Имя: " + save_data["name"])
        print("День недели: " + save_data["date"])
        print("Выбор из первой главы: " + save_data["Vibor1"])
        print("Выбор из второй главы: " + save_data["Vibor2"])
        print("Выбор из третьей главы: " + save_data["Vibor3"])
        print("Выбор из четвертой главы: " + save_data["Vibor4"])
    except FileNotFoundError:
        print("Данного сохранения не существует")       

def delete_save(): #удаление сохранения
    try:
        os.remove("save.json")
        print("Сохранение успешно удалено!")
    except FileNotFoundError:
        print("Данного сохранения не существует")     

def write_to_csv():   #ссв
    headers = ["Name", "date", "Vibor1", "Vibor2", "Vibor3", "Vibor4"]
    if os.path.isfile("save.csv"):
        with open("save.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            with open("save.json", "r") as json_file:
                data = json.load(json_file)
                writer.writerow([data["name"], data["date"], data["Vibor1"], data["Vibor2"], data["Vibor3"], data["Vibor4"]])
    else:
        with open("save.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            with open("save.json", "r") as json_file:
                data = json.load(json_file)
                writer.writerow([data["name"], data["date"], data["Vibor1"], data["Vibor2"], data["Vibor3"], data["Vibor4"]])



def gm_choice(option):
    print ("Выберите один из вариантов")
    for i, option in enumerate (option):
        print(f"{i+1}.{option}")
    while True:
        try:
            choice = int (input(" "))
            if choice < 1 or choice > len (option):
                print ("Выберите допустимый вариант")
            else:
                return choice 
        except ValueError:
            print(" ")
def main():
    print("Добро пожаловать в игру!")
    action = input("Выберите действие: \n1.Создать новое сохранение \n2.Загрузить сохранение \n3.Удалить сохранение \n4.Записать данные в CSV файл \n")
    if action == "1":
        create_save()
    elif action == "2":
        load_save()
    elif action == "3":
        delete_save()
    elif action == "4":
        write_to_csv()
    else:
        print("Неверный выбор!")
        main()

    
    def coffe():
        print("-Вы идете на кухню с одной мыслью: \"быстрее бы взбодриться\"")
        print ("-Вы вставляете капсулы в кофемашину и ждете.\n-5 минут и кофе готов!")
        print("-Попивая кофе, вы думаете, чем бы заняться сегодня.")

    def chai():
        print("-Вы идете на кухню с одной мыслью: \"быстрее бы взбодриться\"")
        print ("-Вы завариваете любимый чай и пьете")
        print("-Попивая чай, вы думаете, чем бы заняться сегодня.")
        
    def dota():
        print("-Вы заходите на локалки в дискорде и ищите тиммейтов.\n-Спустя 5 минут сборов, ваша команда заходит в доту и запускает первую катку.")
        print("-Первая игра закончилась довольно быстро, вы даже не успели насладиться")
        print("-Поэтому решаетесь регнуть еще одну катку,но она тоже заканчивается довольно быстро.")
        print("-Вам это надоело и вы думаете, чем же можно еще заняться")
    def progylka():
        print("-Вы вышли на улицу.\n-Солнце светило ярко, птички громко пели, на небе было ни облачка, все было прекрасно.")
        print("-Сначала вы решили прогуляться в парке, после чего пошли музей, где вам рассказали нобычные истории.После этого вы направились к озеру, где покормили уточек.")
        print("-Прогулка была утомительной, поэтому вы зашли перекусить в кафе. Там вы думали, как съездить бы вам в магазин за новыми вещами")

    def domashka():
        print("-Вы решили заняться домашним заданием. Вы садитесь за стол и начинаете выполнять задания.")
        print("-Вы быстренько управляетесь с домашнем заданием.")
        print("-После этого вы думаете о том, чем себя занять.") 
    def metro():
        print("-Вы идете к ближайшему метро")
        print("-Внутри слышны прекрасные звуки.\n-Вы идете на этот звук и видите, что это музыканты утроили концерт.")
        print("-Постояв  и послушав их буквально 5 минут, вы бежите на приближающийся поезд.\n-Там вы думали, в какой бы магазин поехать")

    def taksi():
        print("-Вы вызываете такси и едете домой")
        print("-Играет спокойная музыка.\n-Вы расслабляетесь и думаете, в какой бы магазин поехать")

    def peshkom():
        print("-Вы решаете идти до магазина пешком, ведь растояние небольшое.")
        print("-Идя в магазин, вы разглядываете досопримечательности на пути и думаете, в какой бы магазин поехать.")

    def bolshoi():
        print('-Вот вы уже у магазина.Глядя на него, вы думаете насколько он большой и насколько обширный выбор одежды')
        print('-Вам нужно было лишь платье, поэтому вы направились в отдел с платьями')
        print('-Так как магазин был большой, вы потратили немало времени и нашли 2 платься, между которыми долго колебалсь')    
        print('-Спустя пару минут ваш выбор пал на:')

    def malenkyi():
        print('-Вот вы уже у магазина.Глядя на него, вы думаете хорошо, что он небольшой')
        print('-Вам нужно было лишь платье, поэтому вы направились в отдел с платьями')
        print('-Так как магазин был небольшой, вы потратили мало времени и нашли 2 платься, между которыми долго колебалсь')    
        print('-Спустя пару минут ваш выбор пал на:')

    def krasnoe():
        print('Вы решаетесь купить красное платье')
    def sinie():
        print('-Вы решаетесь купить синие платье')

    print("Добро пожаловать в игру-новеллу!")
    print("!Каждый ваш выбор будет влиять на дальнейшую судьбу вашего героя.!")    

    print ("Глава 1:")
    print ("-Вы встали рано утром и даже не вдупляете, что происходит.\nВам приходит мысль:")

    while (True):
        print("Придумате имя персонажа")
        name = input("Введите имя персонажа: ")
        print("Имя персонажа:", name)

        choice = gm_choice (["Сделать кофе","Сделать чай"])
        if choice == 1:
            coffe()
        else:
            chai()
        
        choice = gm_choice (["Скатать пару каток в доту", "Сделать домашнее задание", "Погулять" ])
        if choice == 1:
            dota()
        elif choice == 2:
            domashka()
        else:
            progylka()
        if choice ==2:
            choice = gm_choice(["Скатать пару каток в доту", "Погулять"])
            if choice == 1:
                dota()
            else:
                progylka()

        if choice == 1:
            choice = gm_choice (["Сделать домашнее задание", "Погулять" ])
            if choice ==1:
                domashka()
            else:
                progylka()

        if choice == 3:
            choice = gm_choice (["Поехать на метро","Вызвать такси", "Попробовать дойти пешком"])
            if choice == 1:
                metro()
            elif choice == 2:
                taksi()
            else:
                peshkom()
            
            if choice == 1:
                choice == gm_choice (["Большой", "Маленький"])
                if choice ==1:
                    bolshoi()
                else:
                    malenkyi()
            if choice == 2:
                choice == gm_choice (["Большой", "Маленький"])
                if choice ==1:
                    bolshoi()
                else:
                    malenkyi()
            if choice == 3:
                choice == gm_choice (["Большой", "Маленький"])
                if choice ==1:
                    bolshoi()
                else:
                    malenkyi()
            if choice == 1:
                choice == gm_choice (["Красное","Синие"])
                if choice ==1:
                    krasnoe()
                else:
                    sinie()
            if choice == 2:
                choice == gm_choice (["Красное","Синие"])
                if choice ==1:
                    krasnoe()
                else:
                    sinie()