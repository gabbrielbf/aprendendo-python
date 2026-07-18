from classes import Casa, Lampada, ArCondicionado, CameraSeguranca

def main():
    lampada = Lampada()
    ar_condiciondo = ArCondicionado()
    camera_seguranca = CameraSeguranca()
    casa = Casa()

    casa.dispositivo = lampada
    casa.dispositivo = ar_condiciondo
    casa.dispositivo = camera_seguranca

    casa.dispositivo

if __name__ == '__main__':
    main()