#!/bin/bash
#
# usage: $ bash get_database.bash sample
SELECTED_DB=$1

# Important: Replace 'open' by 'uc' in gdrive links.
# x https://drive.google.com/open?id=1sDZBQEjtKI_QU9SAAL6W9paQBkokDN27
# o https://drive.google.com/uc?id=1sDZBQEjtKI_QU9SAAL6W9paQBkokDN27
function get_database()
{
    local DB_DIR
    local DB_NAME
    local DB_PARENT_DIR
    local DB_TAR
    local DB_URL
    DB_NAME="$1"
    DB_URL="$2"

    DB_PARENT_DIR="/opt/mpavezb/data"
    DB_PARENT_DIR="/home/mpavezb/data"

    # Sample DB
    DB_TAR="${DB_PARENT_DIR}/${DB_NAME}.tar.xz"
    DB_DIR="${DB_PARENT_DIR}/${DB_NAME}"

    # create parent folder
    mkdir -p ${DB_PARENT_DIR}

    # download
    if [ -f ${DB_TAR} ]; then
	echo " - Tar file ${DB_TAR} found. Will not download."
    else
	if [ -d ${DB_DIR} ]; then
	    echo " - Tar file ${DB_TAR} not found, but ${DB_DIR} exists. Will not download."
	else
	    echo " - Tar file ${DB_TAR} not found. Downloading ..."
	    wget -O ${DB_TAR} ${DB_URL}
	fi
    fi

    # uncompress
    if [ -f ${DB_TAR} ]; then
	if [ -d ${DB_DIR} ]; then
	    echo " - DB directory already exists: ${DB_DIR}. Will not uncompress."
	else
	    echo " - Uncompressing ${DB_TAR} ..."
	    tar xf ${DB_TAR} -C ${DB_PARENT_DIR}
	fi
    else
	echo " - Ups... database tar not found: ${DB_TAR}."
    fi
    echo "Bye!."
}

case "$SELECTED_DB" in
    sample)
	get_database ${SELECTED_DB} "https://drive.google.com/uc?id=1sDZBQEjtKI_QU9SAAL6W9paQBkokDN27"
	;;
    data)
	get_database ${SELECTED_DB} "https://drive.google.com/uc?id=1AQ2_zFyioXwFA1SFcVDQUweYcRidXyiV"
	;;
    track1_curves)
	get_database ${SELECTED_DB} "https://drive.google.com/uc?id=1sc1Ittfb7P1w3AOVrcEboId04eJHIRGu"
	;;
    track1_forward)
	get_database ${SELECTED_DB} "https://drive.google.com/uc?id=1QsAXjnPpG5RUo5JG9aCRQ6TMOjB1VX1h"
	;;
    track1_reverse)
	get_database ${SELECTED_DB} "https://drive.google.com/uc?id=17BG3A1_WWTfBo09Lj3IYZPncXFPHoObM"
	;;
    track1_recovery)
	get_database ${SELECTED_DB} "https://drive.google.com/uc?id=1CjL90vMx5YGOrjjbTGmk5sf-I6wabuIf"
	;;
    *)
	echo "unknown database name: ${SELECTED_DB}"
	exit 1
esac
