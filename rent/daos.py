from .models import *
from .services import *
from datetime import datetime

class AluguelDao:
    def alugarTema(self, s, n, compl, dist, c, state, date, start_hours, end_hours, client_id, theme_id):
        
        #Removendo Tupla
        date_string = date[0]
        date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
        
        # Salvar endereço 
        endereco = Address(street = s,
                 number = n,
                 complement = compl, 
                 district = dist,
                 city =c,
                 state = state)
        endereco.save()

        calcAluguel = CalcularAluguel()
        valorAluguel = calcAluguel.calcularDesconto(date_object, client_id, theme_id)

        aluguel = Rent (date=date_object, 
                 start_hours=start_hours,
                 end_hours=end_hours,
                 client_id= client_id,
                 theme_id = theme_id,
                 end_price= valorAluguel,
                 address = endereco )
        aluguel.save()