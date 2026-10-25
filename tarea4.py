class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return self.titulo + ", de " + self.autor + " (" + estado + ")"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado.")
        else:
            print("El libro no está disponible.")

    def devolver(self):
        self.disponible = True
        print("Libro devuelto.")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def listar(self):
        for libro in self.libros:
            print(libro)

    def buscar(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None


# Reto opcional
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    def prestar(self):
        print("El libro digital siempre está disponible.")

    def devolver(self):
        print("El libro digital no necesita devolución.")

#libros

libro1 = Libro("Meditaciones", "Marco Aurelio")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro3 = LibroDigital("Python Básico", "Steve García", "PDF")

biblioteca = Biblioteca()

biblioteca.agregar(libro1)
biblioteca.agregar(libro2)
biblioteca.agregar(libro3)

libro1.prestar()

print("\nLista de libros:")
biblioteca.listar()


    