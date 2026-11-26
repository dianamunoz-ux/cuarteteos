
def infijo_a_postfijo(expresion):
    token = namedtuple("token", "tipo lexema linea")
    cuarteto = namedtupla("cuarteto", "operador operando1 operando2 resultado") 

    class errorComp (exception):
        def init(self, mens, linea, clase="sintactico")
            super().int(mens)
            self.mens= mens
            self.linea =linea
            self.clase = clase
        def str(self):
            return f"Error {self.clase} (linea{self.clase}): {self.mensaje}"
    PATRONES=[
        ("NUM", r"\+(?:\.\d+)?"),("ID", r"\+[^\W\d]\w*"), ("OP", r":=|<=|>=|<>|==|[-+*^<>=]"),
        (parizq, r"\("), (parder, r"\)"), (coma, r","), (puntocoma, r";"), (salto, r"\n"), (espacio, r"[\t\r\f\v]+"), (error, r".")
    ]
    expresionlexica= re.compile("|".join(f"?\P<[nombre]>{patron}" for nombre, patron in PATRONES))
    palabrasreservadas ={"read": "READ", "write": "WRITE"}
    operadorespalabra= {"not", "and", "or"}

    def analizadorLexico(texto)
        for guin in "---" :
            texto =texto.replace

def infijo_a_postfijo(expresion):
    # Definición de precedencias (a mayor valor, mayor prioridad)
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    asociatividad_derecha = {'^'}
    pila = [] # Almacena operadores y paréntesis
    salida = [] # Resultado en notación postfijo
    # Remover espacios en blanco para procesar caracteres limpios
    tokens = expresion.replace(" ", "")
    for token in tokens:
    # Caso 1: El token es un operando (Letra o Número)
        if token.isalnum():
            salida.append(token)
        # Caso 2: Paréntesis de apertura
        elif token == '(':
            pila.append(token)
        # Caso 3: Paréntesis de cierre
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if pila and pila[-1] == '(':
                pila.pop() # Eliminar el '(' residual
        # Caso 4: El token es un operador
        elif token in precedencia:
            while (pila and pila[-1] != '(' and precedencia[pila[-1]] > precedencia[token] or precedencia[pila[-1]] == precedencia[token] and token not in asociativid salida.append(pila.pop())
            pila.append(token)
    # Vaciar los elementos restantes de la pila
    while pila:
        salida.append(pila.pop())
    return "".join(salida)
# Pruebas de ejecución
if name == " main ": ejemplo
    = "A + B * C ^ D - E"
    resultado = infijo_a_postfijo(ejemplo)
    print(f"Infijo: {ejemplo} -> Postfijo: {resultado}")