# Conceptos Básicos utilizados en Python

1.- ¿Para qué usamos Clases en Python?

2.- ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

3.- ¿Cuáles son los tres verbos de API?

4.- ¿Es MongoDB una base de datos SQL o NoSQL?

5.- ¿Qué es una API?

6.- ¿Qué es Postman?

7.- ¿Qué es el polimorfismo?

8.- ¿Qué es un método dunder?

9.- ¿Qué es un decorador de python?

## 1.- Para que usamos las clases en Python?

En Python, una clase es una plantilla o modelo para la creación de objetos. Un objeto es una instancia de una clase, es decir, una versión específica de la plantilla que incluye sus propios valores y métodos.

**Para qué sirven las clases en Python?**

Las clases sirven para organizar el código y hacerlo más modular. Con las clases, podemos encapsular la lógica de nuestro programa en unidades lógicas y reutilizables. Además, las clases nos permiten heredar propiedades y métodos de otras clases, lo que nos permite crear jerarquías de objetos y reducir la cantidad de código que necesitamos escribir.

Las clases y los objetos sirven para crear tu propio tipo de datos (es decir, tipos de datos definidos por el usuario). Una clase es un tipo de dato definido por el usuario, y la crear instancias de una clase hace relación a la creación de objetos de ese tipo. Las clases y los objetos son considerados los principales bloques de desarrollo para Python, el cual es un lenguaje de programación orientado a objetos.

La estructura más simple sería de esta manera:

**class className: statements**

_Pasos sencillos para crear una clase:_

1.-**Las clases** la definimos utilizando la palabra clave class y className sería el nombre de la clase (identificador). Se recomienda que los nombres de las clases estén capitalizadas.

```
class person:

Para crear una instancia (objeto) de esta clase, simplemente se hace lo siguiente:

Jorge = Person()
```

Eso significa que hemos creado un nuevo objeto jorge del tipo Person, para crear un objeto solo se debe escribir el nombre de la clase, seguido de paréntesis.

2.- **Los atributos** son variables que pertenecen a la clase. Para definir un atributo, vamos a añadir a nuestra clase: name y school

```
class Person:
        name  = ¨ ¨
        School = ¨ ¨
```

3.- **Los métodos** son como funciones definidas en una clase que pueden ser llamadas en objetos de clase. En Python los métodos necesitan tener un argumento llamado self que se refiere al objeto del método que esta siendo llamado (name). Se pueden pasar más de un argumento al método.
Cuando queremos imprimir name

```Python
class Persona:

def init(self, nombre, edad):
self.nombre = nombre
self.edad = edad

    def saludar(self):

print(f"Hola, mi nombre es {self.nombre}")
```

El inicializador con nombre **init**(el método se considera especial por eso tiene subrayados dobles al principio y al final.) Este método se llama automáticamente cuando se crea un objeto de la clase.

_El parámetro self:_

En Python, el parámetro self se utiliza para referirse a la instancia actual de una clase. Permite acceder a las propiedades y métodos de esa instancia. Es una convención utilizar el nombre self para este parámetro, pero podrías usar cualquier nombre que elijas.

```Python
class Persona:
def init(self, nombre):
self.nombre = nombre

persona = Persona("Alice")
print(persona.nombre) # salida: Alice
```

Definir una clase en Python significa crear un nuevo objeto con atributos y métodos que nos permitirán dar estructura y sentido a nuestro código. Al crear una clase en Python, podemos definir objetos que tiene un estado específico y un comportamiento propio. A través de la utilización de clases, podemos reutilizar código, evitar repeticiones y omitir errores innecesarios.

Como un ejemplo práctico, pensemos en un programa que necesita llevar el control de estudiantes que han inscrito algunas materias. De manera básica, podríamos pensar en el uso de listas para representar los estudiantes, sus notas y la materia que están cursando. Sin embargo, esto puede ser complicado de manejar y poco práctico si queremos agregar más funcionalidades al mismo programa. Es aquí donde entra la creación de clases.

Para comenzar a trabajar en nuestro ejemplo, primero debemos definir una clase estudiante que tenga atributos como nombre, edad y materia. Además, también es importante agregar métodos que nos permitan acceder y modificar estos atributos de manera dinámica. Esto nos permite contar con una estructura organizada para manejar la información que genera dicho objeto y facilitar la adición de nuevas funcionalidades.

```Python
class Estudiante:
  def init(self, nombre, edad, materia, calificacion):
    self.nombre = nombre
    self.edad = edad
    self.materia = materia
    self.calificacion = calificacion

  def definir_materia(self, nueva_materia):
    self.materia = nueva_materia

  def definir_calificacion(self, nueva_calificacion):
    self.calificacion = nueva_calificacion
```

En este ejemplo, se define la clase Estudiante que tiene los métodos definir_materia y definir_calificación. Además, cada objeto de tipo Estudiante tiene atributos como nombre, edad, materia y calificación que los caracterizan.

Otro ejemplo que agregaremos subclases heredadas como Perro y Gato. Cada una de estas subclases tendrá una serie de atributos y comportamientos específicos para el tipo de animal que representan.

```Python
class Animal:
    "Definición de la superclase Animal"
    def __init__(self, nombre, edad, tipo, especie, color):
        self.nombre= nombre
        self.edad = edad
        self.tipo = tipo
        self.especie = especie
        self.color = color


class Perro(Animal):
    "Definición de la subclase Perro"
    def ladrar(self):
        print("Guau! Guau!")


class Gato(Animal):
    "Definición de la subclase Gato"
    def maullar(self):
        print("Miau! Miau!")
```

En este ejemplo, estamos definiendo las subclases **Perro** y **Gato**, que heredan atributos y comportamientos de la clase Padre Animal. Además, cada una de estas subclases tiene un método específico que los caracteriza.

Usar objetos nos ayuda a estructurar mejor nuestro código y reducir la complejidad.
Al hablar de clases en Python, estamos hablando de la creación de objetos. Un objeto es una entidad en el código que tiene ciertas propiedades y métodos. Las clases son la plantilla para crear objetos y nos permiten definir las propiedades y métodos que tendrá cualquier objeto creado a partir de dicha clase.

Por ejemplo, imaginemos que estamos escribiendo un programa para una tienda en línea. Podríamos crear una clase llamada “Producto”, que definiría las propiedades que tendría cualquier producto en la tienda, como su nombre, descripción, precio, etc. Luego, podríamos crear objetos a partir de esta clase, cada uno representando un producto en particular.

```Python
class Producto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


producto1 = Producto("Camiseta", "Una camiseta de algodón", 10.99)
producto2 = Producto("Zapatillas", "Zapatillas deportivas", 49.99)
```

**_Ahora veremos por que la creación de objetos nos ayuda a estructurar mejor nuestro código y reducir la complejidad:_**

**En primer lugar**, las clases nos permiten organizar nuestro código de manera más clara y ordenada. Al agrupar propiedades y métodos relacionados dentro de una clase, podemos encontrar más fácilmente lo que buscamos en el código.

**En segundo lugar**, al crear objetos a partir de una clase, estamos aprovechando la reutilización de código. Si necesitamos crear varios objetos que tengan las mismas propiedades y métodos, no tenemos que copiar y pegar el mismo código una y otra vez. En su lugar, podemos simplemente crear nuevos objetos a partir de la misma clase.

**Por último**, el uso de objetos nos ayuda a reducir la complejidad del código. Al agrupar propiedades y métodos relacionados en un solo objeto, estamos haciendo que sea más fácil entender ese objeto y las acciones que puede realizar. Además, al crear múltiples objetos con diferentes propiedades, podemos manejar mejor la complejidad del programa en general.

En resumen, las clases son una herramienta fundamental en la programación orientada a objetos y en Python en particular, su dominio es esencial para cualquier programador en Python.. Utilizando las clases, podemos crear objetos que encapsulan la lógica de nuestro programa y nos permiten crear aplicaciones escalables y modulares.

## 2.- ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

Un **método constructor** es un método especial que se ejecuta automáticamente cuando se crea una nueva instancia de una clase. Este método se utiliza principalmente para inicializar los atributos del objeto recién creado con valores predeterminados o personalizados. En Python, el método constructor se define mediante el método **init**

Comprender cómo funcionan los constructores no solo facilita la organización del código, sino que también mejora la legibilidad y la mantenibilidad de las aplicaciones desarrolladas en Python.

La importancia de los constructores radica en su capacidad para garantizar que los objetos se creen con un estado coherente y válido. Un constructor bien diseñado puede hacer que el código sea más fácil de entender y mantener, ya que encapsula la lógica de inicialización en un solo lugar.

Algunas de las ventajas de utilizar constructores son:

- Facilitan la creación de objetos con configuraciones específicas.

- Permiten establecer valores predeterminados para atributos.
- Contribuyen a la encapsulación y mejoran la legibilidad del código.

Los constructores pueden aceptar parámetros que permiten personalizar aún más la creación del objeto. Esto significa que se puede instanciar la misma clase de diferentes maneras, lo que aumenta la flexibilidad del diseño del software. Al utilizar constructores, los desarrolladores pueden crear aplicaciones más robustas y menos propensas a errores, lo que resulta en un código más eficiente y fácil de mantener.

Además de inicializar atributos, los constructores pueden tener lógica adicional, como validaciones.

En este sentido, es importante seguir algunas buenas prácticas al definir un constructor:

- **Claridad:** Asegúrate de que los nombres de los parámetros sean descriptivos.
- **Flexibilidad**: Proporciona valores predeterminados para parámetros opcionales.
- **Documentación:** Incluye comentarios o docstrings que expliquen la finalidad y uso del constructor.

![](https://www.luisllamas.es/images/20379/programacion-constructor.webp)

_Sintaxis del Metodo Constructor:_

```Python
class NombreDeLaClase:
    def __init__(self, parametros):
        # Inicialización de atributos
        self.atributo1 = valor1
        self.atributo2 = valor2
        # Más inicializaciones si es necesario
```

**Ejemplo básico de constructor:**

```Python
Definición de una clase con constructor:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Creación de instancias utilizando el constructor:
persona1 = Persona("Luis", 30)
persona2 = Persona("María", 25)

Acceso a los atributos de las instancias:
print(persona1.nombre, persona1.edad) Salida: Luis 30
print(persona2.nombre, persona2.edad) Salida:María 25
```

En este ejemplo,
**init**(self, nombre, edad) es el constructor de la clase Persona, cuando se crea una nueva instancia (persona1 y persona2) Python automáticamente llama a **init**() y pasa los argumentos nombre y edad proporcionados.

### Parámetros del constructor

El primer parámetro de **init**() es self, que representa la instancia actual de la clase. Se utiliza para acceder a los atributos y métodos de la instancia dentro del propio método y en otros métodos de la clase.

Si no se define un constructor (**init**()), Python proporciona uno por defecto que no inicializa ningún atributo.
Además de self, el constructor puede aceptar cualquier número de parámetros necesarios para inicializar la instancia. Estos parámetros son proporcionados al crear la instancia.

### Tipos de constructores

Existen otros tipos de constructores que pueden ser útiles en diferentes contextos.
Uno de los tipos de constructores menos comunes es el constructor de clase, definido mediante el método **new**. Este método se invoca antes de **init** y se utiliza principalmente para crear instancias de clases. Es útil en situaciones donde se necesita personalizar la creación de un objeto, como en el caso de patrones de diseño como el Singleton. A continuación, se muestran algunas aplicaciones de **new**:

- Controlar la creación de instancias de una clase.
- Implementar el patrón Singleton.
- Realizar la creación de objetos inmutables.

Otro tipo de constructor en Python es el constructor de clase, que se define con el decorador @classmethod. Este constructor permite crear instancias de la clase utilizando métodos que no son necesariamente el constructor principal. Esto es útil para crear instancias a partir de datos alternativos, como archivos o bases de datos. Algunas aplicaciones de los constructores de clase son:

- Crear instancias a partir de datos en formatos específicos.
- Implementar métodos de fábrica que simplifican la creación de objetos.
- Ofrecer diferentes formas de instanciar una clase según el contexto.

Finalmente, los constructores estáticos, implementados con el decorador @staticmethod, permiten definir métodos que no dependen del estado de la instancia o de la clase. Aunque no son constructores en el sentido tradicional, pueden ser utilizados para crear instancias de clase de manera más flexible. Esto es particularmente útil cuando se desea encapsular la lógica de creación en un método separado. Algunas aplicaciones de los métodos estáticos incluyen:

- Crear instancias a partir de datos estáticos.
- Proporcionar utilidades de creación que no requieren acceso a atributos de instancia.
- Mejorar la legibilidad del código al separar la lógica de creación de la lógica de negocio.

### Mejores prácticas para el uso de constructores en Python

- Una de las mejores prácticas al utilizar constructores es asegurarse de que todos los parámetros necesarios se pasen en el momento de la creación del objeto. Esto garantiza que el objeto esté completamente inicializado y en un estado válido. Evitar valores por defecto innecesarios también ayuda a prevenir la creación de instancias con atributos incompletos.

- Otra práctica recomendada es mantener el constructor lo más simple y claro posible. Esto significa que no deberías incluir lógica compleja o cálculos dentro del **init**. En su lugar, se recomienda delegar esas tareas a métodos separados. De esta manera, el constructor se enfoca exclusivamente en la inicialización del objeto, lo que facilita la lectura y el mantenimiento del código.

- Además, es conveniente utilizar anotaciones de tipo en los parámetros del constructor. Esto no solo mejora la legibilidad del código, sino que también proporciona información adicional sobre los tipos de datos esperados, lo que puede ayudar en el desarrollo de software más robusto.

Por ejemplo:

_Definir tipos de datos específicos para cada parámetro._

_Utilizar docstrings para documentar el propósito de cada parámetro y el comportamiento del constructor._

- Por último, es importante considerar la implementación de métodos especiales como **str** y **repr** para proporcionar representaciones legibles de los objetos. Esto no solo facilita la depuración, sino que también mejora la interacción con otros desarrolladores, ya que les permite entender rápidamente el propósito y el estado del objeto. Al seguir estas mejores prácticas, podrás crear clases más efectivas y mantener un código más limpio y comprensible en tus proyectos de Python.

- Un ejemplo práctico de su uso se puede observar en la creación de una clase de Usuario. Al definir el constructor, podemos asignar atributos como el nombre, la edad y el correo electrónico al momento de instanciar un nuevo objeto. Esto permite que cada instancia de la clase tenga características únicas desde el principio.

Otro caso de uso común es en la creación de clases que gestionan conexiones a bases de datos. Mediante un constructor, podemos establecer parámetros como el nombre de la base de datos, el usuario y la contraseña. Un ejemplo de esto podría incluir:

1. Conexión a una base de datos SQLite para una aplicación pequeña.
2. Configuración de parámetros de conexión para bases de datos SQL como MySQL o PostgreSQL.
3. Inicialización de un cliente para conectar a APIs externas.

## 3.- ¿Cuáles son los tres verbos de API?

Una **API** es un conjunto de reglas y estándares que permite a dos sistemas comunicarse entre sí de manera eficiente. En el contexto de desarrollo web, una API facilita la interacción entre un cliente (como una aplicación o sitio web) y un servidor, permitiendo el intercambio de datos de forma estructurada.

La API utiliza los métodos estándar de HTTP (GET, POST, PUT, DELETE) para realizar operaciones específicas. Es crucial utilizar el método correcto en cada solicitud para garantizar la integridad de los datos y la seguridad de la operación.

**¿Qué son los verbos HTTP?**

Son aquellos verbos propios del protocolo HTTP que fueron tomados para definir operaciones muy puntuales y específicas sobre los recursos de la API.

Los tres verbos de API más comunes son:

**GET** : Se utiliza para solicitar información del servidor.

**POST** : Se utiliza para enviar información al servidor.

**PUT** : Se utiliza para actualizar un recurso existente en el servidor.

#### GET

El método GET recupera la representación/información del recurso solamente. Es seguro y se puede almacenar en caché.
GET es el que usamos para consultar un recurso. Una de las principales características de una petición GET es que no debe causar efectos secundarios en el servidor, no deben producir nuevos registros, ni modificar los ya existentes. A esta cualidad la llamamos idempotencia, cuando una acción ejecutada un número indefinido de veces, produce siempre el mismo resultado.

Esto quiere decir, que no importa cuántas veces hagamos una petición GET, los resultados obtenidos serán los mismos.

#### POST

El método POST se utiliza para enviar datos a un servidor para crear un recurso. No es ni seguro.
Las peticiones con POST son sólo para crear recursos nuevos. Cada llamada con POST debería producir un nuevo recurso.

Normalmente, la acción POST se dirige a una recurso que representa una colección, para indicar que el nuevo recurso debe agregarse a dicha colección, por ejemplo POST /cursos para agregar un nuevo recurso a la colección cursos.

Algunos escenarios más complejos para el uso de POST son los inicios de sesión, agregar a un carrito de compras, procesar un pago nuevo, etc. Estos ejemplos nos dejan en claro que el recurso creado por POST no es precisamente una fila en la base de datos, el recurso puede ser una sesión, un pago en una API externa, etc.

    Ejem:
    POST /users
    Esto creará un nuevo usuario.

#### PUT

El método PUT se utiliza para actualizar un recurso existente o crearlo si no existe. Es idempotente pero no seguro.
Los verbos PUT/PATCH son muy similares ya que ambos se usan para modificar un recurso existente. PUT se diferencía de PATCH, en que el primero indica que vamos a sustituir por completo un recurso, mientras que PATCH habla de actualizar algunos elementos del recurso mismo, sin sustituirlo por completo.

En la práctica, ambos verbos se usan para actualizar un recurso, sin importar si lo sustituimos parcial o totalmente.

    Ejem: PUT /users/123

Esto actualizará el usuario con el id 123 o creará un nuevo usuario con este id si aún no existe.

Un escenario común para el uso de PUT sería una llamada para actualizar la información de un curso, por ejemplo:

PUT /cursos/backend-profesional

O también:

PATCH /cursos/backend-profesional
En la práctica, y particularmente en Rails, ambos verbos se usan para actualizar un recurso, sin importar si lo sustituimos parcial o totalmente.

## 4.- Es MongoDB una base de datos SQL o NoSQL?

Cuando hablamos de MongoDB nos estamos refiriendo a un sistema de gestión de bases de datos de código abierto.
MongoDB es utilizado en una amplia variedad de aplicaciones y sectores debido a su capacidad de manejar datos no estructurados.

MongoDB es una base de datos NoSQL orientada a documentos que permite almacenar datos de una manera mucho más flexible que las bases de datos tradicionales relacionales. A diferencia de las bases de datos SQL, que organizan la información en tablas y filas, MongoDB almacena los datos en documentos JSON (JavaScript Object Notation), lo que facilita una estructura más natural para las aplicaciones modernas.

Mongo se utiliza en muchas compañías a lo largo del mundo para almacenar datos o para servir como base de datos en distintas aplicaciones. A su vez, se trata de un programa que puede ser útil para la creación de tiendas online e incluso para el diseño de aplicaciones.
En el caso de las aplicaciones, tenemos al caso particular de los videojuegos. Por lo general, aquellos que sean escalables y de alto rendimiento utilizan Mongo para el almacenamiento de sus datos.

![](https://miracomohacerlo.com/wp-content/uploads/2019/06/1124-3.jpg)

#### ¿Qué es SQL?

El lenguaje de consulta estructurada (SQL) es un lenguaje de programación para almacenar y procesar información en una base de datos relacional. Una base de datos relacional almacena información en forma de tabla, con filas y columnas que representan diferentes atributos de datos y las diversas relaciones entre los valores de datos. Puede usar las instrucciones SQL para almacenar, actualizar, eliminar, buscar y recuperar información de la base de datos. También puede usar SQL para mantener y optimizar el rendimiento de la base de datos.

#### ¿Qué es NoSQL?

NoSQL significa "No solo SQL" o "No SQL". Hay varios tipos de bases de datos NoSQL, como documento, clave-valor, gráfico, etc. La diferencia clave entre NoSQL y MongoDB es que NoSQL es un mecanismo para almacenar y recuperar datos en una base de datos no relacional y MongoDB es una base de datos orientada a documentos que pertenece a NoSQL.

Se refiere a bases de datos no relacionales que no usan tablas para almacenar datos. Las bases de datos de documentos se utilizan para datos dinámicos. Tales bases de datos son MongoDB. En estas bases de datos, los datos se almacenan en formato de notación de objetos de JavaScript (JSON).

Los desarrolladores almacenan información en diferentes tipos de bases de datos NoSQL, incluidos gráficos, documentos y valores clave. Las bases de datos NoSQL son populares para las aplicaciones modernas porque son escalables horizontalmente. El escalado horizontal consiste en aumentar la potencia de procesamiento al agregar más computadoras que ejecuten el software NoSQL.

#### Similitudes entre NoSQL y MongoDB??

- Ambos pueden manejar Big Data.
- Admite la escalabilidad horizontal sin hardware costoso.
- Apoya la arquitectura distribuida.
- Ambos no soportan uniones.
- Ambos no pueden manejar transacciones complejas.
- El esquema es dinamico.
- Flexible y fácil de usar.

#### Diferencias entre MongoDB y NoSQL

- NoSQL se utiliza para almacenar y recuperar datos en una base de datos no relacional. Puede ser de diferentes tipos, como base de documentos, almacén de valores clave, base de datos gráficos, etc

- MongoDB es una base de datos escalable, de alto rendimiento, orientada a documentos, que es un sistema de gestión de base de datos no relacional. Es una base de datos orientada a documentos.

**En resumen - NoSQL vs MongoDB**

Las bases de datos NoSQL tienen una arquitectura distribuida y pueden aumentar la consistencia de los datos. MongoDB es una base de datos de código abierto NoSQL. Proporciona escalabilidad y alto rendimiento. En el desarrollo ágil, los requisitos pueden cambiar, y MongoDB permite cambiar el esquema. La diferencia entre NoSQL y MongoDB es que NoSQL es un mecanismo para almacenar y recuperar datos en la base de datos no relacional y MongoDB es una base de datos orientada a documentos que pertenece a NoSQL.

![](https://datasciencedojo.com/wp-content/uploads/SQL-and-NoSQL-1030x1030.jpg)

## 5.- ¿Qué es una API?

Una API, o Interfaz de Programación de Aplicaciones, es un conjunto de reglas o protocolos que permite a las aplicaciones informáticas comunicarse entre sí para intercambiar datos, características y funcionalidades sin necesidad de conocer su implementación interna.

**_Ejemplo simple_**: Imagina que estás en un restaurante y el menú representa los servicios que puedes pedir. El camarero (**API**) recibe tu pedido, lo lleva a la cocina (servidor) y te trae la comida preparada. No necesitas saber cómo se cocina, solo te interesa recibir tu plato. Así funcionan las **APIs** en el mundo digital.

Las **APIs** permiten a los desarrolladores integrar funciones y datos de otras plataformas en sus aplicaciones, evitando la necesidad de construir todo desde cero.
Ya sea que uses una red social, realices un pago en línea o consultes un mapa, lo más probable es que detrás de esa acción haya una **API** trabajando.

Las **API** permiten compartir solo la información necesaria, manteniendo ocultos otros detalles internos del sistema, lo que ayuda a la seguridad del sistema. Los servidores o dispositivos no tienen que exponer completamente los datos: las **API** permiten compartir pequeños paquetes de datos, relevantes para la solicitud específica.

#### Como funcionan las API

Una manera sencilla de entender cómo funcionan las API es examinar un ejemplo común: el procesamiento de pagos de terceros. Cuando un usuario compra un producto en un sitio de comercio electrónico, es posible que se le pida que "pague con PayPal" u otro tipo de sistema externo. Esta función depende de las API para realizar la conexión, sin acceder directamente a los datos de la cuenta del usuario.

1. El cliente envía una solicitud a la API (por ejemplo, una aplicación solicita datos de una base de datos externa).
2. La API procesa la solicitud y la redirige al servidor adecuado.

3. El servidor responde con los datos o la acción solicitada.
4. La API transfiere la respuesta al cliente, que muestra la información al usuario final.

![](https://outvio.com/static/b649eefd687b1e175f6cb22298929902/1b4a6/cl2t0lc4l000w7b7t0yli356j.jpg)

![](https://www.container-loading.com/wp-content/uploads/2022/03/API-infographics-1024x536.png)

#### Tipos de APIs según su uso:

_API de datos_

Facilita el acceso a bases de datos para consultar, modificar o eliminar información.  
Ejemplo:  
API de Google Sheets para obtener datos en tiempo real.

_API de sistemas operativos_

Permite a las aplicaciones interactuar con los recursos del sistema operativo.
Ejemplo:
API de Windows para gestionar archivos.

_API remotas_

Permiten la comunicación entre aplicaciones en diferentes dispositivos o servidores.

Ejemplo:

API de WhatsApp Business para enviar mensajes desde un software externo.

_API web_

Son las más comunes y se utilizan para intercambiar datos a través de Internet mediante HTTP.

Ejemplo:

API de Google Maps para incrustar mapas en una web.

![](https://uploads-ssl.webflow.com/62e153e41d6ee298cc9a98f7/63becf42923e2bf220790838_APIS.png)

#### Tipos de APIs según su nivel de acceso:

_API abiertas (públicas)_

- Están disponibles para cualquier desarrollador sin restricciones estrictas.

Ejemplo:

API de Twitter para obtener tweets públicos.

_API de socios_

- Solo están accesibles para empresas o colaboradores autorizados.

Ejemplo:

API de Shopify para tiendas afiliadas.

_API internas (privadas)_

- Se usan dentro de una empresa para mejorar la comunicación entre sus sistemas internos.

Ejemplo:

API de Recursos Humanos para gestionar empleados.

_API compuestas_

- Combinan varias APIs en una sola solicitud para realizar tareas más complejas.

Ejemplo:

Una API que consulte datos bancarios y verifique la identidad en un solo proceso.

Las _APIs_ están en todas partes,desde aplicaciones móviles hasta plataformas de software empresarial, por ejemplo:

- Inicios de sesión universales: Usar Google o Facebook para iniciar sesión en una app sin crear una cuenta nueva.

- Comparadores de precios de vuelos: Agencias como Skyscanner usan APIs de aerolíneas para mostrar precios en tiempo real.

- Servicios de pago en línea: PayPal y Stripe permiten integrar pagos en tiendas virtuales mediante sus APIs.
- Plataformas de redes sociales: Instagram y Twitter ofrecen APIs para incrustar contenido en otras webs.
- Aplicaciones de navegación: Google Maps proporciona rutas y tráfico en tiempo real a través de su API.

![](https://edteam-media.s3.amazonaws.com/community/original/7dc50204-6f44-4000-bfe3-1d8677bab50c.jpg)

#### Ventajas de las APIs:

Las APIs simplifican el diseño y el desarrollo de nuevas aplicaciones y servicios, así como la integración y gestión de las existentes. También ofrecen beneficios significativos a los desarrolladores y a las organizaciones en general.

**_Colaboracion mejorada:_**

Las API permiten la integración, para que estas plataformas y aplicaciones puedan comunicarse entre sí sin problemas. Mediante esta integración, las empresas pueden automatizar los flujos de trabajo y mejorar la colaboración en el lugar de trabajo. Sin las API, muchas empresas carecerían de conectividad, lo que provocaría silos de información que comprometerían la productividad y el rendimiento.

**_Innovación acelerada:_**

Las API ofrecen flexibilidad, lo que permite a las empresas establecer conexiones con nuevos socios comerciales y ofrecer nuevos servicios a su mercado existente. Esta flexibilidad también permite a las empresas acceder a nuevos mercados que pueden aumentar los rendimientos e impulsar la transformación digital.

**_Monetización de datos:_**

Muchas empresas optan por ofrecer API gratuitas, al menos al principio, para poder crear una audiencia de desarrolladores en torno a su marca y forjar relaciones con posibles socios. Si la API da acceso a recursos digitales valiosos, una empresa lo monetiza vendiendo el acceso. Esta práctica se conoce como la economía API.

**_Seguridad del sistema:_**

Las API separan la aplicación solicitante de la infraestructura del servicio que responde y ofrecen capas de seguridad entre las dos a medida que se comunican. Por ejemplo, las llamadas a la API suelen requerir credenciales de autenticación. Los encabezados HTTP, cookies o cadenas de consulta pueden proporcionar seguridad adicional durante el intercambio de datos. Una puerta de enlace API puede controlar el acceso para minimizar aún más las amenazas a la seguridad.

**_Seguridad y privacidad del usuario:_**

Las API brindan protección adicional dentro de una red. También pueden proporcionar otra capa de protección para los usuarios personales. Cuando un sitio web solicita la ubicación de un usuario (una API de ubicación proporciona esta información), el usuario puede decidir si permite o rechaza esta solicitud.
Muchos navegadores web y sistemas operativos móviles y de escritorio tienen estructuras de permisos integradas. Cuando una aplicación debe acceder a los archivos a través de una API, los sistemas operativos como iOS, macOS, Windows y Linux utilizan permisos para ese acceso.

## 6.- ¿Qué es Postman?

Postman en sus inicios nace como una extensión que podía ser utilizada en el navegador Chrome de Google y básicamente nos permite realizar peticiones de una manera simple para testear APIs de tipo REST propias o de terceros.

Gracias a los avances tecnológicos, Postman ha evolucionado y ha pasado de ser de una extensión a una aplicación que dispone de herramientas nativas para diversos sistemas operativos como lo son Windows, Mac y Linux.

Gracias a su interfaz gráfica intuitiva, Postman facilita el proceso de prueba, desarrollo y documentación de servicios web, optimizando el flujo de trabajo y favoreciendo la colaboración entre equipos.

Con Postman, los desarrolladores pueden enviar peticiones HTTP (GET, POST, PUT, DELETE, entre otros). Si no tuviéramos algo como Postman necesitaríamos generar código del cliente, con Javascript y generalmente Ajax para poder realizar los request al servidor y probar todos esos métodos, ya que un navegador cuando accedemos a un recurso mediante su URL solo nos permite hacer un simple GET.

Esta herramienta no solo ahorra tiempo, sino que también reduce errores en la programación de aplicaciones que requieren comunicación constante con servicios externos.

### Características de Postman

**_Colecciones de solicitudes:_** Postman permite agrupar diferentes solicitudes en colecciones, lo cual facilita la organización de las pruebas y la reutilización de peticiones en distintos entornos de desarrollo.

**_Pruebas automatizadas:_** Utilizando JavaScript, Postman permite la creación de scripts personalizados para automatizar pruebas y validar respuestas. Esto es esencial para garantizar que los servicios web funcionen correctamente en diferentes etapas del ciclo de desarrollo.

**_Gestión de entornos:_** Postman permite crear y gestionar distintos entornos (desarrollo, pruebas, producción) para probar cómo se comportan las APIs en diferentes configuraciones. Esto proporciona una gran flexibilidad a la hora de realizar pruebas sin necesidad de cambiar manualmente los parámetros.

**_Generación de documentación:_** La documentación es fundamental para que otros desarrolladores comprendan cómo interactuar con una API. Postman genera automáticamente documentación a partir de las solicitudes y las respuestas, haciendo que sea más sencillo compartir los detalles de la API con el equipo.

#### **Ventajas:**

Postman se ha convertido en una herramienta indispensable gracias a sus múltiples ventajas. Estas facilitan la vida del desarrollador y mejoran la eficiencia en la gestión de APIs. Las más relevantes:

1. **_Interfaz gráfica intuitiva:_** Postman ofrece una interfaz amigable y fácil de usar, que permite a los desarrolladores ejecutar pruebas sin necesidad de escribir código complejo. La posibilidad de interactuar de manera visual con las APIs reduce significativamente la curva de aprendizaje y favorece la productividad.

2. **_Compatibilidad multiplataforma:_** Postman es compatible con diversos sistemas operativos y puede ejecutarse en cualquier lugar, lo cual permite a los desarrolladores trabajar de manera colaborativa y sin restricciones. Además, su capacidad para soportar múltiples protocolos, como HTTP, HTTPS, y GraphQL, lo convierte en una herramienta versátil.

3. **_Mejora en la colaboración:_** Postman fomenta la colaboración en los equipos de desarrollo al permitir compartir colecciones de solicitudes y entornos. Esto facilita la integración de todos los miembros del equipo y asegura que todos trabajen sobre la misma base, mejorando la coordinación.

4. **_Versión gratuita:_** Postman ofrece un plan gratuito con características suficientes para equipos pequeños y proyectos individuales. Aunque también tiene una versión premium, la opción gratuita sigue siendo muy potente para los desarrolladores que recién comienzan a trabajar con APIs.

5. **_Automatización y productividad:_** Postman permite automatizar tareas repetitivas, como la ejecución de pruebas o la generación de documentación, lo cual incrementa la productividad del equipo. Los desarrolladores pueden enfocarse en resolver problemas más complejos y mejorar la calidad del software.

#### Para que sirve Postman?

Exploramos para qué sirve esta herramienta y cómo se puede aprovechar al máximo en el contexto del desarrollo de software.

**Desarrollo y Prueba de APIs**

La herramienta permite enviar solicitudes HTTP a servicios web y analizar sus respuestas, lo que es esencial para verificar el correcto funcionamiento de los endpoints. Los desarrolladores pueden utilizar Postman para enviar solicitudes GET, POST, PUT, DELETE, entre otros métodos, y comprobar cómo responde la API en diferentes circunstancias.

Esto no solo ayuda a identificar errores o comportamientos inesperados, sino que también permite validar las funciones que se han implementado. Por ejemplo, al construir un servicio web, Postman puede utilizarse para verificar si la API devuelve los datos correctos cuando se le proporcionan entradas específicas.

**Automatización de Pruebas**

Postman permite la automatización de pruebas, una función sumamente valiosa en entornos de desarrollo ágil. Los desarrolladores pueden escribir scripts de prueba utilizando JavaScript para automatizar la validación de las respuestas recibidas. Esta capacidad es particularmente útil para realizar pruebas de regresión, asegurando que nuevas funcionalidades no afecten negativamente el comportamiento existente de la API.

**Documentación de APIs**

La documentación generada por Postman incluye detalles de las solicitudes realizadas, ejemplos de respuestas y descripciones de los endpoints. Esta documentación interactiva es muy útil para los equipos de desarrollo y facilita la comprensión del funcionamiento de la API a otros desarrolladores o colaboradores del proyecto.
La documentación puede compartirse online, permitiendo que cualquier miembro del equipo acceda a ella y la consulte según sea necesario.

**Colaboración en Equipos de Desarrollo**

Los equipos que trabajan en proyectos grandes y distribuidos pueden compartir colecciones de solicitudes, entornos de pruebas y los resultados obtenidos. Esta funcionalidad ayuda a que todos los miembros del equipo trabajen de manera coordinada y eficiente, evitando errores y asegurando que todos estén alineados respecto al comportamiento y evolución de la API.

**Pruebas de Integración Continua**

Las pruebas automatizadas de APIs pueden integrarse con herramientas de CI/CD para verificar cada cambio realizado en el software, lo cual asegura que el nuevo código no afecte negativamente al funcionamiento del sistema. Gracias a las integraciones de Postman con herramientas populares de automatización, los equipos pueden implementar un flujo de trabajo que permita la prueba continua y el despliegue ágil del software.

#### Como usar Postman:

Descarga e Instalación de Postman: Postman está disponible para varias plataformas, incluidas Windows, Mac, y Linux. Para comenzar, debes visitar el sitio web oficial de Postman y descargar la versión correspondiente a tu sistema operativo. Tras la descarga, la instalación es un proceso rápido y directo, guiado por un asistente que te ayudará a configurarlo en unos minutos.

**_Crear una Nueva Colección:_** Las colecciones son esenciales porque permiten organizar múltiples solicitudes relacionadas en un solo lugar. Para crear una nueva colección, basta con abrir Postman y hacer clic en el botón de "New" en la parte superior de la interfaz. Selecciona "Collection" y asigna un nombre descriptivo para identificarlo fácilmente en el futuro.

![](https://desarrolloweb.com/media/190/new-collection.jpg)

**_Hacer una Solicitud HTTP:_** Selecciona la colección creada previamente y haz clic en "Add Request". Podrás especificar el nombre de la solicitud y el tipo de método HTTP que deseas usar, como GET, POST, PUT, o DELETE. Para realizar una solicitud HTTP con Postman, necesitarás ingresar la URL del endpoint al que deseas acceder.

![](https://desarrolloweb.com/media/189/new-request.jpg)

**_Configuración del Cuerpo de la Solicitud:_** Dependiendo del tipo de solicitud HTTP que vayas a realizar, deberás configurar el cuerpo (body) de la solicitud. Postman te permite seleccionar el tipo de contenido y añadir la información que necesita la API. El cuerpo puede ser de diferentes tipos: raw, form-data, o x-www-form-urlencoded.

![](https://desarrolloweb.com/media/185/pestana-body.jpg)

**_Enviar la Solicitud y Revisar la Respuesta:_** Una vez que hayas configurado la solicitud, puedes enviarla al servidor haciendo clic en el botón "Send". Postman mostrará la respuesta en la parte inferior de la ventana, donde podrás revisar los códigos de estado, encabezados y el contenido del cuerpo de la respuesta.

![](https://desarrolloweb.com/media/181/boton-send.jpg)

**_Uso de Variables y Entornos:_** Las variables te permiten parametrizar diferentes partes de las solicitudes, como las URLs, encabezados o tokens de autenticación, y cambiar rápidamente entre distintos entornos (por ejemplo, desarrollo, pruebas y producción). Para definir un entorno, solo debes hacer clic en "Environments" y configurar las variables según sea necesario.

#### Conclusión

Postman es una herramienta que sirve de gran ayuda al equipo de desarrollo, permitiendo mantener las colecciones actualizadas, ahorrando los tiempos de respuesta al momento de realizar los test o las llamadas a los servicios. Es potente gracias a su fácil integración con APIs de terceros y cuenta con una gran comunidad.

## 7.- Qué es el polimorfismo?

Uno de los conceptos más importantes en POO es el polimorfismo.

El polimorfismo es el último pilar que nos falta por ver de la programación orientada a objetos. Lo cual es una definición muy teórica pero poco práctica. Dicho de otra forma: Es una forma muy compleja de decir que un alcalde es una persona.

El concepto de polimorfismo es en realidad algo muy básico. Realmente, cuando estamos aprendiendo Programación Orientada a Objetos (también conocida por sus siglas POO / OOP) muchos estudiantes nos hacemos un embolado tremendo al tratar de entender el concepto, pero en su base es algo extremadamente sencillo.

El polimorfismo es una técnica en la programación orientada a objetos que permite que los objetos de diferentes clases respondan a un mismo mensaje de diferentes maneras. Esto significa que el mismo método puede tener diferentes comportamientos según la clase del objeto que lo recibe.
El polimorfismo permite crear una jerarquía de clases relacionadas que se comportan de manera diferente pero que comparten una interfaz común. Esto hace que el código sea más fácil de mantener y actualizar, ya que se puede agregar una nueva clase sin afectar el código existente.

### De donde viene el polimorfismo?

Vamos a ver los motivos que llevaron a inventar el polimorfismo. Recordemos que la gente ya hacia agrupaciones de datos. Pero si cualquier para del programa podía modificarlos, se montaban unos líos muy interesantes e inmantenibles.

![](https://www.luisllamas.es/images/20365/pilares-oop.webp)

Asi que inventaron la **ENCAPSULACION**. A estar encapsuladas, cada clase tenía que ser independiente, lo cual obligaba a tener mucho código duplicado. Para permitir reaprovechar código se introduce la **HERENCIA**.

Pero con la herencia por si sola, no evitamos del todo tener que repetir código. Para evitar esto se introduce el **POLIMORFISMO.**

**_En resumen:_**

- La encapsulación impide que me toquen los objetos de forma incontrolada.

- La herencia permites que no tenga que repetir el código de las clases.
-
- El polimorfismo completa la herencia, y me permite no tener que repetir el código de lo que usa mis clases (colecciones, funciones)

#### **Como funciona el polimorfismo**

Para terminar de ver el polimorfismo, necesitamos hablar de como se comporta un objeto cuando ocupa una variable de otro tipo que no es el suyo propio. «Para esto
Tenemos que recordar que las clases hijas, ademas de heredar propiedades y métodos que tienen sus padres, pueden sobrescribir algunos o todos ellos.

Por ejemplo:  
Supongamos que Fruta y Manzana tienen un método muy sencillo que escribe en consola su nombre. «Fruta» y «Manzana» respectivamente.

```Python
class Fruta
{
    DiTuNombre() { console.write("Fruta") }
}

class Manzana extends  Fruta
{
	// sobreescribo el método
    DiTuNombre() { console.write("Manzana") }
}
```

Lo que queremos saber es que pasa cuando jugamos a meter objetos de un tipo en otro tipo. Tenemos los tres supuestos válidos.

```Python

Fruta miFruta = new Fruta();
miFruta.DiTuNombre();
    imprime "Fruta"


Naranja miNaranja = new Naranja();
miNaranja.DiTuNombre();
    imprime "Naranja"

aquí el lio, naranja como fruta
Fruta miNaranjaFruta = new Naranja();
miNaranjaFruta.DiTuNombre();
    POLIMORFISMO, imprime "Naranja"
```

#### **Relación entre polimorfismo y herencia**

Si quieres entender bien el concepto de polimorfismo, es sumamente necesario que comprendas la herencia en POO. Lo que permite la herencia es que una clase hija herede las propiedades y los métodos de una clase padre. Entonces, el polimorfismo entra en acción cuando un objeto de una clase hija es tratado como si fuera un objeto de la clase padre.

**Por ejemplo**, imagina que tienes una clase base Instrumento y varias clases derivadas como Guitarra, Piano y Batería. Lo que puedes hacer con el polimorfismo es crear una lista de Instrumentos y llenar esa lista con instancias de Guitarra, Piano y Batería, tratándolas todas como Instrumentos pero permitiendo que cada una actúe de acuerdo a su propia implementación.

#### **Tipos de polimorfismo**

Hay dos tipos principales de polimorfismo:

**1.- Polimorfismo de sobrecarga:** La sobrecarga de métodos es una técnica que permite que una clase tenga varios métodos con el mismo nombre, pero con diferentes parámetros. En tiempo de compilación, el compilador identifica el método adecuado a partir de los parámetros utilizados.

**2.-Polimorfismo de sobreescritura:** La sobreescritura de métodos es una técnica que permite que una subclase redefina un método de su superclase. Esto significa que el método de la subclase reemplaza al método de la superclase y se ejecuta en su lugar cuando se llama al método.

**_Ejemplo de polimorfismo_**

Supongamos que tenemos una clase Animal y dos subclases: Perro y Gato. Ambas subclases tienen un método llamado «sonido» que devuelve el sonido que hace cada animal. El código se vería así:

```Python
class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau guau"

class Gato(Animal):
    def sonido(self):
        return "Miau miau"
```

En este ejemplo, Animal es la clase base y Perro y Gato son las subclases. La clase Animal tiene un método llamado «sonido» que no hace nada. Las subclases Perro y Gato sobrescriben el método «sonido» y lo hacen suyo. Cada vez que llamamos al método «sonido» en un objeto Perro, se devolverá «Guau guau». Y cada vez que llamamos al método «sonido» en un objeto Gato, se devolverá «Miau miau».

![](https://image1.slideserve.com/2008135/polimorfismo-definici-n-l.jpg)

#### **Polimorfismo en Python**

Aunque en Python el polimorfismo funciona de manera muy similar, este lenguaje no requiere una jerarquía de clases estricta para aplicarlo, porque es dinámico. Te lo explico de manera más simple: piensa que tienes dos clases, Pájaro y Avión, ambas con un método volar(). A pesar de no tener una clase base común, lo que hace Python es dejar que ambas clases compartan un método con el mismo nombre y lo llamen de manera polimórfica. Queda algo así:

```Python
class Pajaro:
    def volar(self):
        return "El pájaro está volando."

class Avion:
    def volar(self):
        return "El avión está volando."

def hacer_volar(objeto):
    print(objeto.volar())

pajaro = Pajaro()
avion = Avion()

hacer_volar(pajaro)  # Output: El pájaro está volando.
hacer_volar(avion)   # Output: El avión está volando.
```

En este ejemplo, la función hacer_volar() es capaz de manejar objetos de diferentes clases (Pajaro y Avion) siempre que estos implementen el método volar(). Esto es polimorfismo en acción, y demuestra cómo Python puede aplicar este concepto sin necesidad de una jerarquía de clases.

![](https://static.platzi.com/media/user_upload/Polimorfismo-82226ef4-19ab-4369-ade4-4234ef0eeac9.jpg)

Finalmente en Python podemos definir nuestra clase Fruta con un método di_tu_nombre(). Luego creamos una subclase Naranja que hereda de Fruta y sobreescribe di_tu_nombre()

```Python
# Definición de la clase base Fruta
class Fruta:
    # Método virtual que muestra información genérica de la fruta
    def di_tu_nombre(self):
        return "Soy una fruta"

# Definición de la subclase Naranja que hereda de Fruta
class Naranja(Fruta):
    # Método sobreescrito que muestra información específica de la naranja
    def di_tu_nombre(self):
        return "Soy una naranja"

# Crear instancias de Fruta y Naranja
fruta = Fruta()
naranja = Naranja()

# Llamar al método di_tu_nombre() en ambas instancias
print(fruta.di_tu_nombre())  # Output: Soy una fruta
print(naranja.di_tu_nombre())  # Output: Soy una naranja
```

#### **El beneficio del polimorfismo**

El polimorfismo nos permite escribir un código más limpio y más fácil de mantener. En lugar de tener que escribir un método separado para cada subclase, podemos utilizar un método genérico que se puede aplicar a todas las subclases. Esto hace que nuestro código sea más modular y menos propenso a errores. Además, podemos agregar nuevas subclases sin tener que modificar el código existente.

#### **Conclusión**

El polimorfismo es una técnica poderosa en la programación orientada a objetos que permite que diferentes objetos de diferentes clases respondan a un mismo mensaje de diferentes maneras. Esto nos permite escribir un código más modular y fácil de mantener. En el ejemplo anterior, podemos ver cómo la sobrescritura de métodos nos permite reutilizar el código de la clase base para todas las subclases. En general, el polimorfismo es una de las características más importantes de la programación orientada a objetos.

## 8.- ¿Qué es un método dunder?

En Python, los métodos Dunder (abreviatura de «double underscore») son aquellos cuyo nombre comienza y termina con dos guiones bajos (\_\_).

Estos métodos no se llaman directamente, sino que son invocados automáticamente por el intérprete de Python en diversas situaciones (como operaciones aritméticas, manipulación de secuencias y gestión del contexto). Estos métodos son especiales en Python por que permiten personalizar clases y objetos. Estos métodos se llaman mágicos porque pueden cambiar el comportamiento del código de forma inesperadas, mejora enormemente la funcionalidad y flexbilidad del programa de Python.

**_Algunos de los métodos dunder mas comunes son:_**

```
__init__	:Inicializa una nueva instancia de una clase.

__str__	:Devuelve un string de un objeto, amigable para el usuario

__repr__	:Devuelve una string de un objeto, amigable para el desarrollador

__len__	:Devuelve la longitud de un objeto

__getitem__ :Permite acceder a elementos mediante índices

__setitem__ :Permite asignar valores a elementos mediante índices

__delitem__ : Permite eliminar elementos mediante índices

__iter__	:Devuelve un iterador para el objeto

__Next__	:Devuelve el siguiente elemento del iterador
```

### _Implementación de Métodos Dunder_

Veamos cómo se implementan y utilizan algunos de estos métodos en una clase en Python.

**Método _init _**

El método **init** se utiliza para inicializar los atributos de una clase cuando se crea una nueva instancia.

```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Alice", 30)
print(persona1.nombre)  # Salida: Alice
print(persona1.edad)    # Salida: 30
```

**Métodos _str _ y _repr _**

Los métodos **str** y **repr** devuelven representaciones en cadena de un objeto. La diferencia principal es que **str** está destinado a una representación amigable para el usuario, mientras que **repr** está orientado a los desarrolladores y debe ser más detallado.

```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

persona1 = Persona("Alice", 30)
print(str(persona1))  # Salida: Persona: Alice, 30 años
print(repr(persona1)) # Salida: Persona('Alice', 30)
```

**Método _len _**

El método **len** se utiliza para devolver la longitud de un objeto.

```Python
class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros

    def __len__(self):
        return len(self.miembros)

grupo = Grupo(["Alice", "Bob", "Charlie"])
print(len(grupo))  # Salida: 3
```

**_Métodos getitem, setitem y delitem_**

Estos métodos permiten que los objetos de una clase se comporten como contenedores (listas, diccionarios, etc.).

```Python
class MiLista:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

mi_lista = MiLista()
mi_lista.data = [1, 2, 3, 4, 5]
print(mi_lista[2])   # Salida: 3
mi_lista[2] = 30
print(mi_lista[2])   # Salida: 30
del mi_lista[2]
print(mi_lista.data) # Salida: [1, 2, 4, 5]
```

**_Métodos iter y next_**

Estos métodos permiten que los objetos de una clase sean iterables.

```Python
class Contador:
    def __init__(self, max):
        self.max = max
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < self.max:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

contador = Contador(5)
for numero in contador:
    print(numero)
```

#### **Métodos Dunder para operaciones aritméticas**

Además de los métodos mencionados, Python permite sobrecargar operadores aritméticos usando métodos dunder como **add**, **sub**, **mul**, **truediv**, entre otros.

```Python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Salida: Vector(6, 8)
```

Este método dunder es útil para liberar recursos como archivos, conexiones de red, u otros objetos a nivel de sistema que no son gestionados automáticamente por Python.

```Python
class MyClass:
    def __init__(self):
        self.file = open('example.txt', 'r')

    def __del__(self):
        self.file.close()
```

En este ejemplo, el constructor MyClass crea un objeto fichero y lo almacena en la variable de instancia file. Cuando se destruye el objeto, se llama al método **del**, que cierra el fichero.

## 9.- ¿Qué es un decorador de python?

Los decoradores son funciones que modifican el comportamiento de otras funciones, ayudan a acortar nuestro código y hacen que sea más Pythonic. Si alguna vez has visto @, estás ante un decorador o decorator, bien sea uno que Python ofrece por defecto o uno que puede haber sido creado ex profeso.

En Python, un decorador es una función que recibe otra función como argumento y devuelve una nueva función que, generalmente, extiende el comportamiento de la original.
Se utilizan ampliamente para aspectos transversales como la autenticación, el registro (logging), y la validación, entre otros.

```
Sintaxis básica:
@un_decorador
def mi_funcion():
 # realizar alguna tarea
 return algo
```

### **Decoradores con argumentos**

Los decoradores también pueden aceptar argumentos. Para hacerlo, se necesita anidar funciones:
Una función externa para aceptar los argumentos del decorador
Una función interna que acepte la función que será decorada.

**Por ejemplo:**

```Python
def repetir(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir(3)
def decir_adios():
    print("Adiós!")

decir_adios()

# Salida:
# Adiós!
# Adiós!
# Adiós!
```

En este caso,repetir es un decorador que acepta un argumento **n** Este repite la ejecución de la función decorada **n** veces

### **Decoradores en múltiples niveles**

Python permite anidar decoradores, aplicando múltiples decoradores a una misma función.

**Por ejemplo:**

```Python
def decorador1(func):
    def envoltura():
        print("Decorador 1 antes")
        func()
        print("Decorador 1 después")
    return envoltura

def decorador2(func):
    def envoltura():
        print("Decorador 2 antes")
        func()
        print("Decorador 2 después")
    return envoltura

@decorador1
@decorador2
def funcion():
    print("Función ejecutándose")

funcion()

# Salida:
# Decorador 1 antes
# Decorador 2 antes
# Función ejecutándose
# Decorador 2 después
# Decorador 1 después
```

En este ejemplo, función está decorada primero por **decorador2** y luego por **decorador1**, mostrando cómo se puede encadenar múltiples decoradores.

### **Conceptos en los que se basan los decoradores**

El funcionamiento de los decoradores se basa en tres ideas que vamos a desarrollar a continuación y que son las siguientes:

- Dentro de una función se pueden crear más funciones
- Las funciones pueden retornar funciones
- Las funciones se pueden pasar como argumentos a otras funciones

### **Estructura de un decorador**

Un decorador se compone de las tres ideas que acabamos de ver. Es decir, acepta una función como argumento y define una función interior la cual retorna. Además, dentro de la función interior ejecuta la función que se le ha pasado como argumento. Esto, que puede sonar algo confuso, traducido a código Python queda tal que así:

```Python
def mi_decorador(funcion_original):
 def funcion_envolvente():
    print("Código antes de la funcion_original()")

 funcion_original()
    print("Código después de la funcion_original()")

 return funcion_envolvente

Ahora definamos una función que vamos a pasarle a mi_decorador():

def funcion_necesita_decorador():
    print("¡Quiero que me decoren!")
```

Si pasamos la función anterior al decorador definido arriba, guardamos la función retornada por el decorador en una variable y ejecutamos dicha función obtenemos el siguiente resultado:

```
funcion_decorada = mi_decorador(funcion_necesita_decorador)
 funcion_decorada()
Código antes de la funcion_original()
¡Quiero que me decoren!
Código después de la funcion_original()
```

Tal y como veíamos en la definición del inicio de ese artículo, en este último paso, hemos añadido funcionalidad extra a una función sin necesidad de añadir dicha funcionalidad explícitamente.

En otras palabras, hemos envuelto o “decorado” una función con nueva funcionalidad dejando dicha función intacta, ya que el código que hemos añadido está en el decorador. Si queremos añadir o quitar dicha funcionalidad a la función, basta con añadirle o quitarle el decorador.

En Python la asignación que hemos realizado en la primera línea del código anterior se realiza con el signo @. Es decir, que esa asignación es equivalente a realizar lo siguiente:

```Python
@mi_decorador
def funcion_necesita_decorador():
 print("¡Quiero que me decoren!")
```

De este modo el código queda muy limpio y fácil de entender. Además, podemos ejecutar la función por su nombre original obteniendo los mismos resultados que antes.

```
funcion_necesita_decorador()
Código antes de la funcion_original()
¡Quiero que me decoren!
Código después de la funcion_original()
```

### **Conclusión**

Los decoradores en Python proporcionan una forma limpia y potente de ampliar el comportamiento de las funciones. Al comprender las funciones y cierres de primera clase, podrá comprender cómo trabajan los decoradores bajo el capó.
Ya sea que esté utilizando decoradores basados en funciones o en clases, puede mejorar sus funciones sin alterar su código original, manteniendo su código base limpio y fácil de mantener.

- Los decoradores son poderosos para ampliar la funcionalidad de las funciones.
- Se pueden implementar mediante funciones o clases.
- La sintaxis @decorador es una forma más limpia y legible de aplicar decoradores.
- Ayudan a mantener su código SECO (No se repita) al abstraer la funcionalidad común.
