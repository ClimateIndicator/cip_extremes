
mkdir raw
pushd raw

wget -r --no-parent -nH --cut-dirs=3 -A 'Complete_????_Daily_LatLong1_*.nc'  http://berkeleyearth.lbl.gov/auto/Global/Gridded/

popd
