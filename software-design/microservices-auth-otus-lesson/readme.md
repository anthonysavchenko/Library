# Практика аутентификации и авторизации в микросервисной архитектуре

20.10.2025

Рекомендации к сессии на основе cookies: HttpOnly, Secure, SameSite

Identity Provider - внешний провайдер: OAuth2.0/OpenUD Connect (OIDC), SAML, cамописные флоу

JWT

В payload находятся атрибуты (claims), чтобы не хранить их в каком-то централизованном хранилище

Плюс - не нужно централизованное хранилище, минус - нельзя сделать единый single sign off

Сервис-меш (sidecar proxy) - полезный паттерн для взаимодействия между микросервисами

Основной курс на Otus: https://otus.ru/lessons/microservice-architecture/

Альтернатива на Яндексе: https://practicum.yandex.ru/microservice-architecture/

