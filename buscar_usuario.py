import xmlrpc.client

db = 'test'
username = 'demo'
password = 'ingresar-api-key'
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model = 'res.partner'
method = 'search_read'

id_tarjeta = '123123'
dominio = [
    [
        [
            'x_id_tarjeta', '=', id_tarjeta
        ]
    ]
]

campos = {
    'fields': [
        'id', 'name', 'x_id_tarjeta'
    ]
}

info = models.execute_kw(
    db
    , uid
    , password
    , model
    , method
    , dominio
    , campos
)

print(info)
