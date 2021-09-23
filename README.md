# Record arcgis_script
How the 3D  building files (kmz) convert to 2D building data (shp)

## Step1
Use Google Earth Pro to compress KMZ to KML

## Step2
Use ArcGis KMLToLayer
*the function let KML to layer (解決一些奇怪的邊線問題)*
```python
arcpy.conversion.KMLToLayer()
```

## Step3
Use ArcGis FeatureClassToShapefile
*the function let layer to Shapefile*
```python
arcpy.conversion.FeatureClassToShapefile()
```

## Step4
Use ArcGis MultiPatchFootprint
*the function let MultiPatch to Polygon and export as a shapefile*

```python
arcpy.ddd.MultiPatchFootprint()
```

All arcpy code
``` python
import os
def input_filename():
    filename=input('input filename:')
    path="C:/D/Study/大四上/實習/圖資/建物/"
    fileDir=path+filename+"/kmz/kml"
    fileExt = r".kml"
    
    # get filename in kml file
    filename=[_[0:-4] for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    for i in filename:
        path='C:/D/Study/大四上/實習/圖資/建物/'+i
        os.mkdir(path)
        arcpy.conversion.KMLToLayer(i, 'C:/D/Study/大四上/實習/圖資/建物/'+i,i, "NO_GROUNDOVERLAY")
        arcpy.conversion.FeatureClassToShapefile("C:/D/Study/大四上/實習/圖資/建物/"+i+"/"+i+".gdb/Placemarks/Multipatches", path)
        arcpy.ddd.MultiPatchFootprint(path+"/Multipatches.shp", "C:/D/Study/大四上/實習/圖資/建物/"+i+'/'+i+'_m', "Name")
    return 'Success',filename
input_filename()
```
Only need to type File Name
#### But it doesn't has data like building heights. 
