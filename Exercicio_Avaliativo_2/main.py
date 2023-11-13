from database import Database
from teacher_crud import TeacherCRUD
from cli import CLI

uri = 'bolt://54.224.249.166:7687'
user = 'neo4j'
password = 'carloads-toolbox-book'

db = Database(uri, user, password)
teacher_crud = TeacherCRUD(db)

teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

cli = CLI(teacher_crud)
cli.run()

db.close()
