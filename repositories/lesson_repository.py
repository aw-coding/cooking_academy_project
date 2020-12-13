from db.run_sql import run_sql
from models.lesson import Lesson


def save(lesson):
    sql = 'INSERT INTO lessons (name) VALUES (%s) RETURNING id'
    values = [lesson.name]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson


def select(id):
    lesson = None
    sql = 'SELECT * FROM lessons WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        lesson = Lesson(result['name'], result['id'])
    return lesson


def select_all():
    lessons = []
    sql = 'SELECT * FROM lessons'
    results = run_sql(sql)
    for row in results:
        lesson = Lesson(row['name'], row['id'])
        lessons.append(lesson)
    return lessons


def update(lesson):
    sql = 'UPDATE lessons SET (name, id) = (%s, %s) WHERE id = %s'
    values =[lesson.name, lesson.id]
    run_sql(sql, values)