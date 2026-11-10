# 12. Lock-Free алгоритмы с Interlocked и Volatile

**15.06.2026**

Уже есть более современные алгоритмы - wait-free

У locked-based подходах есть несколько проблем, самая известная - deadlocks

Условия возникновения deadlock от Коффмана, Элфика и Шошани (1970–1971 годы):

1. Взаимоисключение (Mutual exclusion). Одновременно использовать ресурс может только один процесс. Каждый ресурс в данный момент времени или отдан одному процессу, или свободен.

2. Ожидание ресурсов (Hold and wait). Процессы удерживают ресурсы, которые им уже выделены, и могут запрашивать новые ресурсы.

3. Неперераспределяемость (No preemption). Ресурс, выделенный ранее процессу, не может быть принудительно забран у него. Освободить ресурс может только тот процесс, который его удерживает.

4. Круговое ожидание (Circular wait). Существует кольцевая цепь процессов, в которой каждый процесс ждёт доступа к ресурсу, удерживаемому другим процессом из этой цепи.

37:45

**Дополнительные материалы для дальнейшего изучения**

https://habr.com/ru/companies/wunderfund/articles/322094/

https://learn.microsoft.com/ru-ru/dotnet/csharp/language-reference/keywords/volatile

https://learn.microsoft.com/ru-ru/archive/msdn-magazine/2012/december/csharp-the-csharp-memory-model-in-theory-and-practice

https://dotnettutorials.net/lesson/interlocked-vs-lock-in-csharp/

https://proglib.io/p/atomarnye-operacii-bezopasnost-potokov-i-sostoyanie-gonki-v-c-2023-08-03

https://habr.com/ru/companies/otus/articles/868764/

https://highload.ru/moscow/2019/abstracts/6012

https://csharp-help.ru/2025/07/08/проблема-aba-в-lock-free-алгоритмах/

https://csharp-help.ru/2025/07/08/атомарные-операции-с-interlocked/

https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked

https://github.com/dotnet/runtime/blob/1d1bf92fcf43aa6981804dc53c5174445069c9e4/src/libraries/System.Private.CoreLib/src/System/Threading/Interlocked.cs
