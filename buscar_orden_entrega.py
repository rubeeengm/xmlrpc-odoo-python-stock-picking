import xmlrpc.client

db = 'test'
username = 'demo'
password = 'ingresar-api-key'
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# 1. buscar orden de entrega
model = 'stock.picking'
method = 'search_read'

id_orden_entrega = 5
id_usuario_solicitante = None

dominio = [
    [
        [
            'id', '=', id_orden_entrega
        ]
        # , [
        #     'x_solicitante', '=', id_usuario_solicitante
        # ]
    ]
]

campos = {
    'fields': [
        'id'
        , 'name' # numero de pedido
        , 'state'
        , 'scheduled_date'
        , 'move_line_ids_without_package' # indice numero 4
        , 'x_solicitante'
        , 'partner_id' # paciente}
        , 'x_cama'
    ]
}

orden_entrega = models.execute_kw(
    db
    , uid
    , password
    , model
    , method
    , dominio
    , campos
)

print('cabecera')
print(orden_entrega)

# 2. buscar lineas de la orden de entrega
model = 'stock.move.line'
method = 'search_read'

dominio = [
    [
        [
            'id', 'in', orden_entrega[0]['move_line_ids_without_package']
        ]
        , [
            'picking_id', '=', id_orden_entrega
        ]
    ]
]

campos = {
    'fields': [
        'id'
        , 'product_id'
        , 'product_uom_id'
        , 'qty_done'
        , 'lot_id'
        , 'x_caducidad_lote'
    ]
}

lineas_orden_entrega = models.execute_kw(
    db
    , uid
    , password
    , model
    , method
    , dominio
    , campos
)
