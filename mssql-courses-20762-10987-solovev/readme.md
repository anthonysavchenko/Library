# 20762: Developing SQL Databases + 10987: Performance Tuning and Optimizing SQL Databases

## Индексы

*04.08.2025*

```sql
DBCC DROPCLEANBUFFERS -- очищает данные, прочитанные в память с диска

SET STATISTICS IO ON -- при выполнении запросов пишет статистику выполнения

DBCC SHOWCONTIG ('TableName', IndexName) -- показывает особенности расположения индекса на диске
```

### Технологии хранения данных

  - HEAP

    - можно использовать обычные (некластерные) индексы

  - COLUMNSTORE (CLUSTERED COLUMNSTORE INDEX)

    - похожа на кучу, но очень сжатую

  - CLUSTERED STORAGE (CLUSTERED INDEX)

    - во время вставки в таблицу для проверки наличия id в связанном справочнике выгоднее делать первичный ключ справочника не кластерным

### Особенности индексов

    - составные индексы - можно включать до 16 колонок таблицы, макс длина строки 900 байт

    - составные индексы сортируют последовательно по каждой колонке

    - можно включать несортированные данные с помощью INCLUDE

    - фильтрованные индексы сокращают данные для хранение в индексе (эти строки не индексируются) CREATE INDEX MyIndex ON Table (Name) WHERE Name <> 'Bob' AND Name <> 'Mary'

    - можно делать сжатие индексов WITH (DATA_COMPRESSION = PAGE)

    - PAGE SPLIT - для некластерного индекса, random access к диску, получается разряженный и неэффективный индекс, зависит от длины строки индекса, решается с помощью компрессии ALTER INDEX ... WITH (DATA_COMPRESSION = PAGE, FILLFACTOR = 70), чтобы не было лишних PAGE SPLIT (записей на диск)

    - HOT PAGES - для индекса возрастающего при вставке (IDENTITY(1, 1)), решается количеством файлов в рабочей группе

### Partitioning Data

Разделение таблицы на 16000 кусков (chunks). Оптимизация по таблице на повторяющее значение - создают искуственные поля. Или одна таблица под исторические данные, вторая под актуальные (или даже просто под каждый год насоздавать куски заранее). Также поддерживаются SWITCH, SPLIT, MERGE

**Домашняя работа. Lab 3 - 20762**


## Курс 10987. Модуль 10. Средства мониторинга (Monitoring, Tracing, and Baselines)

*05.08.2025*

### Baseline

Необходимо собрать базу для дальнейшего сравнения

  - Environment (OS + Hardware)

    - CPU

    - Memory

    - Disk

### Инструменты

  - Панель управления - Администрирование - Системный монитор (Performance Monitor)

    - Процессор

      - % работы в пользовательском режиме

      - % работы в привилегированном режиме

    - Система

      - Длина очереди процессора

      - Контекстных переключений в секунду (их должно быть как можно меньше)

    - Память

      - Pages/sec

      - Page Faults/sec

    - SQLServer Buffer Manager

      - Checkpoint pages/sec

      - Buffer cache hit  (если не 100% то серверу приходится читать с диска вместо памяти)

      - Page lige expectancy (должна плавно расти)

    - SQLServer Databases

      - Log Flushes/sec

      - Log Flash Waits/sec

    - Физический диск

      - Обращений к диску/с

      - Скорость записи на диск (байт/с)

      - Скорость чтения с диска (байт/с)

      - Средняя длина очереди диска

  - Extended events

    Management - Extended Events - Sessions - New (PAGE SPLIT)

    Пример: transaction_log, operation LOP_DELETE_SPLIT, histogram, field alloc_unit_id,

    Пример: field latch_suspend_end, filter = (mode = SH or mode = UP or mode = EX) and database_id = 8, event page_id, histogram, field page_allocation_unit_id

  - Avtivity Monitor

    - Latch

    - Buffer Latch

```sql
SELECT * FROM sys.dm_db_database_page_allocations(7, default, default, default, default)
WHERE allocation_unit_id = 720989809087987098 -- (alloc_unit_id value)

SELECT * FROM sys.indexes
WHERE object_id = 123412341234 -- (index_id)

SELECT * FROM sys.dm_db_index_usage_stats
WHERE object_id = 124312341234 -- (index_id)
```

### Основные проблемы

  - Блокировки
      
  - Неграмотная работа с сетью
      
  - Неграмотно работа с диском

Чтобы убрать частое переключение контекстов при долгих вычислениях можно сделать задержку:

```sql
DECLARE @Tmp INT = 0
WHILE 1 = 1
BEGIN
WAITFOR DELAY '00:00:00.001'
SET @Tmp = 1
END
```

Файл: Header|GAM|SGAM|PFS|--------PFX----GAM|SGAM-----...

### tempdb

tempdb - узкое место SQLServer из-за того, что все клиенты и базы данных используют ее для временных таблиц (Hash Join, ORDER BY, GROUP BY, CREATE TABLE #Table). Это как PageFile для Windows. Мы получаем блокировки страниц. Боремся с этим количеством файлов и раскладываем их на разные быстрые диски (SSD). Но хотя и не боимся потерять эти диски. А также лучше больше разделять базы данных, чтобы у каждой базы данных была своя tempdb (разные экземпляры серверов) и файл логов (разделение по базам данных). Можно использовать линкованные сервера для джойнов (правда, это не рекомендовано уже, и есть альтернативы)

## Статистика

*07.08.2025*

COMPATIBILITY_LEVEL - при переносе БД остается на той версии сервера, на которой она была создана

CARDINALITY ESTIMATION - оценка количества строк, которое выдаст запрос по статистике 

  - до MSSQL 2014 включительно = (a/n) * (b/n) * n

  - начиная с MSSQL 2016 и выше = (a/n) * POWER((b/n), 0.5) * n

Статистику по нескольким полям нужно создавать и обновлять самостоятельно, а по одному полю сервер создает и обновляет сам. Для маленьких таблиц (< 500 строк) обновление статистики выполняется при внесении 10% строк изменений. Для больших таблиц (> 500 строк) - при внесении 20% изменений.

### Activity Moninor

```sql
-- Processes
SELECT * FROM sys.dm_exec_sessions WHERE session_id > 51

-- Resource Waits
SELECT * FROM sys.dm_os_wait_stats ORDER BY wait_time_ms DESC

SELECT * FROM sys.dm_exec_query_stats AS S
CROSS APPLY sys.dm_exec_sql_text(S.plan_handle) AS T
CROSS APPLY sys.dkm_exec_query_plan(S.plan_handle) AS P
WHERE T.text LIKE '%TestHeap%'
```

## Инструменты для диагностики работы БД

- Query Store

- Помощник по настройке ядра СУБД

- `SELECT * FROM sys.dm_db_tuning_recommendations`

## Курс 10987. Модуль 8. Plan Caching and Recompilation

`SET STATISTICS TIME ON` - показывает, на что сервер потратил время при выполнении запроса

`DBCC FREEPROCCACHE` - очистить кэш планов

Планы с постоянной селективностью хорошо использовать в процедурах (в программных объектах), так как план запроса не меняется при повторнвх выполнениях

`ALTER TABLE T1 SET PARAMETERIZATION FORCED WITH NO_WAIT` - все запросы превращаются в процедуры с параметрами

`EXEC sys.sp_configure N'optimize for ad hoc workloads', N'1'`

## Курс 10987. Модуль 8. Views

*11.08.2025*

Кэширование данных во вью. Только аддитивные функции

```sql
CREATE VIEW ViewName
WITH SCHEMABINDING AS
SELECT ... SUM(...) AS F1, COUNT_BIG(*) AS F2
GROUP BY F3

CREATE UNIQUE CLUSTERED INDEX IndexName ON ViewName(F3)
```

20762 - 8-11 lab
10987 - 5 lab

## SQL Server Components and SQLOS

*12.08.2025*

Context Switches / sec (System) - можно наблюдать (в Performance Monitor), будет высоким, если один из потоков выжерает много CPU, должно примерно равнятся количеству потоков в ОС (в Task Manager). Также полезно мониторить % Privileged Time и % User Time (Processor)

Managment - Resource Governor - new Resourse Pool (можно смотреть Template Browser) - можно регулировать количество ресурсов для выполнения задач по пользователю. Применяется для выполнения технических задач без потребления большого количества ресурсов

## Memory Table

Memory Optimized Table - сейчас применяют для "опердня" (оперативно меняющейся части таблицы), Column Store Index - используют для остальной части таблицы

Memory Optimized Table - индекс с указателями на строки в памяти. Вся наодится в памяти. Восстанавливается из лога. Делают UNION ALL таблицу "опердня" Memory Table с Column Store, разбитую на партиции. Но нужно регулярно переносить руками каждый "опердень" в большую таблицу.

10987 - 1, 4 Lab

Найти все учебники на виртуалках 
Запустить лабы

