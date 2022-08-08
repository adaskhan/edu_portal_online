# Educational Project
## Content
1. Project Description
2. Project Deployment
3. Additional part
4. API Documentation

## Project Description
Данный проект был создан для реализации минимального функционала под внутренний портал для студентов и преподавателей.  
Данный проект создан как учебный материал курса Python camp.

## Project Deployment


## Documentation
### Courses API
Base URL: `courses/api/v1/`
1. url: `courses`
GET all courses:
```json
[
    {
        "url": "http://localhost:8000/courses/api/v1/courses/1/",
        "name": "Python",
        "description": "Python basics + Django",
        "lessons_count": 21,
        "lesson_duration": 70.0
    },
]
```

| Attribute | Type | Description       |
|-----------|------|-------------------|
| `url`     | str  | URL of object     |
| `name`    | str  | Name of the course|
