import xmlrpc.client

db = 'test'
username = 'demo'
password = 'ingresar-api-key'
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model = 'stock.picking'
method = 'message_post'

id_orden_de_entrega = 40
nota = {
    'body': 'este es un mensaje de prueba'
    , 'message_type': 'comment'
}

info = models.execute_kw(
    db
    , uid
    , password
    , model
    , method
    , [id_orden_de_entrega]
    , nota
)

print(str(info))
