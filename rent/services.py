from .models import *

class CalcularAluguel:
    def calcularDesconto(self, date, client_id, theme_id):
        valorDesconto = 0

        if self.jaAlugou(client_id):
            valorDesconto += 0.1

        if self.verificarDiaDaSemana(date):
            valorDesconto += 0.4

        preco = Theme.objects.values_list('price', flat=True).get(id=theme_id)

        print('----- inicial', preco)
        print('----- valor desconto', valorDesconto)
        if valorDesconto > 0:
            valorDesconto *= preco
            preco -= valorDesconto 
            print('----- com desconto', preco)
        return preco
    
    # Verificar se o cliente já alugou alguma tema
    def jaAlugou(self, cliente_id):
        cliente = Client.objects.get(pk=cliente_id)
        return Rent.objects.filter(client=cliente)
    
    # Verificar se o dia escolhido é ida da semana
    def verificarDiaDaSemana(self,date):
        if date.weekday() < 4:
            print('############ verdadeiro ############')
            return True
        else: 
            
            print('############ falso ############')
            return False