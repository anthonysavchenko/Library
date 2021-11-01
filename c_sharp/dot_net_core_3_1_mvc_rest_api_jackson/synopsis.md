# .NET Core 3.1 MVC REST API - Full Course

*By Les Jackson* — Apr 23, 2020


## References

[Source](https://www.youtube.com/watch?v=fmvcAzHpsk8)

[Repository](https://github.com/anthonysavchenko/Commander)

[Model Binding in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/mvc/models/model-binding?view=aspnetcore-3.1)

[nuget](https://www.nuget.org/)


## Acronyms and Terminology

* DTO - Domain Transfer Object. Used to **decouple** internal domain from external contract.


## Usefull Commands

`dotnet new webapi -n Commander` - create new project from template

`dotnet new mvc -au None -o aspnetapp` - create MVC application without authentication in aspnetapp
directory

`code -r Commander` - open folder in VS Code from the outside

`code .` - open folder in VS Code from the inside

`dotnet restore` - restore packages, generate make file etc

`dotnet build` - build code

`dotnet run` - run program

`dotnet add package AutoMapper.Extensions.Microsoft.DependencyInjection` - install package from nuget

`dotnet tool install --global dotnet-ef` - install Entity Framework CLI

`dotnet tool` - check if EF CLI is installed

`dotnet tool update --global dotnet-ef` - update Entity Framework CLI

`dotnet ef migrations add Initial` - create new migration named Initial

`dotnet ef migrations remove` - remove last migration

`dotnet ef database update` - update database with migrations


## Difference Between PUT and PATCH

PUT - "full" update (need to supply the entire object), inefficient, error prone, PATCH is the favoured approach.

PATCH request body example:

```c#
[
    {
        "op": "replace",
        "path": "/howto",
        "value": "How to run program"
    }
]
```

