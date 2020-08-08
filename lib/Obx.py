class OBX:
  def __init__(self, cadena):
    self.cadena = cadena
    self.conjunto = cadena.split('|')

  def Id_tira(self):
    return self.conjunto[0]

  def Id_test(self):
    return self.conjunto[3]

  def Resultado(self):
    return self.conjunto[5]

  def Unidad_resultado(self):
    return self.conjunto[6]

  def Alarmas(self):
    return self.conjunto[8]

  def Lotes(self):
    submodulos = self.conjunto[9]
    submodulos = submodulos.split('^')
    lote_de_control = submodulos[0]
    lote_de_reactivo = submodulos[1]
    return lote_de_control, lote_de_reactivo

  def Estatus_de_revision(self):
    submodulos = self.conjunto[10]
    modulos = submodulos.split('^')
    revision = modulos[0]
    text = ''
    if revision == 'H':
      text = 'Pendiente de revisar'
    else:
      if revision == 'S':
        text = 'Rechazado'
      else:
        if revision == 'A':
          text = 'Aceptado'
    return revision, text

  def Estatus_de_test(self):
    submodulos = self.conjunto[10]
    modulos = submodulos.split('^')
    test = modulos[1]
    text = ''
    if test == '1':
      text = 'Rechazado'
    else:
      if test == '3':
        text = 'Aceptado'
      else:
        if test == '':
          test = 'Por revisar'
    return test, text

  def fecha_y_hora_DeResultado(self):
    date = self.conjunto[14]
    return date

  def Id_instrumento(self):
    instrumento = self.conjunto[15]
    submodulos = instrumento.split('^')
    id_instrumento = submodulos[3]
    return id_instrumento

if __name__ == "__main__":
  cadena = 'OBX|1||109||99|ng/mL||Normal, No Alarm|PCCC2_001-L1^CS-cobas6kv2-1-ISE1-R1-GLU-L1|A^3|F|||20200616121951|^^^C6K-ISE1.800|||800.800'
  obx = OBX(cadena)
  print('********** id tira **********')
  print(obx.Id_tira())
  print('********** id test **********')
  print(obx.Id_test())
  print('********** resultado **********')
  print(obx.Resultado())
  print('********** unidad de resultado **********')
  print(obx.Unidad_resultado())
  print('********** alarmas **********')
  print(obx.Alarmas())
  print('********** Lotes **********')

  control,reactivo=obx.Lotes()
  print('control ----> '+control)
  print('reactivo ----> '+reactivo)

  print('********** Estatus de revision **********')
  revision,texto= obx.Estatus_de_revision()
  print(revision)
  print(texto)

  print('********** Estatus de revision **********')
  test, descrpcion = obx.Estatus_de_test()
  print(test)
  print(descrpcion)

  print('********** Fecha y hora de resultado **********')
  print(obx.fecha_y_hora_DeResultado()) 
  
  print('********** id instrucmento **********')
  print(obx.Id_instrumento())