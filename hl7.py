from lib.Obx import OBX

mensaje1 = 'MSH|^~\&|cobas infinity 2.5|Roche Diagnostics|Receiver Application|Receiver Facility|20200616122014||OUL^R21^OUL_R21|6FE5440F-8043-41FB-8E19-47E7EEAD01EB|P|2.3|||ER|ER||8859/1'
mensaje1 += 'PID|1'
mensaje1 += 'ORC|RE|PCCC2-ISE1|||IP||^^^^^^R'
mensaje1 += 'OBR|1|PCCC2-ISE1||ALL|||||||||||^^^^^^Q||||||||||||^^^^^R'
mensaje1 += 'OBX|1||109||99|ng/mL||Normal, No Alarm|PCCC2_001-L1^CS-cobas6kv2-1-ISE1-R1-GLU-L1|A^3|F|||20200616121951|^^^C6K-ISE1.800|||800.800'

prueba = 'OBX|1||109||99|ng/mL||Normal, No Alarm|PCCC2_001-L1^CS-cobas6kv2-1-ISE1-R1-GLU-L1|A^3|F|||20200616121951|^^^C6K-ISE1.800|||800.800'


if __name__ == "__main__":
  obx = OBX(prueba)
  """obx.Id_tira()
  obx.Id_test()
  obx.Resultado()
  obx.Unidad_resultado()
  obx.Alarmas()
  #lote_de_control, lote_de_reactivo
  obx.Lotes()
  #revision, text
  obx.Estatus_de_revision()
  # test, text
  obx.Estatus_de_test()

  obx.fecha_y_hora_DeResultado()
  obx.Id_instrumento()
  """

"""
data=prueba.split('|')

print(len(data))

print('posicion 1 :'+data[0])
print('posicion 2 :'+data[1])
print('posicion 3 :'+data[2])
print('posicion 4 :'+data[3])
print('posicion 5 :'+data[4])
print('posicion 6 :'+data[5])
print('posicion 7 :'+data[6])
print('posicion 8 :'+data[7])
print('posicion 9 :'+data[8])
print('posicion 10 :'+data[9])
print('posicion 11 :'+data[10])
print('posicion 12 :'+data[11])
print('posicion 13 :'+data[12])
print('posicion 14 :'+data[13])
print('posicion 15 :'+data[14])
print('posicion 16 :'+data[15])
print('posicion 17 :'+data[16])
print('posicion 18 :'+data[17])
print('posicion 19 :'+data[18])
"""

#print(data)
"""
OBX|
1
||
109
||
99|
ng/mL
||
Normal, No Alarm
|
PCCC2_001-L1^CS-cobas6kv2-1-ISE1-R1-GLU-L1
|
A^3
|
F
|||
20200616121951
|
^^^C6K-ISE1.800
|||
800.800



"""
