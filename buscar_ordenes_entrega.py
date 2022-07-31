import xmlrpc.client

db = 'test'
username = 'demo'
password = 'ingresar-api-key'
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model = 'stock.picking'
method = 'search_read'

# id del modelo res.partner
id_solicitante = 9
dominio = [
    [
        [
            'x_solicitante', '=', id_solicitante
        ]
        , [
            'state', '=', 'assigned'
        ]
    ]
]

campos = {
    'fields': [
        'id'
        , 'name' # numero de pedido
        , 'state'
        , 'scheduled_date'
        , 'move_line_ids'
        , 'x_solicitante'
        , 'partner_id' # paciente
        , 'x_cama'
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
