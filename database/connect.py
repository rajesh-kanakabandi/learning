import psycopg2

conn = psycopg2.connect("dbname='rajesh' user='postgres' host='localhost' password=''")
print("Connected successfully!!")
cursor = conn.cursor()
cursor.execute("""select * from Company""");
# for row in cursor.fetchall():
#     print(row)

while True:
    rows = cursor.fetchmany(2)
    if not rows:
        break
    for row in rows:
        print(row)

# cursor.execute("""insert into company values(3, 'fasdf',23,'sdfgd', 12.0)""")
# cursor.execute("""insert into company values(4, 'fasdf',23,'sdfgd', 12.0)""")
# cursor.execute("""insert into company values(5, 'fasdf',23,'sdfgd', 12.0)""")
cursor.execute("""insert into company values(9, 'fasdf',23,'sdfgd', 12.0)""")

cursor.execute("""update company set address='usa' where name='rajesh'""")
conn.commit()

#ORM object relational model.
#java - hibernate
#python - django, SQLAlchemy
#class Company(django.model):
    name = model.Integer(primary_key=True)
    address = model.Char(max_len=500)

import Cpmpany

records = Company.objects.filter(name="rajesh")
new_user = Company()
new_user.save()


users table;
    id,
    name,
    password;


tasks;
    id,
    uid,
    task,
    status;

select statment to query tasks for a particular user.
select statment to query incomplete tasks for a user.

select statment to query all user tasks
                        all user incomplete tasks.

insert statment to create a new task and assign to a user.


# fetchall()
# fetchone()
