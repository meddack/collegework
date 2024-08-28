db={}
def add_stud(nm,sid,clss,grade):
    if sid in db:
        print("already there")
    else:
        db[sid]={
            'stu_name':nm,
            'id':sid,
            'class':clss,
            'grade':grade
        }
        print("student added")
 
add_stud("aabcd","4","5","B")
print(db)

def update_grade(sid,ngrade):
    if sid in db:
        db[sid]['grade']=ngrade
        print(db)
    else:
        print('data doesnt exist')

update_grade("4","C")
print('updated')
    
