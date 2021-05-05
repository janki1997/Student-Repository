from flask import Flask,render_template
import sqlite3
from typing import Dict

app: Flask = Flask(__name__)

@app.route('/')
def query_table()-> str:
    try:
        db_path: sqlite3.Connection = sqlite3.connect('C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW_12/Janki.db')
    except sqlite3.DatabaseError as e:
        return e

    data_collection : Dict[str , str] =[{'name': name, 'cwid' : cwid, 'course':course, 'grade':grade, 'instructor':instructor}\
    for name,cwid,course,grade,instructor in db_path.execute("""SELECT stu.Name,stu.CWID,gra.Course,gra.Grade,ins.Name
                    FROM student AS stu JOIN grades AS gra ON stu.CWID = gra.StudentCWID
                    JOIN instructor AS ins ON gra.InstructorCWID=ins.CWID
                    order by stu.Name""")]
    db_path.close()

    return render_template('forntview.html',
                           title='Stevens Repository',
                           t_title="student,course,grade,instructor",
                           s=data_collection)
if __name__ == '__main__':
    app.run(debug=True)
