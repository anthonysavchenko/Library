# Руководство по межпроцессному взаимодействию (IPC) в Linux

**Marty Kalin, ~2024**

[Source](https://opensource.com/sites/default/files/gated-content/inter-process_communication_in_linux.pdf)

[Перевод. Часть 1](https://habr.com/ru/articles/819263/)

[Перевод. Часть 2](https://habr.com/ru/articles/842410/)

[Перевод. Часть 3](https://habr.com/ru/articles/846608/)

IPC - interprocess communication

Механизмы:

- Разделяемые файлы (shared files)

- Разделяемая память (shared memory), семафоры (semaphore), мьютексы (частый случай семаформа - только два значения, mutually exclusive - взаимоисключающие)

- Именованные и неименованные каналы (named and unnamed pipes)

- Очереди сообщений (message queues)

- Сокеты (sockets)

- Сигналы (signals)
