# Download Data Gelombang
from ecmwfapi import ECMWFDataServer

''' NOTES:
    Hs - stream:wave, param:229.140, class:ei, levtype:sfc
    u10 & v10 - stream:oper, param:165.128/166.128, class:ei, levtype:sfc
'''

server = ECMWFDataServer()

# untuk kode 'stream','param','type' bisa di cek di web ecmwf ketika ingin mendownload datanya
server.retrieve({
    'stream'    : "wave",                     # kode untuk akses data swh
    'levtype'   : "sfc",
    'param'     : "229.140",                  # kode parameter untuk Hs
    'dataset'   : "interim",                  # jenis dataset yg di download
    'step'      : "0",                        # dimulai dari step 0
    'grid'      : "0.125/0.125",              # resolusi grid
    'time'      : "0000/0600/1200/1800",      # resolusi waktu, kalau per 6 jam: (0000/0600/1200/1800)
    'date'      : "1980-08-01/to/2019-08-31", # Periode download
    'type'      : "an",                       # kode untuk akses data swh
    'class'     : "ei",
    'area'      : "5/90/-11/140",            # Domain kajian
    #'area'      : "0/104/-10/114",            # Domain kajian
    'format'    : "netcdf",                   # format file
    'target'    : "swh_indo_6jam_0880_0819.nc"     # Nama file yg akan disimpan
 })
