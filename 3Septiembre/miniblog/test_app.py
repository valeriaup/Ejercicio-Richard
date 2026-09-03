from app import app

def test_hola():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert b"Hola desde mi contenedor" in respuesta.data