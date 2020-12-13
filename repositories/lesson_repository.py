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