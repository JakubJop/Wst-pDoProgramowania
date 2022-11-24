def z5(**kwargs):
  if 'end' in kwargs:
      pom=kwargs['end']
  else:
      pom= '\n'
  print(kwargs)
  for k in kwargs:
   print(k,' = ', kwargs[k],end=pom)

z5(dom=1,ulica="Lwowska", kod_pocztowy='35-202')
print()
z5(dom=7,ulica="Lwowska", kod_pocztowy='35-202',end=' ')
