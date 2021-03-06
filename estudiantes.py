import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set(f'estudiante:b45698:nombre', "David Ramirez")
r.set(f'estudiante:b45698:carrera', "Artes Plasticas")
r.set(f'estudiante:b45698:ponderado', 10)
r.incr('universidad:cantidadEstudiantes')
r.zadd("estudiantes:ponderado:index", "b45698", 10)

r.set(f'estudiante:b86574:nombre', "Bianca Nieves")
r.set(f'estudiante:b86574:carrera', "Fisica")
r.set(f'estudiante:b86574:ponderado', 7.5)
r.incr('universidad:cantidadEstudiantes')
r.zadd("estudiantes:ponderado:index", "b86574", 7.5)

r.set(f'estudiante:b75486:nombre', "Alejandro Ramirez")
r.set(f'estudiante:b75486:carrera', "Artes Plasticas")
r.set(f'estudiante:b75486:ponderado', 10)
r.incr('universidad:cantidadEstudiantes')
r.zadd("estudiantes:ponderado:index", "b75486", 10)

r.set(f'estudiante:b59218:nombre',"Kevin Jimenez")
r.set(f'estudiante:b59218:carrera', "Informatica")
r.set(f'estudiante:b59218:ponderado', 8)
r.incr('universidad:cantidadEstudiantes')
r.zadd("estudiantes:ponderado:index", "b59218", 8)

r.set(f'estudiante:b55824:nombre', "Joe Rementeria")
r.set(f'estudiante:b55824:carrera', "Informatica")
r.set(f'estudiante:b55824:ponderado', 9.2)
r.incr('universidad:cantidadEstudiantes')
r.zadd("estudiantes:ponderado:index", "b55824", 9.2)

r.set(f'estudiante:b69896:nombre', "Ramon Chacon")
r.set(f'estudiante:b69896:carrera', "Economia")
r.set(f'estudiante:b69896:ponderado', 2.9)
r.incr('universidad:cantidadEstudiantes')
r.zadd("estudiantes:ponderado:index", "b69896", 2.9)
