# CONTADOR DE SEGUNDOS

segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")

segundosint = int(segundos_str)

dias = segundosint//86400
segundosrestantesdias = segundosint%86400

horas = segundosrestantesdias//3600
segundosrestanteshoras = segundosrestantesdias%3600

minutos = segundosrestanteshoras//60
segundosrestantesfinal = segundosrestanteshoras%60

print(dias, "dias,",horas, "horas,",minutos, "minutos e",segundosrestantesfinal, "segundos." )
