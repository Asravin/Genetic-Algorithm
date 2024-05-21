# Алгоритм построения генетического метода селекции

## 1. Сделаем класс **Chromosome**, у которого будет три свойства:

* **rating** - рейтинг хромосомы

* **size** - размер хромасомы (длина массива генов)

* **genes** - массив генов хромасомы (то, что раньше было самой хромосомой)

## 2. Теперь напишем функцию для генерации случайной хромасомы.

> Функция принимает два параметра:

* **длина хромасомы**, которую надо получить, 

* **набор генов**, из которого надо сделать хромасому

## 3. Создадим функцию заполнения популяции

> В функцию **Заполнения популяции** передадим:

* **размер популяции**

* **размер хромасом**

* **генофонд**

* **подбор пар** 

> Чтобы не зависеть от от глобальных переменных
