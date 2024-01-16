# Importaciones
from webexteamssdk import WebexTeamsAPI, ApiError
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.models.cards.card import AdaptiveCard
from webexteamssdk.models.cards.inputs import Text, Number
from webexteamssdk.models.cards.components import TextBlock
from webexteamssdk.models.cards.actions import Submit

# instancia de webex
api_token="NmUyZTdlYjQtN2U2NC00MGFkLTk0OWItMGJiNTUyYTM2MzdmZDY5NDBlMzQtODk5_PE93_27f882c3-50be-433d-96e5-4dceb2514eab"
api = WebexTeamsAPI(access_token=api_token)

# Obtener las salas creados
all_rooms = api.rooms.list()


    
try:
    # Creando una sala
    sala_examen = api.rooms.create('Sala de Examen')
    # instancia de api de mensajes
    api.messages.create(sala_examen.id, text="Esta es una sala de examen",)
    
    # campos de la api
    saludo = TextBlock("Hey hello there! I am a adaptive card")
    nombre = Text('first_name', placeholder="First Name")
    edad = Number('age', placeholder="Age")
    # boton
    enviar = Submit(title="Send me!")
    # creacion de la tarjeta
    card = AdaptiveCard(body=[saludo, nombre, edad], actions=[enviar])


    api.messages.create(text="fallback", roomId=sala_examen.id, attachments=[card])
    
    for c_room in all_rooms:
        print('Salas creadas: ',c_room.title)
        
except ApiError as e:
    print(e)

