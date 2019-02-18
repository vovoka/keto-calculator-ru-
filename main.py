from tkinter import *
from tkinter import ttk

PROGRAM_NAME = " Protein/Fat/Hydrocarb Calcualtor "

# Products contain products name and values of protein/fat/hydrocarb/kKal per 100gramm 
PRODUCTS = {
    "Абрикосы":[1,0,10,45],
    "Авокадо":[2,19,7,197],
    "Аджика":[2,3,8,59],
    "Айва":[1,0,9,41],
    "Айсберг":[1,0,2,17],
    "Активиа кефирная 1%":[3,1,4,39],
    "Ананас":[0,0,12,50],
    "Ананас консервированный":[0,0,16,65],
    "Ананас цукаты":[1,2,15,78],
    "Апельсин":[2,0,9,43],
    "Арахис":[25,46,13,561],
    "Арахис в сахаре":[18,30,51,535],
    "Базилик свежий":[3,1,4,27],
    "Баклажаны":[1,0,6,27],
    "Банан":[3,3,22,97],
    "Баранина вареная":[24,21,0,286],
    "Батон":[8,3,49,264],
    "Бедро индейки":[16,9,1,143],
    "Бекон":[15,45,2,469],
    "Блины обычные":[6,6,25,178],
    "Борщ лёгкий":[3,2,9,58],
    "Брокколи":[4,1,4,33],
    "Брусника":[1,0,9,42],
    "Бульон из говядины":[6,4,0,57],
    "Бульон из куриной грудки":[7,1,0,42],
    "Бульон куриный":[3,2,1,33],
    "Вареная говядина":[23,16,0,236],
    "Вареная колбаса":[12,22,1,253],
    "Вареная куриная грудка":[27,6,1,138],
    "Вареная курица":[19,9,0,150],
    "Вареная морковь":[1,0,6,31],
    "Вареная чечевица":[8,0,20,111],
    "Варёная сгущёнка":[7,9,55,326],
    "Вермишель":[11,1,72,347],
    "Ветчина":[16,19,2,246],
    "Вино белое сухое":[0,0,0,67],
    "Виноград":[1,1,16,69],
    "Вино красное сухое":[0,0,1,70],
    "Вишня":[1,0,11,54],
    "Геркулес":[12,6,56,327],
    "Говядина":[20,13,0,192],
    "Говяжья печень":[17,3,3,110],
    "Голень куриная":[20,9,0,168],
    "Голландский сыр":[24,30,0,373],
    "Голубика":[1,1,9,46],
    "Горбуша":[21,7,0,143],
    "Горох":[19,3,42,256],
    "Гороховое пюре":[8,1,23,106],
    "Горошек зеленый":[4,0,10,59],
    "Горчица":[8,11,13,184],
    "Гранат":[2,1,14,67],
    "Грейпфрут":[1,0,9,41],
    "Грецкие орехи":[15,65,14,697],
    "Гречневая каша рассыпчатая":[5,1,24,131],
    "Гречневая крупа":[12,4,63,329],
    "Грибы белые":[9,2,3,28],
    "Грибы белые сушеные":[27,7,16,239],
    "Грибы грузди":[2,1,1,16],
    "Грибы лисички":[2,1,1,20],
    "Грибы маслята":[2,1,1,9],
    "Грибы опята":[2,1,1,17],
    "Грибы подберёзовики свежие":[2,1,4,17],
    "Грибы подосиновики свежие":[3,1,3,26],
    "Грибы рыжики":[2,1,1,17],
    "Грибы шампиньоны":[4,1,0,22],
    "Груша":[1,0,12,51],
    "Груша (сухофрукты)":[2,0,62,246],
    "Дайкон":[1,0,4,21],
    "Джем мандариновый":[0,0,72,276],
    "Дрожжи":[29,3,23,263],
    "Дрожжи сухие":[49,6,40,410],
    "Дыня":[1,0,8,35],
    "Ежевика":[2,0,5,31],
    "Жареное яйцо":[14,14,1,183],
    "Желатин":[86,0,1,343],
    "Зеленая фасоль":[3,0,4,30],
    "Зеленый лук":[1,0,4,19],
    "Зелень петрушки":[4,0,8,50],
    "Зелёный горошек Бондюэль":[5,0,8,60],
    "Зелёный горошек Фрау Марта":[3,0,7,40],
    "Земляника":[1,0,9,38],
    "Зефир бело-розовый":[1,0,80,304],
    "Изюм":[2,0,68,280],
    "Имбирь свежий":[2,1,16,72],
    "Индейка (грудка)":[19,2,0,94],
    "Индейка (филе)":[20,12,0,188],
    "Инжир (сухофрукты)":[3,1,57,239],
    "Йогурт Активия":[4,3,11,97],
    "Кабачки жареные":[1,6,7,91],
    "Кабачки цукини":[2,0,3,16],
    "Кабачковая икра":[1,6,7,90],
    "Кабачок":[1,1,5,28],
    "Какао":[14,9,26,234],
    "Какао порошок":[23,15,29,326],
    "Кальмар":[18,2,1,97],
    "Кальмар ":[18,3,1,103],
    "Каперсы":[2,1,4,21],
    "Капуста белокочанная":[2,0,6,29],
    "Капуста брокколи замороженая":[2,0,4,21],
    "Капуста брюссельская":[4,0,4,47],
    "Капуста жареная":[3,6,8,88],
    "Капуста квашенная":[2,0,3,23],
    "Капуста китайская":[1,0,2,16],
    "Капуста кольраби":[3,0,9,42],
    "Капуста краснокочанная":[2,0,6,29],
    "Капуста морская":[1,5,0,58],
    "Капуста пекинская":[2,0,3,15],
    "Капуста цветная":[3,0,5,34],
    "Капуста цветная отварная":[2,0,4,29],
    "Картофель":[2,1,20,84],
    "Картофель молодой":[2,0,16,61],
    "Картофельные хлопья":[8,1,83,366],
    "Картофель фри":[4,17,40,323],
    "Картошка":[2,1,21,105],
    "Каша рисовая":[2,3,26,130],
    "Квас хлебный":[0,0,5,24],
    "Кедровые орехи":[15,63,17,652],
    "Кетчуп":[5,1,16,90],
    "Кефир 1%":[3,1,5,45],
    "Кефир 2,5%":[3,3,4,52],
    "Кефир 3,2%":[3,3,4,58],
    "Кешью":[21,48,20,607],
    "Киви":[1,1,10,51],
    "Клубника":[1,0,7,32],
    "Клюква":[0,0,9,43],
    "Клюква сушеная":[0,1,70,305],
    "Колбаса вареная докторская":[13,22,1,254],
    "Конфеты Батончики Рот Фронт с орехами":[12,32,49,379],
    "Корень имбиря":[2,1,18,90],
    "Корень сельдерея":[1,0,6,31],
    "Коричневый сахар":[0,0,92,393],
    "Корнишоны маринованные":[1,0,4,36],
    "Котлеты полтавские":[26,32,6,415],
    "Кофе молотый Арабика":[12,14,3,193],
    "Кофе растворимый (сухой)":[15,4,7,116],
    "Кофе эспрессо крепкий":[1,2,0,19],
    "Кофе якобз монарх (растворимый)":[15,0,8,97],
    "Крабовые палочки":[8,2,10,85],
    "Краковская колбаса":[17,39,0,420],
    "Красная фасоль консервированная":[7,0,17,99],
    "Крахмал картофельный":[0,0,82,335],
    "Крахмал кукурузный":[1,0,87,348],
    "Краюшка":[9,1,43,226],
    "Креветки м":[18,2,0,90],
    "Крупа гречневая":[12,3,65,326],
    "Крупа кукурузная":[8,1,75,337],
    "Крупа манная":[11,1,70,330],
    "Крупа овсяная":[12,6,65,342],
    "Крупа перловая":[10,1,65,328],
    "Крупа пшеничная":[12,2,63,322],
    "Крупа рис длиннозерный пропаренный":[7,1,74,333],
    "Крупа рисовая":[7,11,63,330],
    "Крупа ячневая":[10,1,59,318],
    "Крыжовник":[1,0,10,41],
    "Ксилитол":[0, 0, 97.9, 367],
    "Кукуруза консервированная":[3,2,17,87],
    "Кукурузные хлопья":[6,3,73,353],
    "Кунжут":[20,50,11,562],
    "Курага":[5,0,54,232],
    "Куриная печень":[19,7,1,140],
    "Куриные грудки":[23,6,3,144],
    "Куриные окорочка":[18,11,0,170],
    "Курица":[21,11,1,186],
    "Кус Кус (крупа)":[13,1,77,373],
    "Лаваш грузинский":[8,2,53,269],
    "Лайм":[1,0,4,20],
    "Лапша гречневая":[15,1,71,348],
    "Лапша рисовая":[5,1,81,350],
    "Лапша яичная":[10,2,64,330],
    "Лимон":[1,0,4,27],
    "Лосось":[21,10,1,172],
    "Лук":[1,0,9,40],
    "Лук зелёный перо":[1,0,5,16],
    "Лук красный салатный":[1,0,9,42],
    "Льняное масло":[1,92,4,849],
    "Майонез":[2,57,4,550],
    "Майонез 15%":[0,15,5,156],
    "Майонез провансаль 67%":[3,369,25,619],
    "Мак":[17,46,8,519],
    "Макаронные изделия":[10,0,72,344],
    "Макароны отварные":[4,1,23,119],
    "Малина":[4,0,9,41],
    "Манго":[1,0,13,62],
    "Манго цукаты":[0,0,60,278],
    "Мандарин":[1,1,9,40],
    "Манная крупа":[11,1,68,334],
    "Маргарин молочный":[0,82,6,745],
    "Маргарин солнечный":[0,72,0,653],
    "Мармелад":[1,0,75,302],
    "Маслины":[1,14,10,167],
    "Маслины без косточки":[1,13,2,133],
    "Масло кукурузное":[1,101,0,916],
    "Масло льняное":[0,96,0,895],
    "Масло оливковое":[1,91,3,851],
    "Масло подсолнечное":[0,96,0,864],
    "Масло растительное":[2,97,0,897],
    "Масло сливочное 83%":[1,83,1,674],
    "Масло сливочное 74%":[1,74,1,674],
    "Масло топленое":[0,86,0,890],
    "Мед":[1,0,80,315],
    "Миндаль":[18,51,16,601],
    "Молоко":[7,3,7,66],
    "Молоко 0,5%":[2,1,3,35],
    "Молоко 1,5%":[3,2,5,44],
    "Молоко 2.5%":[2.8, 2.5, 4.7, 52],
    "Молоко 3,2%":[3,3,8,67],
    "Молоко сгущёное":[7,9,56,317],
    "Молоко сухое":[31,22,36,446],
    "Морковь отварная":[1,0,7,32],
    "Морковь печеная":[1,0,7,31],
    "Морковь свежая":[1,0,8,35],
    "Мороженое Пломбир":[4,15,24,245],
    "Морская капуста":[1,2,2,37],
    "Мука кукурузная":[9,3,65,333],
    "Мука пшеничная в/с":[10,1,71,332],
    "Мука ржаная":[8,2,65,307],
    "Мюстли с фруктами":[8,2,68,314],
    "Мясо свинина":[26,29,7,293],
    "Мясо свинина постная":[18,8,0,151],
    "Нектарин":[1,0,11,47],
    "Облепиха":[1,2,6,47],
    "Овощная смесь 'Весенние овощи'":[3,0,4,30],
    "Овсяная мука":[13,7,65,368],
    "Овсянка":[9,5,46,271],
    "Овсянные хлопья 'геркулес'":[11,6,51,305],
    "Огурцы":[1,0,4,19],
    "Огурцы грунтовые":[1,0,3,14],
    "Огурцы маринованные":[2,0,2,16],
    "Огурцы солёные":[1,0,2,14],
    "Оливки":[1,17,5,178],
    "Оливки зеленые без косточки":[1,17,0,157],
    "Омлет":[10,14,3,175],
    "Орех грецкий":[15,64,11,671],
    "Отруби овсяные":[15,7,45,305],
    "Отруби пшеничные очищенные":[13,4,23,214],
    "Отруби ржаные очищенные":[12,3,9,167],
    "Паприка":[3,2,7,112],
    "Патиссон":[1,0,4,19],
    "Перепелиное яйцо":[13,13,0,167],
    "Перец сладкий":[1,0,5,26],
    "Перец чили":[2,0,9,40],
    "Перловка (крупа)":[10,1,76,346],
    "Перловка отварная":[2,0,27,121],
    "Персики":[1,1,12,51],
    "Персики (сухофрукты)":[2,0,42,168],
    "Петрушка корень":[2,0,11,48],
    "Петрушка свежая":[3,1,7,38],
    "Печенье 'Юбилейное' Молочное":[8,18,66,455],
    "Печень куриная":[27,7,1,144],
    "Пиво светлое":[0,0,4,50],
    "Плавленный сыр":[15,20,2,280],
    "Помидоры консервированные":[1,0,5,23],
    "Помидоры свежие":[4,1,3,33],
    "Простокваша":[3,3,4,52],
    "Пшено":[11,3,68,337],
    "Ревень черешковый":[1,0,4,16],
    "Редис":[1,0,4,20],
    "Редька":[2,0,7,35],
    "Редька зеленая":[2,0,7,35],
    "Репа":[1,0,5,29],
    "Рис":[7,1,75,331],
    "Рис отварной":[4,1,25,134],
    "Рожки отварные":[3,0,24,115],
    "Рожки (сухой продукт)":[11,1,72,344],
    "Руккола":[2,1,2,24],
    "Рыба скумбрия":[16,13,1,187],
    "Рыба треска":[17,1,0,80],
    "Рябина черноплодная":[2,0,12,54],
    "Ряженка":[3,3,4,62],
    "Салат лист":[1,0,2,16],
    "Сахар песок":[0,0,109,396],
    "Свежий укроп":[3,1,6,38],
    "Свекла":[2,1,12,61],
    "Свекла отварная":[2,0,10,50],
    "Свинина":[16,27,0,304],
    "Сельдерей":[1,0,3,13],
    "Сельдерей стебель":[1,0,2,11],
    "Сельдь атлантическая жирная":[15,15,0,204],
    "Семена тыквы неочищенные с солью":[29,47,13,596],
    "Семечки подсолнечные":[26,50,9,583],
    "Сладкая кукуруза в початках":[4,3,21,124],
    "Слива садовая":[1,0,10,45],
    "Сливки 10%":[3,10,4,118],
    "Сливки 20%":[3,20,4,206],
    "Сливки 22%":[3,22,4,224],
    "Сливки 33%":[2,33,4,322],
    "Сметана 10%":[3,10,4,117],
    "Сметана 15%":[3,15,4,159],
    "Сметана 20%":[3,19,6,204],
    "Сметана 25%":[2.6, 25, 2.5, 248],
    "Сметана 30%":[2,30,3,291],
    "Смородина красная":[1,0,8,40],
    "Смородина чёрная":[1,0,9,41],
    "Соевый соус":[5,0,22,36],
    "Сок апельсиновый":[1,0,11,47],
    "Сок грейпфрутовый":[0,0,10,44],
    "Сок лайма":[1,0,6,22],
    "Сок лимона":[1,0,3,18],
    "Сок лимонный":[1,0,5,29],
    "Сок мандарина":[1,0,10,43],
    "Сок свекольный":[1,0,14,61],
    "Сок томатный":[0,0,5,21],
    "Сок яблочный":[0,0,10,44],
    "Соленый огурец":[1,0,3,14],
    "Соус соевый":[4,0,10,53],
    "Соя":[34,12,27,359],
    "Спагетти отварные":[7,1,46,223],
    "Спагетти (сухой продукт)":[10,1,72,344],
    "Сухари панировочные":[12,2,74,362],
    "Сыворотка":[1,0,4,22],
    "Сыр брынза":[17.9, 20.1, 0, 260],
    "Сыр 45%":[26,26,0,336],
    "Сыр 50% «Сливочный»":[23,28,0,288],
    "Сыр Адыгейский":[18,16,0,224],
    "Сыр гауда":[24,27,2,350],
    "Сыр козий":[19,23,2,296],
    "Сыр «Лёгкий»":[23,17,0,300],
    "Сырок плавленный Дружба":[6,19,0,178],
    "Сыр российский":[23,29,0,361],
    "Сыр твердый":[25,27,2,358],
    "Тархун":[0,0,10,41],
    "Творог 0%":[16,0,2,75],
    "Творог 1%":[17,1,2,82],
    "Творог 5%":[17,5,2,122],
    "Творог 9%":[16,8,3,153],
    "Творог 10%":[15,9,2,150],
    "Творог 11%":[16, 11, 1, 170],
    "Творожная масса с цукатами":[7,21,33,349],
    "Тесто дрожжевое":[7,4,43,238],
    "Тесто слоеное дрожжевое":[7,19,40,356],
    "Тесто слоёное бездрожжевое":[6,18,38,335],
    "Томат":[1,0,5,27],
    "Томатная паста помидорка":[1,0,15,77],
    "Томаты (парниковые)":[1,0,3,14],
    "Треска филе":[17,1,0,78],
    "Тушенка говядина высший сорт":[15,17,0,213],
    "Тыква":[1,0,5,22],
    "Укроп":[3,1,6,38],
    "Уксус столовый 6-7%":[0,0,6,13],
    "Урюк (сухофрукты)":[5,0,51,213],
    "Фарш говяжий":[18,16,0,214],
    "Фарш куриный":[19,10,0,166],
    "Фасоль":[18,1,44,263],
    "Фасоль «Бондюэль»":[7,0,10,74],
    "Фасоль стручковая":[2,0,4,29],
    "Фасоль стручковая замороженная":[2,0,4,26],
    "Фасоль Фрау Марта":[6,1,16,92],
    "Фaсоль Фрау Марта в томатном соусе":[5,0,15,86],
    "Фасоль Фрау Марта Лобио":[5,1,13,80],
    "Фенхель":[1,0,7,31],
    "Филе куринное":[23,2,0,114],
    "Филе куриной грудки":[22,2,0,109],
    "Финики (сухофрукты)":[2,0,72,280],
    "Фруктоза":[0,0,100,390],
    "Фундук":[15,62,11,665],
    "Хлеб белый":[8,3,54,254],
    "Xлеб бородинский":[7,1,42,210],
    "Хлеб пшеничный":[8,3,50,263],
    "Хлеб ржаной":[7,1,36,187],
    "Хлебцы пшеничные":[12,2,60,305],
    "Хлопья кукурузные":[7,1,84,373],
    "Хлопья овсяные":[12,6,52,308],
    "Хрен":[3,5,14,113],
    "Хурма":[1,0,15,65],
    "Цедра апельсина":[1,0,6,36],
    "Цедра лимона":[1,0,4,28],
    "Цукаты":[3,0,56,224],
    "Цукини":[2,0,3,18],
    "Черемша":[2,0,7,37],
    "Черешня":[1,0,12,51],
    "Черника":[1,0,9,39],
    "Чернослив (сухофрукты)":[3,0,62,256],
    "Чеснок":[6,0,23,115],
    "Чечевица зелёная":[24,2,44,286],
    "Чечевица красная":[22,1,49,312],
    "Шампиньоны":[4,1,1,26],
    "Шампиньоны замороженные":[3,0,1,27],
    "Шампиньоны резанные консерв.":[0,1,1,16],
    "Шелковица":[1,0,13,52],
    "Шиповник сушёный":[4,0,60,253],
    "Шоколад 57%":[0, 35, 49, 540],
    "Шоколад горький 75%":[9,41,39,550],
    "Шоколад горький 80%":[12,39,34,527],
    "Шоколад молочный":[7,34,52,539],
    "Шпинат":[3,0,2,22],
    "Щавель":[2,0,5,25],
    "Яблоки":[1,1,13,60],
    "Яблоки сушёные (сухофрукты)":[3,0,66,269],
    "Яйца":[15,13,1,162]
}

p_names = list(PRODUCTS.keys())
root=Tk()
root.title(PROGRAM_NAME)

ttk.Style().configure("TButton", bd = 1, relief=RAISED, width=11)

def to_box_2():
    """ Replace chosen product form box_1 to box_2 """

    select=list(box_1.curselection())
    select.reverse()
    for i in select:
        tmp_list = [box_1.get(i), enter_mass.get()]
        box_2.insert(END, tmp_list)
        u_box_2_list.append([box_1.get(i), int(enter_mass.get())])
        box_1.delete(i)
        press()


def to_box_1():
    """ Replace chosen product form box_2 to box_2 """

    select=list(box_2.curselection())
    select.reverse()
    for i in select:
        box_1.insert(END, box_2.get(i)[0])
        box_2.delete(i)
        # delete from u_box_2_list the product.
        u_box_2_list.pop(i)
        press()


def press():
    """ Update report values 
    
    Represents "Calculate and show updated result" button press.
    Call 'Calculator function'.
    """

    report_parameter_names = [
        Report_P_gram, Report_P_kkal, Report_P_percent,
        Report_F_gram, Report_F_kkal, Report_F_percent,
        Report_H_gram, Report_H_kkal, Report_H_percent,
        Report_total_kkal
    ]
    calc_res = calculator(u_box_2_list)
    for i in range(10):
        report_parameter_names[i].config(text=calc_res[i])


def calculator(eated_food: list) -> list:
    """Calcuale total amount of proteins/fat/hydrocarbons/kKalories

    Argument: dictionary, where key is food name, value is a mass in grams
    Argument example: {'Банан': '50', 'Бекон': '400'}

    Returns: List:
        [0] Protein in gr
        [1] Protein in kkal
        [2] Protein in % (from all cunsumed products)
        [3] Fat in gr
        [4] Fat in kkal
        [5] Fat in % (from all cunsumed products)
        [6] Hydrocarb in gr
        [7] Hydrocarb in kkal
        [8] Hydrocarb in % (from all cunsumed products)
        [9] Total kkal consumed

    """

    output = [0] * 10

    if not eated_food:
        return output
    total_protein = 0
    total_fat = 0
    total_hydrocarb = 0
    total_kkal = 0
    for product in eated_food:
        if product[0] in PRODUCTS:
            # protein = mass * (value per 100gr)
            total_protein += product[1] * PRODUCTS[product[0]][0] / 100
            total_fat += product[1] * PRODUCTS[product[0]][1] / 100
            total_hydrocarb += product[1] * PRODUCTS[product[0]][2] / 100
            total_kkal += product[1] * PRODUCTS[product[0]][3] / 100
        else: 
            print('ERR!: ', product)

    # Food energy
    # https://en.wikipedia.org/wiki/Food_energy
    # Energy in kkal:
    total_protein_kkal = total_protein * 4.1
    total_fat_kkal = total_fat * 9.29
    total_hydrocarb_kkal = total_hydrocarb * 4.1
    total_kkal = total_protein_kkal + total_fat_kkal + total_hydrocarb_kkal

    output = [
        int(total_protein),
        int(total_protein_kkal),
        round((total_protein_kkal/total_kkal * 100), 1),
        int(total_fat),
        int(total_fat_kkal),
        round((total_fat_kkal/total_kkal * 100), 1),
        int(total_hydrocarb),
        int(total_hydrocarb_kkal),
        round((total_hydrocarb_kkal/total_kkal * 100), 1),
        int(total_kkal)
    ]
    return output


def show_about_window():
    about_text = """Программа создана для образовательных целей;\nразработчик не несет никакой ответственности о результатах программы.\n
        Обратную связь с разработчиком: kovalyov.volodymyr@gmail.com
        """
    newwin = Toplevel(root)
    display = Label(newwin, text=about_text, justify=LEFT, wraplength=500)
    display.pack()  


def show_help_window():
    helptext = """Калькулятор белков, жиров, углеводов и калорий (Далее - БЖУК).\n
        Как пользоваться:
          - Выбираете продукт из списка слева, выделяете его кликом на нем.\n 
          - Вносите вес продукта в средней части окна (по умолчанию программа предполагает что вы потребляте по 100 грамм продукта).\n
          - Кликаете на кнопку [↦]. Продукт с указанной массой перемещается во второй список. - Кнопкой [↤] можно удалить продукт из списка (этот продукт теперь будет в конце первого списка). Программа автоматически считает общую величину БЖУК для выбранного набора продуктов.\n\n
        FAQ
    • Можно ли редактировать общий список продуктов, изменять калорийность?
     - На данном этапе - нет. В случае развития проекта, данная функциональность может быть добавлена.
    • Как поддержать проект?
     - Исходный код проекта находится по ссылке: https://github.com/vovoka/keto-calculator-ru-
     - Если вы не программист/ка, пишите на kovalyov.volodymyr@gmail.com.
        """
    newwin = Toplevel(root)
    display = Label(newwin, text=helptext, justify=LEFT, wraplength=300, width = 60)
    display.pack()  

# Add Menubar in the widget
menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to", command=show_help_window)
helpmenu.add_command(label="About", command=show_about_window)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)


top=Frame()
top.pack(side=TOP)

# Report frame
right_fr=Frame()
right_fr.pack(side=BOTTOM)

u_box_2_list = list() # list of eated food ['product_name', mass]
# Label(text="Product list").pack(side=TOP)
box_1=Listbox(top,selectmode=EXTENDED, height= 25)
box_1.pack(side=LEFT)


for product in p_names:
    box_1.insert(END, product)
scroll=Scrollbar(top,command=box_1.yview)
scroll.pack(side=LEFT, fill=Y)
box_1.config(yscrollcommand=scroll.set)
 
mid=Frame(top)
mid.pack(side=LEFT)

Label(mid, text="gram").pack()
default_mass = StringVar(mid, value='100')
enter_mass = Entry(mid, textvariable=default_mass, width=4)
enter_mass.pack()
mass = enter_mass.get()

Button(mid, text="↦", command=to_box_2).pack()
Button(mid, text="↤", command=to_box_1).pack()

box_2=Listbox(top, selectmode=EXTENDED, height= 25)
box_2.pack(side=LEFT)
scroll=Scrollbar(top, command=box_2.yview)
scroll.pack(side=LEFT, fill=Y)
box_2.config(yscrollcommand=scroll.set)

# Report header
Report_dummy = ttk.Button(right_fr)
Report_dummy.grid(row = 1, column = 1)
Report_gram = ttk.Button(right_fr, text="грам")
Report_gram.grid(row = 1, column = 2)
Report_kkal = ttk.Button(right_fr, text="кКал")
Report_kkal.grid(row = 1, column = 3)
Report_percent = ttk.Button(right_fr, text="%")
Report_percent.grid(row = 1, column = 4)

# Protein
Report_P_name = ttk.Button(right_fr, text="Белки")
Report_P_name.grid(row = 2, column = 1)
Report_P_gram = ttk.Button(right_fr)
Report_P_gram.grid(row = 2, column = 2)
Report_P_kkal = ttk.Button(right_fr)
Report_P_kkal.grid(row = 2, column = 3)
Report_P_percent = ttk.Button(right_fr)
Report_P_percent.grid(row = 2, column = 4)

# Fat report
Report_F_name = ttk.Button(right_fr, text="Жиры")
Report_F_name.grid(row = 3, column = 1)
Report_F_gram = ttk.Button(right_fr)
Report_F_gram.grid(row = 3, column = 2)
Report_F_kkal = ttk.Button(right_fr)
Report_F_kkal.grid(row = 3, column = 3)
Report_F_percent = ttk.Button(right_fr)
Report_F_percent.grid(row = 3, column = 4)

# Hydrocarbons report
Report_H_name = ttk.Button(right_fr, text="Углеводы")
Report_H_name.grid(row = 4, column = 1)
Report_H_gram = ttk.Button(right_fr)
Report_H_gram.grid(row = 4, column = 2)
Report_H_kkal = ttk.Button(right_fr)
Report_H_kkal.grid(row = 4, column = 3)
Report_H_percent = ttk.Button(right_fr)
Report_H_percent.grid(row = 4, column = 4)

# total kKal report
Report_total_kkal_name = ttk.Button(right_fr, text="Всего")
Report_total_kkal_name.grid(row = 5, column = 1)
Report_total_kkal = ttk.Button(right_fr)
Report_total_kkal.grid(row = 5, column = 3)

press()
root.mainloop()
