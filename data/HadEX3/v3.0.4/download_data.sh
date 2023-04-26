#!/bin/bash

mkdir raw
pushd raw

base_url=https://www.metoffice.gov.uk/hadobs/hadex3/data/

# list of data with 1961-1990 climatology

hadex_data=(
    "HadEX3_TXx_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    "HadEX3_TXn_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    "HadEX3_TNx_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    "HadEX3_TNn_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_TX90p_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_TX10p_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_TN90p_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_TN10p_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_TR_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_SU_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_FD_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_ID_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_CSDI_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_WSDI_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_DTR_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_GSL_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_CDD_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_CWD_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_PRCPTOT_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_R10mm_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_R20mm_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_Rx1day_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_Rx5day_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_R95p_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_R99p_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_R95pTOT_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_R99pTOT_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
    # "HadEX3_SDII_1901-2018_ADW_61-90_1.25x1.875deg.nc.gz"
)

# download using wget
parallel -j 4 wget ${base_url}{} ::: "${hadex_data[@]}"

parallel -j 10 gunzip {} ::: "${hadex_data[@]}"


# list of data with 1981-2010 climatology

# hadex_data_81_10=(
#     "HadEX3_TX90p_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_TX10p_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_TN90p_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_TN10p_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_CSDI_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_WSDI_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_R95p_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_R99p_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_R95pTOT_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
#     "HadEX3_R99pTOT_1901-2018_ADW_81-10_1.25x1.875deg.nc.gz"
# )

# download using wget
# parallel -j 4 wget ${base_url}{} ::: "${hadex_data_81_10[@]}"

# parallel -j 10 gunzip {} ::: "${hadex_data_81_10[@]}"

popd
