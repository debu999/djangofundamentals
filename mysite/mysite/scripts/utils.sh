#!/usr/bin/env bash
set -e


function getparentnlevelup()
{
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]
    then
        echo "Usage: getparentnlevelup -h|--help"
        echo "Usage: getparentnlevelup dirorfilename [no. of levels] [resultvariable]"
        echo "if no 2nd variable, it defaults to 1 level up"
        echo "if 2nd variable is not number, output is set in 2nd variable"
        echo "if 2nd variable is number and no 3rd variable output is printed to stdout"
        echo "if 2nd variable is number and 3rd variable is provided, output is assigned to 3rd variable"
        echo "Example: getparentnlevelup /tmp/test 2 res -> res is set as /"
        echo "Example: getparentnlevelup /tmp/test 2  -> prints /"
        echo "Example: getparentnlevelup /tmp/test  -> prints /tmp"
        echo "Example: getparentnlevelup /tmp/test res -> res is set as /tmp"
        echo "No parameter throws exit 1"
        echo "If dirorfilename does not exist throws exit 2"
        exit 0
    fi

    local numofparams=$#
    if [ ${numofparams} -lt 1 ]
    then
        echo "Mandatory to give the directory from where you need nth parent directory."
        exit 1
    fi
    local pathname=$1

    if [ ! -e ${pathname} ]
    then
        echo "Incorrect parameter. Directory or File not found."
        exit 2
    fi

    local re='^[0-9]+$'
    local parlevel=1
    local __resultvar=$3

    if [ ${numofparams} -gt 1 ]
    then
        secparam=$2
        if [[ ${secparam} =~ $re ]]
        then
            parlevel=${secparam}
        else
            __resultvar=$2
        fi
    fi

    for ((iternum=0; iternum<parlevel; iternum=iternum+1))
    do
        pathname=$(dirname ${pathname})
    done

    if [[ "$__resultvar" ]]
    then
        eval $__resultvar="'$pathname'"
    else
        echo "$pathname"
    fi
}