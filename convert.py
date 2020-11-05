import xarray as xr

ds = xr.open_dataset("./data/wind_europe_2015_2019.grib", engine="cfgrib")
ds.to_netcdf('./data/wind_europe_2015_2019.nc')