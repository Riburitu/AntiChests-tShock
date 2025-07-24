
# AntiChests tShock

### SPANISH

 Esté código Python limpia los cofres duplicados desde la base de datos InfChests3.sqlite el cual se provoca por un bug al crear las IDs de los cofres.
 El cual los reposiciona en una misma posición y esto se duplica así exponencialmente. Asimismo, se reasigna la secuencia de IDs para que no se repitan al final.
 Si estas utilizando esté script, asegúrate de crear una copia de seguridad de tu base de datos antes de ejecutarlo, ya que podrías remplazar y perder datos permanentemente.

### ENGLISH

 This code Python cleans the duplicated chests in the InfChests3.sqlite database, which is caused by a bug when creating the chest IDs.
 It repositions them in the same position, and this duplicates exponentially. Additionally, it reassigns the ID sequence to prevent future duplicates.
 If you are using this script, make sure to create a backup of your database before running it, as you may overwrite and lose data permanently.

### Use
 Execute the file kill_dup.bat / Ejecutar el archivo kill_dup.bat