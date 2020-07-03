class Medal:
    def __init__(self, country, gold=0, silver=0, copper=0):
        self.__country = country
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper

    def __str__(self):
        return '金牌{}\n银牌{}\n铜牌{}\n'.format(self.__gold, self.__silver, self.__copper)

    def country(self):
        return self.__country

    def get_place(self, g, s, c):
        self.__gold += g
        self.__silver += s
        self.__copper += c

    def medalInfo(self):
        return self.__gold, self.__silver, self.__copper

    def total(self):
        return self.__gold + self.__silver + self.__copper


China = Medal('China', 10, 8, 6)
China.get_place(1, 1, 1)
print(China.medalInfo())
print('China total', China.total())
print(China)


Korea = Medal('Korea', 4, 3, 2)
Spain = Medal('Spain', 5, 3, 0)
Japan = Medal('Japan', 6, 3, 2)

MedalLst = [China, Korea, Spain, Japan]
order_by_gold = [i.country() for i in sorted(MedalLst, key=lambda x: x.medalInfo()[0], reverse=True)]
print(order_by_gold)
order_by_medal = [i.country() for i in sorted(MedalLst, key=lambda x: x.total(), reverse=True)]
print(order_by_medal)
