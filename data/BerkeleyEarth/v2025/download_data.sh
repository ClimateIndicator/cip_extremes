
mkdir -p raw
pushd raw

url=https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Gridded/

# wget -r --no-parent -nH --cut-dirs=2 -A 'Complete_????_Daily_LatLong1_*.nc' $url

for VARIABLE in TMAX TMIN TAVG
do

    mkdir $VARIABLE

    pushd $VARIABLE

    for YEAR in {1880..2020..10}
    do
        file=Complete_${VARIABLE}_Daily_LatLong1_${YEAR}.nc

        echo Downloading: $VARIABLE $YEAR
        wget ${url}${file}

    done

    popd

done


popd
