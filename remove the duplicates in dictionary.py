student_data = {'id1': 
   {'name': ['Sara'], 
    'section': ['V'], 
    'subject': ['english, math, python']
   },
 'id2': 
  {'name': ['David'], 
    'section': ['f'], 
    'subject': ['english, math, python']
   },
 'id3': 
    {'name': ['Sara'], 
    'section': ['V'], 
    'subject': ['english, math, python']
   },
 'id4': 
   {'name': ['Surya'], 
    'section': ['i'], 
    'subject': ['english, math, python']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
