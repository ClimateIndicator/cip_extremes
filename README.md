# Climate Indicator Project - Extremes

Authors: Mathias Hauser<sup>1</sup>, Dominik Schumacher<sup>1</sup>, Sonia I. Seneviratne<sup>1</sup>

<sup>1</sup>Institute for Atmospheric and Climate Science, Department of Environmental Systems Science, ETH Zurich, Zurich, Switzerland

Analysis of land mean extreme indicators - currently annual maximum temperatures (TXx).


## Data

### ERA5

- Variable: hourly temperature
- Coverage:
  - Spatial: Global, 0.25°
  - Temporal: 1950-today
- Reference: Hersbach et al. (2020)
- Data source: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels
- License: [Copernicus license](http://apps.ecmwf.int/datasets/licences/copernicus/)
- Comments:
  - Annual maximum derived from hourly temperature data


### Berkely Earth

- Variable: daily maximum (and minimum)
- Coverage:
  - Spatial: land-only, 1°; with gaps
  - Spatial: 1750-today
- Reference: Rhode et al., 2013
- Data source: https://berkeleyearth.org/data/
- License: [Creative Commons BY-NC 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)
- Comments:
  - usable from about 1955
  - data for 2022 not complete as of April 2023


### HadEX3

- Variable: annual maximum (and minimum)
- Coverage:
  - Spatial: land-only, 1.25°; with gaps
  - Spatial: 1901-2018
- Reference: Dunn et al., (2020)
- Data source: https://www.metoffice.gov.uk/hadobs/hadex3/download.html
- License: [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/)
- Comments:
  - Used for [IPCC AR6 WGI Chapter 11, Figure 11.2](https://www.ipcc.ch/report/ar6/wg1/figures/chapter-11/figure-11-2/)
  - usable from about 1961
  - lower data availability (~70%) than ERA5 and Berkeley Earth


## Further Datasets

This section lists datasets that were not considered in this analyis round.

- GHCNDEX (https://www.climdex.org/access/)
  - Low data availability, would require uncertainty analysis and/ or infilling.
- CPC (https://psl.noaa.gov/data/gridded/data.cpc.globaltemp.html)
  - Has outliers in the data
  - Would need a different reference period (starts in 1979)
- CRU-TS (https://crudata.uea.ac.uk/cru/data/hrg/)
- 20-century analysis
  - Only up to 2010 and not updated
  - Need to check if appropriate variables are available



## License

Copyright (c) 2023 ETH Zurich.

This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 or (at your option) any later version.

The code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. If not, see https://www.gnu.org/licenses/.

Note that this license only applies to the code and not the figures and underlying data.

## Acknowledgment

HadEX3 [3.0.4] data were obtained from https://www.metoffice.gov.uk/hadobs/hadex3/ on 05.04.2023 and are © British Crown Copyright, Met Office, 2022, provided under a Open Government Licence http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/

## References

* Dunn, R. J. H., Alexander, L. V., Donat, M. G., Zhang, X., Bador, M., Herold, N., et al. (2020). "Development of an Updated Global Land In Situ-Based Data Set of Temperature and Precipitation Extremes: HadEX3." J. Geophys. Res. Atmos. 125. doi:10.1029/2019JD032263.
* Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz‐Sabater, J., et al. (2020). "The ERA5 global reanalysis." Q. J. R. Meteorol. Soc. 146, 1999–2049. doi:10.1002/qj.3803.
* Rohde, R., R. Muller, R. Jacobsen, S. Perlmutter, A. Rosenfeld, J. Wurtele, J. Curry, C. Wickham, and S. Mosher. "Berkeley earth temperature averaging process, geoinfor. geostat.-an overview, 1, 2." Geoinformatics Geostatistics An Overview 1, no. 2 (2013): 20-100.

