def main():

    pregunta = input("Introduce una lista de países [separados por comas ',']: ")
    
    lista = set(pregunta.split(','))
    lista_paises = list(lista)
    lista_paises.sort()

    print("\nLos países que haz visitado son:\n")
    for p in lista_paises:
        print(p, end=', ')



if __name__ == "__main__":
    main()
