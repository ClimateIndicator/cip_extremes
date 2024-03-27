from pathlib import Path

import filefinder
import xarray as xr

DATA_ROOT = Path("/net/exo/landclim/data/dataset/ERA5_deterministic/recent/")

SEL_LAT = slice(84, -58)

files_orig = filefinder.FileFinder(
    path_pattern=DATA_ROOT / "0.25deg_lat-lon_{time_res}/original/",
    file_pattern="era5_deterministic_recent.{variable}.025deg.{time_res}.{year}.nc",
)

files_post = ff = filefinder.FileFinder(
    path_pattern="../data/era5/{variable}",
    file_pattern="era5_{variable}_{year}.nc",
)


def load_landmask(remove_antarctica=True):

    path = DATA_ROOT/ "0.25deg_lat-lon_time-invariant/original"
    fN = path / "era5_deterministic_recent.lsm.025deg.time-invariant.nc"

    land_mask = xr.open_dataset(fN).lsm
    land_mask = land_mask.rename(longitude="lon", latitude="lat")
    land_mask = land_mask.squeeze(drop=True)

    if remove_antarctica:
        land_mask = land_mask.sel(lat=SEL_LAT)

    return land_mask


def load_post(variable):

    fc = files_post.find_files(variable=variable)

    out = list()
    for fN, meta in fc:
        ds = xr.open_dataset(fN)

        ds = ds.assign_coords(year=int(meta["year"]))

        out.append(ds)

    ds = xr.concat(out, dim="time")

    return ds
