#definir un bingo 5x5
filas = 5
columnas=5
num= random.sample(range(1,51),25)
carton=[[random.choice(num)for_ir range(5)]for_ir range(5)]
print(carton)