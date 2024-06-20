import arcpy

def ScriptTool(param0, param1):
    # Script execution code goes here
    return

# This is used to execute code if the file was run but not imported
if __name__ == '__main__':

    # Tool parameter accessed with GetParameter or GetParameterAsText
    input_fc = arcpy.GetParameterAsText(0) #servicio
    output = arcpy.GetParameterAsText(1)    #directorio salida
    nameout = arcpy.GetParameterAsText(2)  #nombre 
    
    ScriptTool(input_fc, output, nameout)
    
    # Update derived parameter values using arcpy.SetParameter() or arcpy.SetParameterAsText()



    #-----------------------------------------


out_fc=f"{output/nameout}"


#campos 
pob="población_residente"
ent="residencial"

#mayor valor
max_valor={}

#diccionario para almacenar el objectid del poligono con mayor poblacion 
max_oid={}

# cursor de busqueda para iterar dentro de residencial
with arcpy.da.SearchCursor(input_fc, [ent, "OID@", pob]) as cur:
    for row in cur:
        entidad = row[0]
        oid = row[1]
        poblacion = row[2]
                # Actualizar el diccionario si encontramos una población mayor para la entidad seleccionada
        if entidad not in max_valor or poblacion > max_valor[entidad]:
            max_valor[entidad] = poblacion
            max_oid[entidad] = oid


# Crear una lista de OBJECTID con el poligono seleccionado
oid_select = list(max_oid.values())

# Crear una cláusula SQL para seleccionar los polígonos con los OBJECTID seleccionados
sql_clause = "{} IN ({})".format(arcpy.AddFieldDelimiters(input_fc, "OBJECTID"), ",".join(map(str, oid_select)))


# Usar la cláusula SQL para seleccionar los polígonos y guardarlos en un nuevo feature class
arcpy.management.SelectLayerByAttribute(input_fc, "NEW_SELECTION", sql_clause)
arcpy.management.CopyFeatures(input_fc, out_fc)
