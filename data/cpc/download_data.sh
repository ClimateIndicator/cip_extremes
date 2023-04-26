
mkdir raw
pushd raw

wget -r --no-parent -nH --cut-dirs=3 -A '*.nc'  https://downloads.psl.noaa.gov/Datasets/cpc_global_temp/

popd
