from email import message


class Data:

   def __init__(self, dia, mes, ano):
     self.data = {dia, mes, ano}
     self.dia = dia
     self.mes = mes 
     self.ano = ano
     self.formatada

   def formatada(self):
     print("{}/{}/{}".format(self.dia, self.mes, self.ano))
     



  
     


