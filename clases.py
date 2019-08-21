class Cacao():
    tamaño = ""
    color = ""
    forma = ""
    peso = []


class AccTijera():
    presion = Pinza()
    apertura = []  # centimetros


class Camara():
    sense_color = []
    resolucion = []  # megapixeles


class SensorProx():
    dist_minima = []
    dist_max = []


class Pinza():
    presion_max = []
    presion_min = []


class CortaMoni():
    cortar = AccTijera()
    cam = Camara()
    proxm = SensorProx()