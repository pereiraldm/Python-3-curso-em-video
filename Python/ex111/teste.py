def leia_cpf(msg="CPF: ", show=True):
    """
    -> Validador de CPF
    :param msg: Mensagem que será exibida para o usuário (não é obrigatório! Caso 'msg' não receba
    nenhum valor ele retornará a mensagem "CPF: ".
    :param show: Parâmetro não obrigatório utilizado para mostrar ou não o CPF formatado (caso 'show' não receba
    nenhum valor, ela retornará 'True' e mostrará o CPF formatado).
    :return: retorna o CPF digitado pelo usuário em tipo inteiro.
    """
    from time import sleep
    while True:
        erro = False
        c1 = input(msg).strip().replace('.', '').replace('-', '').replace(',', '')
        print('Verificando...')
        sleep(1)
        if not c1.isnumeric() or len(c1) != 11:
            erro = True
        if erro:
            print(f'CPF inválido!')
        else:
            if show:
                print(f'O CPF \'{c1[:3]}.{c1[3:6]}.{c1[6:9]}-{c1[9:]}\' é válido.')
            else:
                print('CPF válido.')
            return int(c1)
