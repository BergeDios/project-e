def Events():
    """List of events to be generated with mongo"""
    events = [
        {
            'id': 1,
            'nombre':'Evento en Teatro de Verano',
            'descripcion':'Lorem ipsum dolor sit amet, consectetur adipiscing',
            'autor':'Santiago Goyret',
            'fecha':'09/06/2022',
        },
        {
            'id': 2,
            'nombre':'Demo Day en el Celebra',
            'descripcion':'Lorem ipsum dolor sit amet, consectetur adipiscing',
            'autor':'Holberton',
            'fecha':'01/7/2022',
        },
        {
            'id': 3,
            'nombre':'Concierto en La Trastienda',
            'descripcion':'Lorem ipsum dolor sit amet, consectetur adipiscing',
            'autor':'AC DC',
            'fecha':'13/12/2022',
        }
    ]
    return events