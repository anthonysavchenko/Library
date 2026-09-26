# 15. Профилирование CPU: BenchmarkDotNet и dotnet-trace

**25.06.2026**

Виды измерений:

- Ручные замеры (StopWatch)

- Бэнчмарки (BenchmarkDotNet)

- Трассировка

  dotnet-trace: `dotnet tool install --global dotnet-trace`

  `dotnet run -c Release -- cpu-slow 60`

  `dotnet-trace collect -p 71096 --profile dotnet-sampled-thread-time dotnet-common -o cpu-slow.nettrace`

  PerfView: `https://github.com/microsoft/perfview`

  SpeedScope: https://www.speedscope.app/, `npm install -g speedscope`

  `dotnet trace collect -p <process id> --format speedscope`

  `dotnet trace convert --format speedscope <trace filename>`

- Счетчики
