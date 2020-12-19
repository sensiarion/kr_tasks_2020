## Ренегаты
Начальник токарного цеха получил нагоняй от руководства с формулировкой "недисциплинированное поведение сотрудников".
Ну, наш начальник человек простой, поэтому решил показать коллективу, как тут работать надобно.
Помогите начальнику вывести коллектив на равную трудоспособность

### Ввод
На ввод подаётся матрица, содержащая информацию о производительности всех сотрудников на заводе

### Вывод
Необходимо вывести словарь, в котором ключем будут являться максимальная и минимальная производительности сотрудников, 
а значениями – список из кортежей с номерами мест сотрудников, на которых сидят выделившиеся.


### Примеры

#### Пример 1
27	10	12	8	20	7	29	24	7	  
10	6	20	24	8	29	13	6	8	  
18	11	10	26	19	15	7	19	24	  
6	19	28	14	22	9	15	5	22	  
---------------------------------------
{29: [(0, 6), (1, 5)], 5: [(3, 7)]}
#### Пример 2
20	18	9	13	4	18	1	8	19	  
27	24	10	28	7	25	21	26	9	  
12	29	19	2	13	12	28	28	29	  
2	8	9	20	20	21	18	23	22	  
30	11	29	9	4	9	20	2	14	  
25	4	2	2	2	26	20	6	27	  
12	29	28	15	3	22	1	3	4	  
17	7	11	28	25	27	26	11	25	  
21	17	11	28	29	21	27	28	16	  
27	3	8	10	18	6	19	21	23	  
---------------------------------------
{30: [(4, 0)], 1: [(0, 6), (6, 6)]}  


#### Пример 3  

21	5	16	29	26	  
9	16	1	16	13	  
1	19	21	4	23	  
25	27	25	19	22	  
---------------------------------------
{29: [(0, 3)], 1: [(1, 2), (2, 0)]}