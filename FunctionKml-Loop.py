def main():
    import arcpy
    import os
    arcpy.env.overwriteOutput = True

    # settings: edit these
    fc_in = r'C:\Users\Admin\Desktop\IDINSIGHTS-SHAPEFILES\All_Segments_Points.shp'
    fld_trail = 'clinic_nam'
    out_folder = r'C:\Users\Admin\Desktop\SettlementPoints'

    # create list of unique trail names
    lst_trails = list(set([r[0] for r in arcpy.da.SearchCursor(fc_in, (fld_trail))]))

    # loop through trails
    for trail_name in lst_trails:
        fld = arcpy.AddFieldDelimiters(fc_in, fld_trail)
        where ="{0} = '{1}'".format(fld, trail_name)
        arcpy.MakeFeatureLayer_management(fc_in,"Settlement_points", where)
        kmz_file = os.path.join(out_folder, "{0}.kmz".format(trail_name))
        arcpy.LayerToKML_conversion("Settlement_Points", kmz_file)

if __name__ == '__main__':
    main()
