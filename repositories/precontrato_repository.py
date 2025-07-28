from models import Precontrato

def obtener_todos_precontratos():
    resultado = Precontrato.query.all()
    print("PRECONTRATOS:", resultado)
    return resultado

