class Msh:
  def __init__(self,cadena):
    self.cadena = cadena
    self.conjunto = cadena.split('|')

  def Id_tira(self):
    id_tira=self.conjunto[0]
    return id_tira

  def Id_separadores(self):
    separadores=self.conjunto[1]
    return separadores

  def Fecha_hora_del_mensaje(self):
    date=self.conjunto[6]
    return date

  def Tipo_mensaje(self):
    mensaje=self.conjunto[8]
  
  #este mensaje es unico por cada mensaje
  def Id_control_mensaje(self):
    control_msg=self.conjunto[9]
    return control_msg


#probando la clase
if __name__ == "__main__":
  mensaje='MSH|^~\&|cobas infinity 2.5|Roche Diagnostics|Receiver Application|Receiver Facility|20200616122014||OUL^R21^OUL_R21|6FE5440F-8043-41FB-8E19-47E7EEAD01EB|P|2.3|||ER|ER||8859/1'
  obj= Msh(mensaje)
  print('************* Id tira *************')
  print(obj.Id_tira())

  print('************* Id separadores *************')
  print(obj.Id_separadores())
  
  print('************* fecha y hora del mensaje *************')
  print(obj.Fecha_hora_del_mensaje())

  print('************* Tipo de mensaje *************')
  print(obj.Tipo_mensaje())

  print('************* id control de mensaje *************')
  print(obj.Id_control_mensaje())
