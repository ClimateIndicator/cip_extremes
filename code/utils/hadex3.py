# Adapted from https://github.com/IPCC-WG1/Chapter-11/blob/24b9a03857c8/code/hadex3.py

# For reference, here is a copy of their copyright notice:

# Copyright (c) 2021 ETH Zurich, Mathias Hauser.

# This is free software; you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 or
# (at your option) any later version.

# The code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.


import warnings

import filefisher as ff
import xarray as xr

# from utils import plot
# from utils.statistics import theil_ufunc

# we would get 13 warnings when reading HadEX3 data
warnings.filterwarnings("ignore", message="variable '.*' has multiple fill values")

CURRENT_VERSION = "3.0.4"


class HadEx3_cls:
    """docstring for HadEx3_cls."""

    def __init__(self):

        self._files_raw = ff.FileFinder(
            path_pattern="../data/HadEX3/v{version}/raw/",
            file_pattern="HadEX3_{varn}_{year_from}-{year_to}_ADW_{climatology}_1.25x1.875deg.nc",
        )

        self._files_post = ff.FileFinder(
            path_pattern="../data/HadEX3/v{version}/{postprocess}/",
            file_pattern="{postprocess}_HadEX3_{varn}_ADW_{climatology}.{ending}",
        )

        self._filecontainer_all_files_raw = None

        self.map_abbrevs = dict(
            TXx="maximum Tmax",
            TXn="minimum Tmax",
            TNx="maximum Tmin",
            TNn="minimum Tmin",
            TX90p="warm days",
            TX10p="cool days",
            TN90p="warm nights",
            TN10p="cool nights",
            TR="tropical nights",
            SU="summer days",
            FD="frost days",
            ID="ice days",
            CSDI="cool spell duration",
            WSDI="warm spell duration",
            DTR="diurnal temperature range",
            GSL="growing season length",
            CDD="consecutive dry days",
            CWD="consecutive wet days",
            PRCPTOT="total precipitation",
            R10mm="precip in &gt;10mm days",
            R20mm="precip in &gt;20mm days",
            Rx1day="maximum 1 day total",
            Rx5day="maximum 5 day total",
            R95p="amount in very wet days",
            R99p="amount in extremely wet days",
            R95pTOT="fraction in very wet days",
            R99pTOT="fraction in extremely wet days",
            SDII="specific daily intensity",
        )

    @property
    def files_raw(self):
        """FileFinder for raw HadEx3 files"""
        return self._files_raw

    @property
    def files_post(self):
        """FileFinder for postprocessed HadEx3 files"""
        return self._files_post

    @property
    def filecontainer_all_files_raw(self):
        """FileFinder list of all raw files"""
        if self._filecontainer_all_files_raw is None:
            self._filecontainer_all_files_raw = self.files_raw.find_files()

        return self._filecontainer_all_files_raw

    def __repr__(self):
        return "<HadEx3 class>"

    def _read_file(
        self, varn, climatology="61-90", variable="Ann", version=CURRENT_VERSION
    ):
        """read one file and return with metadata

        Parameters
        ----------
        varn : str
            Variable name (e.g. 'TXx')
        climatology : "61-90" | "81-10"
            Climatology of the HadEx files
        variable : str
            Name of the variable to read, e.g. "Ann", "JAN"
        version : str, default: CURRENT_VERSION
            Which version of the HADEX3 data to read.

        Returns
        -------
        da : xr.DataArray
        meta : dict of meta data
        """

        fc = self.filecontainer_all_files_raw
        fc = fc.search_single(varn=varn, climatology=climatology, version=version)
        fN, meta = fc[0]

        ds = xr.open_dataset(fN, decode_cf=False)

        ds = ds.rename(longitude="lon", latitude="lat")

        # get rid of the "days" units, else CDD will have dtype = timedelta
        units = ds[variable].attrs.get("units", None)
        if units in ["seconds", "days"]:
            ds[variable].attrs.pop("units")

        ds = xr.decode_cf(ds, use_cftime=True)

        da = ds[variable]

        return da, meta

    def read_file(
        self, varn, climatology="61-90", variable="Ann", version=CURRENT_VERSION
    ):
        """read one file and return without metadata

        Parameters
        ----------
        varn : str
            Variable name (e.g. 'TXx')
        climatology : "61-90" | "81-10"
            Climatology of the HadEx files
        variable : str
            Name of the variable to read, e.g. "Ann", "JAN"
        version : str, default: CURRENT_VERSION
            Which version of the HADEX3 data to read.

        Returns
        -------
        da : xr.DataArray
        """

        ds, meta = self._read_file(
            varn, climatology=climatology, variable=variable, version=version
        )

        return ds

    def read_files(
        self, varns, climatology="61-90", variable="Ann", version=CURRENT_VERSION
    ):
        """read several files

        Parameters
        ----------
        varns : str
            Variable name (e.g. 'TXx')
        climatology : "61-90" | "81-10"
            Climatology of the HadEx files
        variable : str
            Name of the variable to read, e.g. "Ann", "JAN"
        version : str, default: CURRENT_VERSION
            Which version of the HADEX3 data to read.

        Returns
        -------
        filelist : list with da/ meta data structure
        """
        if isinstance(varns, str):
            varns = [varns]

        out = list()

        for varn in varns:
            ds, meta = self._read_file(
                varn=varn, climatology=climatology, variable=variable, version=version
            )

            out.append([ds, meta])

        return out

    def read_landmask(self, version=CURRENT_VERSION):
        """read the HadEx3 landmask"""

        landmask, meta = self._read_file(
            varn="landmask", climatology=None, variable="landmask", version=version
        )

        return landmask


# ds = ds.rename(longitude="lon", latitude="lat")


HadEx3 = HadEx3_cls()


def _invalidated(valid, condition, what=""):
    """print percentage of invalidated grid cells"""
    n_valid = valid.sum().values

    invalidated = valid & (~condition)

    invalidated = invalidated.values.sum() / n_valid * 100

    print(f"{what} removed {invalidated:0.2f} % valid gridpoints")


def find_valid_gridpoints_dunn(
    da, time=slice(1950, 2018), last_timestep=2009, minimum_valid=0.66
):
    """find valid grid points after Dunn et al., Figure 2a

    1.) time 1950...2018
    2.) last valid data must at least be in 2009
    3.) 66% of valid gridpoints
    """

    # select timeframe
    da = da.sel(time=time)

    # find valid data
    isnull = da.isnull()
    notnull = ~isnull

    # grid cells with at least one datapoint
    atleast_one = notnull.any("time")

    # last valid data must be after 2009
    if last_timestep is not None:
        # find the last timestep that is non-nan
        idx = isnull.sortby("time", ascending=False).argmin("time")
        last_timestep_in_series = da.time.max() - idx

        condition = last_timestep_in_series >= last_timestep

        da = da.where(condition)

        _invalidated(atleast_one, condition, what="end date")

    # require more than minimum_valid timesteps
    valid_fraction = notnull.sum("time") / len(da.time)
    condition = valid_fraction >= minimum_valid

    da = da.where(condition)

    _invalidated(atleast_one, condition, what="minimum_valid")

    return da


def valid_for_globmean(da, time=slice(1950, 2018), minimum_valid=0.9):
    # for the global mean Dunn et al. require at least 90% valid years (see Figure 2.)

    # select timeframe
    da = da.sel(time=time)

    # find valid data
    isnull = da.isnull()
    notnull = ~isnull

    # grid cells with at least one datapoint
    atleast_one = notnull.any("time")

    # require more than minimum_valid timesteps
    valid_fraction = notnull.sum("time") / len(da.time)
    condition = valid_fraction >= minimum_valid

    da = da.where(condition)

    _invalidated(atleast_one, condition, what="minimum_valid")

    return da
