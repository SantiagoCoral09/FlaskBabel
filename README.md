<!-- Crear el archivo con los textos a traducir teniendo en cuenta los idiomas establecidos -->
pybabel extract -F babel.cfg -o messages.pot .

<!-- Iniciar los textos que van a ser traducidos -->
pybabel init -i messages.pot -d translations -l es

<!-- Actualizar archivos de traducción existentes (messages.po):
Luego, ejecuta el siguiente comando para actualizar los archivos de traducción existentes con las nuevas cadenas extraídas: -->
pybabel update -i messages.pot -d translations


<!-- Luego de modificar las traducciones se deben compilar -->
pybabel compile -d translations
