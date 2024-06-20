import arcpy
def ScriptTool(calle_apta_fc, industrial_fc, baldio_fc):
    # Script execution code goes here
    return
# This is used to execute code if the file was run but not imported
if __name__ == '__main__':
    # Tool parameter accessed with GetParameter or GetParameterAsText
    calle_apta_fc = arcpy.GetParameterAsText(0)
    industrial_fc = arcpy.GetParameterAsText(1)
    baldio_fc = arcpy.GetParameterAsText(2)
    
    ScriptTool(calle_apta_fc, industrial_fc, baldio_fc)
    
    # Update derived parameter values using arcpy.SetParameter() or arcpy.SetParameterAsText()
#---------------------------------------------
output_fc = "vias_op"          # polilíneas de salida
# Crear un entorno de trabajo temporal para almacenar resultados intermedios
arcpy.env.workspace = "C:\proyecto\DAG_1s2024_L_TRABAJO_1_PARTE_2_CLM\DAG_1s2024_L_TRABAJO_1_PARTE_2_CLM.gdb\salidas"

# Crear un feature class temporal para almacenar la intersección con "industrial"
intersect_output_industrial = "intersect_output_industrial"
arcpy.analysis.Intersect([calle_apta_fc, industrial_fc], intersect_output_industrial, "ALL", "", "LINE")

# Crear un feature class temporal para almacenar la intersección con "baldio"
intersect_output_baldio = "intersect_output_baldio"
arcpy.analysis.Intersect([calle_apta_fc, baldio_fc], intersect_output_baldio, "ALL", "", "LINE")

# Unir las dos intersecciones temporales en una sola capa temporal
union_output = "union_output"
arcpy.management.Merge([intersect_output_industrial, intersect_output_baldio], union_output)

# Guardar el resultado final en el feature class de salida
arcpy.management.CopyFeatures(union_output, output_fc)

# Limpiar el entorno de trabajo temporal
arcpy.management.Delete(intersect_output_industrial)
arcpy.management.Delete(intersect_output_baldio)
arcpy.management.Delete(union_output)
