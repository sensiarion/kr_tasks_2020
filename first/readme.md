## Сбор дани

Петя и его друзья решили устроить вечиринку по случаю сдачи ОГЭ.  
Петю назначали ответственным за сбор средств. Ходить и лично спрашивать каждого у Пети  
желания не было, поэтому он сказал всем скидывать сообщения о переводе в общий чат.  

Сообщение о переводе выглядит следующим образом:

перевод с карты <1234> <Имя> <Фамилия> на карту <1234> в размере * рублей.  
Например: "перевод с карты 4276 Мансур Изерт на карту 3286 в размере 300 рублей"  


Необходимо помочь Пете определиться с тем, кто уже сдал деньги в необходимом количестве, а кому ещё
предстоит это сделать


### Ввод

На вход подаётся число N с кол-вом сообщений, номер карты на которую необходимо совершить перевод  
и минимальная сумма M которую необходимо сдать каждому.
Далее идут N сообщений, часть из которых являются сообщеними о переводе


### Вывод

Кол-во учеников, сдавших необходимую сумму и сообщения о необходимой сумме для сдачи для тех, кто сдал
недостаточно.

### Примеры

#### Пример 1

10  
6198  
1400  
перевод с карты 4904 Настя Максимова на карту 6198 в размере 6000 рублей  
перевод с карты 9403 Настя Башмакова на карту 6198 в размере 9700 рублей  
перевод с карты 2277 Даша Чугунова на карту 4202 в размере 1800 рублей  
перевод с карты 7505 Вика Иванова на карту 6198 в размере 6400 рублей  
перевод с карты 3765 Оля Башмакова на карту 6198 в размере 1100 рублей  
перевод с карты 9666 Миша Иванов на карту 5754 в размере 2700 рублей  
перевод с карты 2808 Оля Торова на карту 7992 в размере 5300 рублей  
перевод с карты 6847 Вася Столяров на карту 6198 в размере 7700 рублей  
перевод с карты 2166 Гоша Башмаков на карту 6198 в размере 6600 рублей  
перевод с карты 2147 Максим Петров на карту 6198 в размере 2000 рублей  
------------------------------------  
6  
Даша Чугунова необходимо доплатить ещё 1400 рублей  
Оля Башмакова необходимо доплатить ещё 300 рублей  
Миша Иванов необходимо доплатить ещё 1400 рублей  
Оля Торова необходимо доплатить ещё 1400 рублей  

#### Пример 2

9  
6377  
2200  
перевод с карты 5916 Оля Торова на карту 8222 в размере 4700 рублей  
перевод с карты 4432 Катя Максимова на карту 2250 в размере 8200 рублей  
перевод с карты 2584 Вася Башмаков на карту 8471 в размере 3200 рублей  
перевод с карты 3715 Максим Башмаков на карту 7410 в размере 3300 рублей  
перевод с карты 3251 Даша Башмакова на карту 6377 в размере 3700 рублей  
перевод с карты 3485 Даша Торова на карту 6377 в размере 4900 рублей  
перевод с карты 4730 Миша Столяров на карту 1483 в размере 8500 рублей  
перевод с карты 8751 Даша Петрова на карту 6377 в размере 6100 рублей  
перевод с карты 9509 Максим Башмаков на карту 5298 в размере 7500 рублей  
------------------------------------  
3  
Оля Торова необходимо доплатить ещё 2200 рублей  
Катя Максимова необходимо доплатить ещё 2200 рублей  
Вася Башмаков необходимо доплатить ещё 2200 рублей  
Максим Башмаков необходимо доплатить ещё 2200 рублей  
Миша Столяров необходимо доплатить ещё 2200 рублей  
Максим Башмаков необходимо доплатить ещё 2200 рублей  



### Примечание

От 1 человека может придти **только 1** сообщение о переводе
