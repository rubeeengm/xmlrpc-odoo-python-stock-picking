import xmlrpc.client

db = 'test'
username = 'demo'
password = 'ingresar-api-key'
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model = 'res.users'
method = 'search_read'

id_usuario = 6
dominio = [
    [
        [
            'id', '=', id_usuario
        ]
    ]
]

campos = {
    'fields': [
        'id', 'login', 'partner_id'
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
