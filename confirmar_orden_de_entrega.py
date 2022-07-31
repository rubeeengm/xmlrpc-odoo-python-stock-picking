import xmlrpc.client
from xmlrpc.client import Fault

db = 'test'
username = 'demo'
password = 'ingresar-api-key'
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model = 'stock.picking'
method = 'button_validate'

id_orden_entrega = 28

info = models.execute_kw(
    db
    , uid
    , password
    , model
    , method
    , [id_orden_entrega]
    , {}
)

print(str(info))
