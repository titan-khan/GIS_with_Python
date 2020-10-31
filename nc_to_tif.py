import numpy as np
import gdal, osr
from netCDF4 import Dataset
from gridfill import fill

nc = Dataset(r'swh_indo_819.nc','r')
lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
swh = nc.variables['swh'][0,:,:]

#--- gridfill u/ mengisi data kosong (pulau)
kw = dict(eps=1e-4, relax=0.6, itermax=1e4, initzonal=False,
          cyclic=False, verbose=True)
filled_swh, converged = fill(swh, 1, 0, **kw)
swh_scaled = np.interp(filled_swh, (swh.min(), swh.max()), (0, 255))

# reverse array so the tif looks like the array
#et_T = et[::-1]
cols = swh_scaled.shape[1]
rows = swh_scaled.shape[0]
RES = 0.125

# Origin should be in Longitude-Latitude form
originX = min(lon)
originY = max(lat)

driver = gdal.GetDriverByName('GTiff')
outRaster = driver.Create(r'swh_indo_time00_2.tif', cols, rows, 1, gdal.GDT_Float64)
outRaster.SetGeoTransform((originX, 0.125, 0, originY, 0, -0.125))
outband = outRaster.GetRasterBand(1)
outband.WriteArray(swh_scaled)
outRasterSRS = osr.SpatialReference()
outRasterSRS.ImportFromEPSG(4326) #before 4326
outRaster.SetProjection(outRasterSRS.ExportToWkt())
outband.FlushCache()
outRaster = None
