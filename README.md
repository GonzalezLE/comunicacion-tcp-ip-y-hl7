##notas  protocollo HL7

HL7 default   Default HL7 interface - Interfaz predeterminada
HL7_PSM       HL7 interface from PSM - Interfaz HL7 de PSM
IM_HL7        HL7 interface from Instrument ManagerTM - Interfaz HL7 de Instrument ManagerTM
ASTM_PSM      ASTM interface from PSM - Interfaz ASTM de PSM
IM_ASTM       ASTM interface from Instrument ManagerTM -Interfaz ASTM de Instrument ManagerTM
PBP           PBP (Protocol Based on Pipes) interface - Interfaz PBP (protocolo basado en tuberías)

• Estándar de mensajería versión 2.xy versión 3 -
especificaciones de interoperabilidad para la salud y la medicina
actas.
• Arquitectura de documentos clínicos (CDA): una
modelo de intercambio de documentos clínicos, basado en HL7
Versión 3.
• Documento de continuidad de la atención (CCD) - un
especificación para el intercambio de resúmenes médicos,
basado en CDA.
• Etiquetado estructurado de productos (SPL): especificaciones
para la información publicada que acompaña a un
medicamento, basado en HL7 Versión 3.
• Grupo de trabajo de objetos de contexto clínico (CCOW): un
especificación de interoperabilidad para la integración visual
de las aplicaciones de usuario.

El "7" en HL7 se refiere a la séptima capa, o aplicación, del modelo OSI. La capa de aplicación sirve como trabajo área para que los usuarios accedan a los servicios de red. Incluye funciones comúnmente necesarias que incluyen:

• Acceso remoto a archivos
• Suministro compartido
• Administración de redes
• Directorio de Servicios
• Acceso remoto a la impresora
• Mensajería electrónica (por ejemplo, correo electrónico)
• Red de terminales virtuales

HL7 proporciona definiciones para los datos que se intercambiarán, el la sincronización de los intercambios de datos y la comunicación de Errores específicos de la aplicación entre aplicaciones.

#limitaciones

HL7 no proporciona ni admite los siguientes:

funcionalidad
• Seguridad: HL7 no prevé la aplicación de las políticas de seguridad del usuario y no especifica un método de cifrado específico.
• Confidencialidad: HL7 no aborda este problema y no hace ninguna suposición sobre el uso de los datos en el origen o destino de un mensaje.
• Responsabilidad: HL7 no define la transacción características de procesamiento necesarias en el entorno del usuario.




Se explica la configuración predeterminada de la interfaz de host HL7 abajo. Protocolo de capa inferior mínima El Protocolo de capa inferior mínima (MLLP) es el estándar para transmitir mensajes HL7 a través de TCP / IP. Cuando usas MLLP, se envía un mensaje HL7 en 1 bloque. Enmarcado caracteres envuelven el mensaje para marcar su comienzo y final. No pertenecen al contenido del mensaje.

********************************************************
*Function      *  Character            *   ASCII code  *
********************************************************
*Message start *  VT (vertical tab)    *     11        *
*Message end   *  FS (file separator)  *     28        *
*              *  CR (carriage return) *     13        *
********************************************************
*Segment end   *  CR (carriage return) *     13        *
********************************************************

## Data in an HL7 message is organized hierarchically


Mensaje : MSH
  Segmento : PID
    Campo : ORC
      Componente : OBR
        Subcomponente : OBX


## Mensaje
 HL7 define diferentes tipos de mensajes para propósitos. Un mensaje se define como una unidad completa de datos. transmitido entre el remitente y el receptor. Un mensaje es desencadenado por un evento real que genera un flujo de trabajo (p. ej. disponibilidad de un resultado de prueba para ser enviado al anfitrión).


## Segmento
Cada línea de un mensaje HL7 es un segmento. Los segmentos pueden ser obligatorio u opcional, y ocurrir solo una vez o repetidamente en un mensaje. Cada segmento comienza con un 3-cadena de caracteres (ID) que define el tipo de segmento. los El ID contiene solo caracteres imprimibles (ASCII 32–126).

## campo
Cada segmento consta de campos. Un campo contiene información sobre 1 atributo específico del segmento. Los campos pueden ser obligatorios, opcionales o condicionales y ocurrir solo una vez o repetidamente

## componentes
Los campos se subdividen en componentes que se refieren a un
conjunto lógico de caracteres dentro de un campo. Los componentes pueden
dividirse en subcomponentes.