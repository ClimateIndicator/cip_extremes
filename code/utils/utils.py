import pathlib

import numpy as np
import xarray as xr

fig_dir = pathlib.Path("../figures")


def open_mfdataset(fNs_in, combine="by_coords", **kwargs):
    """set defaults for xr.open_mfdataset"""

    defaults = {
        "coords": "minimal",
        "data_vars": "minimal",
        "compat": "override",
        "parallel": False,
        "decode_cf": True,
        "use_cftime": True,
    }

    defaults.update(**kwargs)

    ds = xr.open_mfdataset(fNs_in, combine=combine, **defaults)

    return ds


def lat_weights(ds, y_coord="lat"):
    wgt = np.cos(np.deg2rad(ds[y_coord]))

    return wgt


def global_mean(da):

    wgt = lat_weights(da)

    return da.weighted(wgt).mean(("lat", "lon"))


def land_mean(da, land_mask):

    wgt = lat_weights(da)

    if land_mask is not None:
        wgt = wgt * land_mask

    return da.weighted(wgt).mean(("lat", "lon"))


def calc_anomaly(data, clim_period, dim="year"):

    return data - data.sel({dim: clim_period}).mean(dim)
