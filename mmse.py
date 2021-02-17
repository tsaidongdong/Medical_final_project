def mmse_test():
    point = 0
    print("今年是幾年？")
    year = input()
    if year == 2020:
        point = point + 1
    print("分數 = " + point)
    print("現在是甚麼季節？")
    season = input()
    if season == '冬季':
        point = point + 1
    print(point)
    print("現在是幾月？")
    month = input()
    if month == 12:
        point = point + 1
    print("分數 = " + point)
    print("今天是幾號？")
    day = input()
    if day == 25:
        point = point + 1
    print("分數 = " + point)
    print("今天是星期幾？")
    week = input()
    if week == '星期五':
        point = point + 1
    print("分數 = " + point)
    print("你在哪一個縣市？")
    province=input()
    if province == '台南市':
        point = point + 1
    print("分數 = " + point)
    print("我們在哪裡？")
    where = input()
    if where == '資訊系館':
        point = point + 1
    print("分數 = " + point)
    print("我們在幾樓？")
    floor = input()
    if floor == 10:
        point = point + 1
    print("分數 = " + point)
    print("99 減 7 五次等於多少？")
    sub = input()
    if sub == 64:
        point = point + 5
    print(point)