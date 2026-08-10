# Схема БД

Тема БД: учет домашних заданий студентов.

```mermaid
erDiagram
    STUDENTS ||--o{ SUBMISSIONS : "сдает"
    HOMEWORKS ||--o{ SUBMISSIONS : "имеет"

    STUDENTS {
        int id PK
        string name
    }

    HOMEWORKS {
        int id PK
        string title
    }

    SUBMISSIONS {
        int id PK
        boolean accepted
        int student_id FK
        int homework_id FK
    }
```

## Таблицы

`students` - студенты.

`homeworks` - домашние задания.

`submissions` - статус сдачи домашнего задания студентом.

## Связи

Один студент может иметь много сдач:

```text
students.id -> submissions.student_id
```

Одно домашнее задание может иметь много сдач:

```text
homeworks.id -> submissions.homework_id
```
