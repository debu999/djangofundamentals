#!/usr/bin/env bash
set -e

if [ $# -lt 3 ]
then
	echo "To start application please provide parameters in following format."
	echo "startapp.sh pkgname.wsgimodulename server:port applicationname [numberofworkers]"
	exit 1
fi
dt=$(date +"%Y%m%d %H:%M:%S")
{
readarray -d . -t arr <<< "${1}"
pkgname=$(echo ${arr[0]} | xargs)
modulename=$(echo ${arr[1]} | xargs)
}||{
echo Please check again first input its not in format pkgname.wsgimodulename
echo Received parameter is ${1}
}
{
readarray -d : -t arr <<< "${2}"
svrname=$(echo ${arr[0]} | xargs)
port=$(echo ${arr[1]} | xargs)
}||{
echo Please check again second input its not in format servername:port
echo Received parameter is ${2}
}

echo -e "System received the following parameters\n1.PackageName: ${pkgname}\n2.ModuleName: ${modulename}"
applicationname=${3}
numofworkers=${4}

if [ -z ${numofworkers} ]
then
    echo "3.NumberofWorkers(Default): 1"
    numofworkers=1
else
    echo "3.NumberofWorkers: ${numofworkers}"
fi
echo -e "4.ServerName: ${svrname}\n5.PortNumber: ${port}\n6.ApplicationName: ${applicationname}"
echo Starting the application ${pkgname}.${modulename} with gunicorn server binding at ${svrname}:${port}

pr=$(ps aux | grep -v "stopapp.sh\|startapp.sh" | grep gunicorn | grep ${pkgname}.${modulename} | awk '{ print $2 }')

currfile=$(readlink -f ${BASH_SOURCE})
currdir=$(dirname ${currfile})

if [ "${pr}" != "" ]
then
	echo Stopping current application processes for the application "${pkgname}.${modulename}"
	${currdir}/stop.sh ${pkgname}.${modulename}
	echo "System will spawn new processes."
else
	echo -e "No current process running for application ${pkgname}.${modulename}.\nSystem will spawn new processes."
fi

echo "Checking PATH before starting the server to ensure the package ${pkgname} is discoverable"

source ${currdir}/utils.sh

packagedir=$(getparentnlevelup ${currdir} 2)
cd $packagedir
echo $packagedir
echo $(pwd)
PATH=${PATH}:${packagedir}

export PATH=$(echo $PATH | tr ':' '\n' | uniq | tr '\n' ':' | sed -e's/:$/\n/')
echo "PATH Set for server start is : $PATH"

if [ ${numofworkers} -lt 2 ]
then
    echo gunicorn -b ${svrname}:${port} ${pkgname}.${modulename}:application
    gunicorn -b ${svrname}:${port} ${pkgname}.${modulename}:application --access-logfile - --error-logfile - --log-file - --log-level debug --capture-output --enable-stdio-inheritance
else
    echo gunicorn -w ${numofworkers} -D -b ${svrname}:${port} ${pkgname}.${modulename}:application
    gunicorn -w ${numofworkers} -b ${svrname}:${port} ${pkgname}.${modulename}:application --access-logfile - --error-logfile - --log-file - --log-level debug --capture-output --enable-stdio-inheritance
fi

#sleep .5
#echo validate gunicorn processes started in the system.
#ps aux | grep -v "stopapp.sh\|startapp.sh\grep" | grep gunicorn | grep ${pkgname}.${modulename}
#echo "Web application started at ${dt} with ${numofworkers} worker nodes and 1 masternode"