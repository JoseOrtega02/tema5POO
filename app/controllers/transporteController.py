from ..models.transporte import Transporte
from ..views.transporteView import transporteView
def transporteController():
    list= Transporte.query.all()
    return transporteView(list)