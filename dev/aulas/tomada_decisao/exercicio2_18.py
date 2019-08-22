data = input('Digite uma data no formatao dd/mm/aaaa: ')

if len(data) == 10:

    if data[2] == '/' and data[5] == '/':

        dia_intervalo = (data[0] + data[1])

        mes_intervalo = (data[3] + data[4])

        ano_intervalo = (data[6] + data[7] + data[8] + data[9])

        if dia_intervalo.isnumeric() == True and mes_intervalo.isnumeric() == True and ano_intervalo.isnumeric() == True:

            numdia = int(dia_intervalo)

            nummes = int(mes_intervalo)

            numano = int(ano_intervalo)

            if numano > 0:

                if nummes > 0 and nummes <= 12:

                    if numdia > 0 and numdia <= 31:

                        print('Data %s validada com sucesso!' % (data))

                    else:

                        print('O valor digitado não é valido para o formato de data.')

                else:

                    print('O valor digitado não é valido para o formato de data.')

            else:

                print('O valor digitado não é valido para o formato de data.')

        else:

            print('O valor digitado não é valido para o formato de data.')

    else:

        print('O valor digitado não é valido para o formato de data.')

else:

    print('O valor digitado não é valido para o formato de data.')