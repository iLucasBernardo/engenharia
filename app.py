def calculadora_engenharia():
    print("=== Calculadora de Grandezas Físicas (Leis de Newton) ===")
    while True:
        print("\nEscolha a grandeza que deseja calcular:")
        print("1 - Força (F = m * a)")
        print("2 - Massa (m = F / a)")
        print("3 - Aceleração (a = F / m)")
        print("4 - Sair")
        escolha = input("Digite o número da opção desejada: ")
        if escolha == '1':
            try:
                massa = float(input("Digite a massa (em kg): "))
                aceleracao = float(input("Digite a aceleração (em m/s²): "))
                forca = massa * aceleracao
                print(f"Força resultante: {forca:.2f} N")
            except ValueError:
                print("Entrada inválida. Digite valores numéricos.")

        elif escolha == '2':
            try:
                forca = float(input("Digite a força (em N): "))
                aceleracao = float(input("Digite a aceleração (em m/s²): "))
                if aceleracao == 0:
                    print("A aceleração não pode ser zero.")
                else:
                    massa = forca / aceleracao
                    print(f"Massa: {massa:.2f} kg")
            except ValueError:
                print("Entrada inválida. Digite valores numéricos.")

        elif escolha == '3':
            try:
                forca = float(input("Digite a força (em N): "))
                massa = float(input("Digite a massa (em kg): "))
                if massa == 0:
                    print("A massa não pode ser zero.")
                else:
                    aceleracao = forca / massa
                    print(f"Aceleração: {aceleracao:.2f} m/s²")
            except ValueError:
                print("Entrada inválida. Digite valores numéricos.")

        elif escolha == '4':
            print("Encerrando a calculadora. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Chamada da função
calculadora_engenharia()
