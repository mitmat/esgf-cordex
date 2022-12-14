# download from liu.se servers requires wget scripts
# -> create scripts automatically (and run them manually later in bash)

# delete manually the non-cropped files afterwards!!

path_in = "/home/climatedata/eurocordex-temp/"
path_out = "/home/climatedata/eurocordex/"

import os
from glob import glob
import xarray as xr
from datetime import datetime # for info

all_vars = os.listdir(path_in)
all_vars.sort()
# all_vars = all_vars[:3] # for test

for var in all_vars:
  all_files = glob(os.path.join(path_in, var, "*.nc"))
  
  for file_in in all_files:
    file_out = os.path.join(path_out, var, os.path.basename(file_in))
    if(not os.path.exists(file_out)):
      ds = xr.open_dataset(file_in, chunks={'time': 120})
      ds = ds.sel(rlat=slice(-8, -1), rlon=slice(-11, 0))
      ds.to_netcdf(file_out)
      print(datetime.now().isoformat())
      print(file_out)



