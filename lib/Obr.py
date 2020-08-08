class Obr:
  def __init__(self,cadena):
    self.cadena = cadena
    self.conjunto = cadena.split('|')

  def Id_tira(self):
    tira=self.conjunto[0]
    return tira

  def Nombre_control_de_calidad(self):
    calidad=self.conjunto[2]
    return calidad

if __name__ == '__main__':
  cadena = 'OBR|1|PCCC2-ISE1||ALL|||||||||||^^^^^^Q||||||||||||^^^^^R'
  obj=Obr(cadena)

  print('*********** id de la tira ***********')
  print(obj.Id_tira())
  
  print('*********** control de calidad ***********')
  print(obj.Nombre_control_de_calidad())
