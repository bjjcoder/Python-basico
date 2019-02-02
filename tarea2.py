todos = [[177, 145, 167, 190, 140, 150, 180,180]], #grupo1
...: [165, 198, 2001, 789], #grupo2,
...: [197, 189, 123, 098], #grupo3,
...: [890, 345, 345, 234, 9] #grupo4

maximo = max(*todos)
maximo

[165, 198, 2001, 789]

todos.index(maximo)

3

todos.index(max(*todos))

3