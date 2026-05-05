# C# разработчик. Экспертный уровень

**otus.ru, 2026**

## Память (куча и стэк)

### Процесс и память

FOH?

### Значимые типы

### Ссылочные типы

### Стэк

- Какой размер стэка? 1 Мб.

- Как выглядит стэк в памяти

### 00:36 Куча

### 01:05 Boxing и unboxing

Вызов CompareTo у int будет ли вызывать упаковку?

### Сборка мусора

### 01:30 LOH - Large Object Heap

### 01:35 POH - Pinned Object Heap

## Неуправляемые ресурсы (IDisposable.Dispose)

Ресурсы бывают управляемые и не управляемые. Рекомендуется использовать подход к освобождению ресурсов через деструктор и IDisposable.Dispose.

https://metanit.com/sharp/tutorial/8.2.php

https://learn.microsoft.com/en-us/dotnet/api/system.idisposable.dispose

Продолжить: https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose

И там же про DisposeAsync и await using

И еще про ConfigureAwait: https://habr.com/ru/articles/482354/