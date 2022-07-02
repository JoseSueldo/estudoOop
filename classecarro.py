from time import sleep

class Carro:
        #Atributos
        def __init__(self, marca, portas, cor, combustivel, placa, velocidade, velocidadetotal, marcha, marchatotal):

                self.marca = marca

                self.portas = portas

                self.cor = cor

                self.combustivel = combustivel

                self.placa = placa

                self.velocidade = velocidade

                self.velocidadetotal= velocidadetotal

                self.marcha = marcha

                self.marchatotal = marchatotal

        #Metodos
        def myfunc(self):
            print(f'''

            1° Carro:

            Marca: {self.marca}

            portas: {self.portas}

            Cor: {self.cor} -

            Combustivél: {self.combustivel} -

            Placa: {self.placa} -

            Velocidade Atual: {self.velocidade}KM/H -

            Velocidade Total do Veiculo: {self.velocidadetotal}

            Marcha: {self.marcha}

            Quantidade de marchas: {self.marchatotal}

            ''')

            # Aqui tem a aceleração, passagem de marcha e redução.

        def acelerar(self):
            self.velocidade = self.velocidade + 2

            self.marcha += 1

            print(f'{self.velocidade:.1f} km/h')

            print(f'Marcha  {self.marcha}°')

            while self.velocidade < self.velocidadetotal:
                self.velocidade = self.velocidade + 2

                print(f'{self.velocidade}km/h')

                sleep(0.1)

                if self.velocidade == 20:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':
                        print(f'{self.velocidade:.1f} km/h')
                        break
                    elif m == 's':
                        a = self.marcha + 1

                        print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')
                    # Aqui pergunta a o usuario se deseja reduzir a marcha

                    dm = str(input('Deseja reduzir a marcha ? '))

                    if dm == 'n':

                        print('Velocidade estabelecida')

                    elif dm == 's':

                        self.velocidade -= 8

                        while self.velocidade > 20:
                            self.velocidade -= 8

                            print(f'{self.marcha}')

                            print(f'{self.velocidade}')

                            self.velocidade == 0
                elif self.velocidade == 50:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':

                        print(f'{self.velocidade:.1f} km/h')

                        break

                    elif m == 's':

                        a = self.marcha + 2

                        # print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')

                        # Aqui pergunta a o usuario se deseja reduzir a marcha

                        dm = str(input('Deseja reduzir a marcha ? '))

                        if dm == 'n':

                            print('Velocidade estabelecida')

                        elif dm == 's':

                            self.velocidade -= 8

                            while self.velocidade > 50:
                                self.velocidade -= 8

                                print(f'{self.velocidade}')

                                self.velocidade == 20
                elif self.velocidade == 80:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':

                        print(f'{self.velocidade:.1f} km/h')

                        break

                    elif m == 's':

                        a = self.marcha + 3

                        # print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')

                        # Aqui pergunta a o usuario se deseja reduzir a marcha

                        dm = str(input('Deseja reduzir a marcha ? '))

                        if dm == 'n':

                            print('Velocidade estabelecida')

                        elif dm == 's':

                            self.velocidade -= 8

                            while self.velocidade > 80:
                                self.velocidade -= 8

                                print(f'{self.velocidade}')

                                self.velocidade == 50

                elif self.velocidade == 110:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':

                        print(f'{self.velocidade:.1f} km/h')

                        break

                    elif m == 's':

                        a = self.marcha + 4

                        # print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')
                        # Aqui pergunta a o usuario se deseja reduzir a marcha

                        dm = str(input('Deseja reduzir a marcha ? '))

                        if dm == 'n':

                            print('Velocidade estabelecida')

                        elif dm == 's':

                            self.velocidade -= 8

                            while self.velocidade > 110:
                                self.velocidade -= 8

                                print(f'{self.velocidade}')

                                self.velocidade == 80
                elif self.velocidade == 150:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':

                        print(f'{self.velocidade:.1f} km/h')

                        break

                    elif m == 's':

                        a = self.marcha + 5

                        # print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')

                        # Aqui pergunta a o usuario se deseja reduzir a marcha

                        dm = str(input('Deseja reduzir a marcha ? '))

                        if dm == 'n':

                            print('Velocidade estabelecida')

                        elif dm == 's':

                            self.velocidade -= 8

                            while self.velocidade > 20:
                                self.velocidade -= 8

                                print(f'{self.marcha}')

                                print(f'{self.velocidade}')

                                self.velocidade == 0

                elif self.velocidade == 180:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':

                        print(f'{self.velocidade:.1f} km/h')

                        break

                    elif m == 's':

                        a = self.marcha + 6

                        # print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')

                        # Aqui pergunta a o usuario se deseja reduzir a marcha

                        dm = str(input('Deseja reduzir a marcha ? '))

                        if dm == 'n':

                            print('Velocidade estabelecida')

                        elif dm == 's':

                            self.velocidade -= 8

                            while self.velocidade > 20:
                                self.velocidade -= 8

                                print(f'{self.marcha}')

                            print(f'{self.velocidade}')

                            self.velocidade == 0
                elif self.velocidade == 200:

                    m = str(input('Deseja mudar a macha ? '))

                    if m == 'n':

                        print(f'{self.velocidade:.1f} km/h')

                        break

                    elif m == 's':

                        a = self.marcha + 7

                        # print(f'{self.velocidade:.1f} km/h')

                        print("")

                        print(f'Marcha {a}°')

                        print('')

                        # Aqui pergunta a o usuario se deseja reduzir a marcha

                        dm = str(input('Deseja reduzir a marcha ? '))

                        if dm == 'n':

                            print('Velocidade estabelecida')

                        elif dm == 's':

                            self.velocidade -= 8

                            while self.velocidade > 180:
                                self.velocidade -= 8

                                print(f'{self.velocidade}')
            if self.velocidade == self.velocidadetotal:

                print('Velocidade maxima atingida')



            elif self.velocidade < self.velocidadetotal:

                print(f'Velocidade estabelecida {self.velocidade} km/h')

        '''def mostrarvel(self):
          print(f'{self.velocidade}')

        def passarmarcha(self):
            self.marcha = self.marcha + 1
            print(f'{self.marcha}')

        def reduzirmarcha(self):

            self.marcha = self.marcha - 1

            print(f'{self.marcha}')
'''
        def freiar(self):

            self.freiar = self.velocidade - 8

            print(f'{self.marcha}')

bmw = Carro('BMW', 4, 'Verde Marinho', 'Disel','X-X-X-X', 0, 230, 0, 8)

bmw.myfunc()
bmw.acelerar()
bmw.freiar()
