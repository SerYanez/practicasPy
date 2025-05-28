# 9- Crear un diccionario catalogo con claves: nombre de película y valores como
# otro diccionario con claves internas: director, año, género. Acceder al género
# de una película específica.

peliculas = {}
peliculas["El Señor de los Anillos: la Comunidad del Anillo"] = {"Director" : "Peter Jackson",
                                                                 "Año" : 2001,
                                                                 "Género" : "Fantasía"}
peliculas["El señor de los anillos: las dos torres"] = {"Director" : "Peter Jackson",
                                                        "Año" : 2002,
                                                        "Género" : "Fantasía"}
peliculas["Star Wars: episodio IV - una nueva esperanza"] = {"Director" : "George Lucas",
                                                             "Año" : 1977,
                                                             "Género" : "Ciencia Ficción"}
peliculas["Tiempos violentos"] = {"Director" : "Quentin Tarantino",
                                  "Año" : 1994,
                                  "Género" : "Acción"}
peliculas["Hombres de negro"] = {"Director" : "Barry Sonnenfeld",
                                 "Año" : 1997,
                                 "Género" : "Acción/Comedia"}

print("El género de 'Hombres de negro' es:", peliculas["Hombres de negro"]["Género"])
