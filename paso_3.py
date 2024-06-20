import arcpy

def ScriptTool(param0, param1):
    # Script execution code goes here
    return

# This is used to execute code if the file was run but not imported
if __name__ == '__main__':

    # Tool parameter accessed with GetParameter or GetParameterAsText
    salida_fc = arcpy.GetParameterAsText(0)  # polilíneas de entrada
    cultivo_fc = arcpy.GetParameterAsText(1) #polígonos de entrada
    
    ScriptTool(salida_fc, cultivo_fc)
    
    # Update derived parameter values using arcpy.SetParameter() or arcpy.SetParameterAsText()



#---------------------------------------------------


output_fc = "calle_apta"       #polilíneas de salida

# Crear un entorno de trabajo temporal para almacenar resultados intermedios
arcpy.env.workspace = "C:\proyecto\DAG_1s2024_L_TRABAJO_1_PARTE_2_CLM\DAG_1s2024_L_TRABAJO_1_PARTE_2_CLM.gdb\salidas"

## Crear un feature class temporal para almacenar la intersección
intersect_output = "intersect_output"
arcpy.analysis.Intersect([salida_fc, cultivo_fc], intersect_output, "ALL", "", "LINE")

# Crear un feature class temporal para almacenar el resultado del borrado
erase_output = "erase_output"
arcpy.analysis.Erase(salida_fc, cultivo_fc, erase_output)

# Guardar el resultado final en el feature class de salida
arcpy.management.CopyFeatures(erase_output, output_fc)

# Limpiar el entorno de trabajo temporal
arcpy.management.Delete(intersect_output)
arcpy.management.Delete(erase_output)
