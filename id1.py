student_date = {'id1':
    {'name': ['Sara']
     ,'class': ['v'],
     'SUBJECT_intergration': ['Math,english,Science']
     },
    'id2':{
        'name': ['David']
     ,'class': ['v'],
     'SUBJECT_intergration': ['Math,english,Science']
     },
     'id3':{
        'name': ['surya']
        ,'class': ['v'],
        'SUBJECT_intergration': ['Math,english,Science']
     },
    }
result = {}
for key,value in student_date.items():
    if value not in result.values ():
        result[key] = value
        print(result)