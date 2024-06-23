from ..models.repartidor import Repartidor
from ..views.homeView import home
def homeController():
    list = Repartidor.query.all()
    return home(list)
