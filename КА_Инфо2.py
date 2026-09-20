import time
import random

inventory = []
rooms_visited = set()
RUN = False
Speak = False
inroom = inroom2 = indvor = indvor2 = infield = infield2 = intown = inminiroom = 0
print('Сцена 1!')
print('Краткий экскурс в проиходящее:')
print('Вы- средневековый воин по имени Кори Динлас. В свои 14 вы уже командир среднего отряда восьмого батальона (В вашем городе это неудивительно).')
def safe_input(prompt, options=None):
    """Безопасный ввод данных с защитой от некорректного ввода."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and prompt.lower().endswith('(ctrl+c для выхода)\n'):
                 raise KeyboardInterrupt
            if options and all(isinstance(x, str) for x in options):
                return user_input.lower()
            value = int(user_input)
            if options is None or value in options:
                return value
            else:
                print(f"Пожалуйста, выберите один из вариантов: {', '.join(map(str, options))}.")
        except ValueError:
            print("Ошибка: нужно ввести число.")
        except KeyboardInterrupt:
            print("\n\nВыход из игры...")
            exit()
def _show_report_text():
    """Вывод текста доклада Джетта (вынесен для исключения дублей)."""
    print('вы берете листок в руки, и всматриваетесь в неровный почерк')
    time.sleep(2)
    inventory.append('доклад Джетта')
    print('"Доклад командиру младшего отряда Авангарда..."')
    time.sleep(1)
    print('"от 31 марта 1745 года"')
    time.sleep(2)
    print('"Вчера на обход у северо-западной стены города было отправлено четверо человек, из которых не вернулся не один."')
    time.sleep(5)
    print('"Не смотря на то, что такие ситуации случались и ранее, меня, как заместителя, волнует то, что солдаты не возвращаются в крепость к ночи."')
    time.sleep(5)
    print('"Всвязи с тем, прошу разрешения на поиск, и последующий разбор ситуации. Или самостоятельного принятия мер"')
    time.sleep(5)
    print('сбоку еще более неразборчиво начиркано: "Кори, прошу, предупреди если пойдешь искать их сам, я ведь тебя знаю."')
    time.sleep(4)
    print('вы откладываете лист и лишь мысленно усмехаетесь. На первый раз вольности в докладе Джетту можно простить. проблема в том, что это вовсе не первый и не второй раз.')
    time.sleep(4)
    print('или в том, что он угадал ваши намерения самому во всем разобраться')
def commroom():
    global inroom, inroom2, RUN
    rooms_visited.add('комната')
    inroom += 1
    has_sword = 'меч' in inventory
    has_report = 'доклад Джетта' in inventory
    if RUN != True:
        if inroom == 1 and inroom2 == 0:
            print('Вы находитесь в данной вам, как командиру, отдельной комнате...')
            time.sleep(6)
            print('за окном ранне утро... В глаза сразу бросается бумага с неровным и спешным почерком.')
            time.sleep(6)
            print('хотите прочесть что он написал?')
            choice = safe_input('1-да, взять и прочитать\n2-нет, обойдется\n', [1, 2])
            if choice == 1:
                _show_report_text()
            else:
                pass
                print('вы можете выйти из комнаты, а можете остаться и поискать что нибудь полезное.')
        if not has_sword or not has_report:
            if inroom > 1 or (inroom == 1 and not has_report):
                print('вы оглядываете комнату...')
                time.sleep(2)
                if not has_sword:
                    print('Двуручный меч сделан специально для вас на заказ.')
                    take_sword = safe_input('1-взять меч\n2-не брать меч\n', [1, 2])
                    if take_sword == 1:
                        inventory.append('меч')
                
                if not has_report:
                    print('На столе лежит стопка докладов.')
                    take_report = safe_input('1-взять доклад\n2-пройти мимо\n', [1, 2])
                    if take_report == 1:
                        _show_report_text()
        
        print('1-выйти во двор крепости\n2-выйти с обратной стороны здания на поле\n3-остаться')
        ost = safe_input('', [1, 2, 3])
        
        if ost == 1:
            dvor()
        elif ost == 2:
            fieldofgarden()
        elif ost == 3:
            inroom2 = 1
            commroom()
            
    else:
        if not has_sword:
            print('вы забегаете в свою комнату, но оружия нет!')
            time.sleep(2)
            print('Девушка появляется быстрее, чем вы успеваете среагировать...')
            time.sleep(2)
            print('ПЛОХАЯ КОНЦОВКА! Безоружный воин против мага обречен.')
            restart = safe_input('1-выход, 2-начать с последнего сохранения\n', [1, 2])
            if restart == 1:
                exit()
            else:
                RUN = False
                commroom()
        else:
            print('вы забегаете в свою комнату, и почти инстинктивно выхватываете меч из ножен')
            time.sleep(2)
            print('как только вы оборачиваетесь, девушка почти материализуется перед вами')
            fight_choice = safe_input('1-защищаться\n2-атаковать\n', [1, 2])
            
            print('вы пытаетесь применить тактику, но магия девушки ломает ваш клинок...')
            time.sleep(3)
            print('к вашей ноге по полу ползет синяя змея...')
            time.sleep(2)
            print('ПЛОХАЯ КОНЦОВКА! Вас убила ведьма...')
            restart = safe_input('1-выход, 2-начать с последнего сохранения\n', [1, 2])
            if restart == 1:
                exit()
            else:
                RUN = False
                commroom()

def dvor():
    global indvor, indvor2
    
    rooms_visited.add('двор')
    indvor += 1
    
    if RUN != True:
        if indvor == 1 and indvor2 == 0:
            print('вы выходите во двор крепости...')
            time.sleep(3)
            print('Однако, остановившись, вы замечаете что-то на земле')
            sledi = safe_input('1-осмотреть, 2-пройти мимо\n', [1, 2])
            
            if sledi == 1:
                inventory.append('следы')
                print('вы обнаруживаете следы с узором, какого не могло быть на простых ботинках воинов...')
                time.sleep(4)
                print('А ведут они прямо к высокой арке крепостных ворот, в город...')
                wheregodvor = safe_input('1-пойти в город\n2-вернуться в комнату\n3-пойти на поле\n', [1, 2, 3])
                if wheregodvor == 1:
                     town()
                elif wheregodvor == 2:
                     commroom()
                elif wheregodvor == 3:
                     fieldofgarden()
            else:
                print('вы игнорируете находку...')
                wherego = safe_input('1-пойти на поле\n2-вернуться в комнату\n', [1, 2])
                if wherego == 1:
                    fieldofgarden()
                elif wherego == 2:
                    commroom()
        else:
            print('вы во дворе крепости.')
            if 'следы' not in inventory and 'город' not in rooms_visited:
                wherego = safe_input('1-осмотреть землю\n2-пойти на поле\n', [1, 2])
                if wherego == 1:
                    inventory.append('следы')
                    print('вы обнаруживаете странные следы...')
                    time.sleep(2)
                    print('А ведут они прямо к высокой арке крепостных ворот, в город...')
                    wheregodvor = safe_input('1-пойти в город\n2-вернуться в комнату\n3-пойти на поле\n', [1, 2, 3])
                    if wheregodvor == 1:
                        inventory.add('город')
                        town()
                    elif wheregodvor == 2:
                        commroom()
                    elif wheregodvor == 3:
                        fieldofgarden()
                elif wherego == 2:
                    fieldofgarden()
            else:
                wherego = safe_input('1-пойти на поле\n2-пойти в город\n', [1, 2])
                if wherego == 1:
                    fieldofgarden()
                elif wherego == 2:
                    town()
    else: 
        print('вы забегаете в крепость и оказываетесь во дворе.')
        wherego = safe_input('1-бежать в комнату\n2-бежать на поле\n', [1, 2])
        if wherego == 1:
            commroom()
        elif wherego == 2:
            fieldofgarden()

def town():
    global intown, Speak
    
    rooms_visited.add('город')
    intown += 1
    
    if RUN != True:
        if intown == 1:
            print('вы вышли в город...')
            time.sleep(3)
            print('среди лавочников вы заметили одного знакомого...')
            razg = safe_input('1-поговорить\n2-пройти мимо\n', [1, 2])
            
            if razg == 1:
                print('-ты вчера никого из моего отряда тут не видел?')
                print('"да кого ж мне тут встречать..."- начал лепетать он')
                speak = safe_input('1-распросить спокойно\n2-настаивать на своем\n', [1, 2])
                
                print('вы прикрикнули на торговца...')
                time.sleep(2)
                print('-Анри заходила! ...ну и еще человека три с ней были!')
                Speak = True
        
        print('1-пойти в поле за стенами города\n2-вернуться в крепость')
        wherego = safe_input('', [1, 2])
        if wherego == 1:
            field1()
        elif wherego == 2:
            dvor()
            
    else:
        print('вы забегаете обратно в город, вам некуда бежать кроме как в крепость')
        dvor()

def field1():
    global RUN
    RUN = True
    print('вы выходите за стены города... и опираетесь на стог сена.')
    time.sleep(5)
    print('вы резко повернулись. слева от вас стояла невысокая фигура под черным плащом.')
    time.sleep(3)
    print('девушка резо обернулась... вы инстинктивно ухватили рукоять меча.')
    runaway = safe_input('1-напасть первым\n2-отойти подальше\n', [1, 2])
    
    if runaway == 1:
        print('однако ее ладони вспыхнули синем пламенем, и в острие вашего меча влетел пламенный шар...')
        live = safe_input('1-постараться выжить\n', [1])
        print('вы бросились бежать, благо до стен города было недалеко...')
        town()
    else:
        print('вы бросились бежать...')
        town()

def fieldofgarden():
    global infield, infield2
    
    if RUN != True:
        infield += 1
        if infield == 1 and infield2 == 0:
            print('вы выходите на поле за зданием казарм...')
            time.sleep(3)
            print('осмотревшись, вы замечаете небольшую дверь в здании позади.')
            wherego2 = safe_input('1-зайти в дверь\n2-вернуться в комнату\n3-вернуться во двор\n', [1, 2, 3])
            if wherego2 == 1:
                miniroom()
            elif wherego2 == 2:
                commroom()
            elif wherego2 == 3:
                dvor()
        else:
            target = 'кладовая' if 'кладовая' in rooms_visited else 'странную дверь'
            wherego2 = safe_input(f'зайти в {target}?\n1-зайти\n2-вернуться в комнату\n3-вернуться во двор\n', [1, 2, 3])
            if wherego2 == 1:
                miniroom()
            elif wherego2 == 2:
                commroom()
            elif wherego2 == 3:
                dvor()
    else: 
        print('вы выбегаете на пустое поле...')
        time.sleep(4)
        print('Однако девушка неспешным шагом идет к вам...')
        if 'кладовая' in rooms_visited:
            whererun = safe_input('1-бежать в свою комнату\n2-бежать в кладовую\n', ['1', '2'])
            if whererun == '1':
                commroom()
            elif whererun == '2':
                miniroom()
        else:
            whererun = safe_input('1-бежать в свою комнату\n2-бежать к странной двери\n', ['1', '2'])
            if whererun == '1':
                commroom()
            elif whererun == '2':
                miniroom()

def miniroom():
    global inminiroom
    
    rooms_visited.add('кладовая')
    
    if RUN == True:
        print('вы пытаетесь открыть дверь, пока сзади приближаются шаги...')
        time.sleep(2)
        final_fight = safe_input('1-спрятаться\n2-попытаться найти оружие\n', [1, 2])
        
        if final_fight == 2:
            print('вы хотели дотянуться до оружия, но тело каменеет...')
            time.sleep(3)
            print('Хорошая концовка первой сцены! Ведьма не успела вас убить.')
            exit()
        elif final_fight == 1:
            print('вы прячетесь за бочками, но девушка отбрасывает их...')
            time.sleep(2)
            print('ПЛОХАЯ КОНЦОВКА. помощь не успела((')
            restart = safe_input('1-выход, 2-начать с последнего сохранения\n', [1, 2])
            if restart == 1:
                exit()
            else:
                fieldofgarden()
    else:
        inminiroom += 1
        if inminiroom == 1:
            print('вы попытались открыть дверь, но она не поддалась вам, даже не скрипнув')
            time.sleep(2)
            fieldofgarden()
        else:
            print('кладовая все так же не поддается никаким усилиям')
            time.sleep(2)
            fieldofgarden()

if __name__ == '__main__':
    try:
        commroom()
    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка: {e}")
        print("Игра будет закрыта для предотвращения потери данных.")
