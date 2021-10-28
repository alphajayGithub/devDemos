#! /bin/bash

TARGET_NAME=excelParser
TARGET_ENTRY=main.py
PROJECT_ROOT=excelParser
PACKAGE_NAME=excelParser


CURRENT_PATH=`pwd`
ROOT_PATH=`cd .. && pwd`

BUILD_LINUX=$ROOT_PATH/build_linux
BUILD_WIN=$ROOT_PATH/build_win
RELEASE_DIR=$ROOT_PATH/release
VENV_LINUX=$ROOT_PATH/VirtualEnvs/devDemos

build()
{
if [ ! -d $BUILD_LINUX ]
then
    mkdir $BUILD_LINUX
fi
cd $BUILD_LINUX

echo  "target build dir is $BUILD_LINUX"
echo  "ready to build under venv:  $VENV_LINUX"
sleep 3

mv $ROOT_PATH/$PROJECT_ROOT/$TARGET_ENTRY  $ROOT_PATH/$PROJECT_ROOT/$TARGET_NAME

source $VENV_LINUX/bin/activate
pip list
pyinstaller -F -n $TARGET_NAME ../excelParser/$TARGET_NAME --clean
ls -al dist/*
file dist/*
deactivate

mv $ROOT_PATH/$PROJECT_ROOT/$TARGET_NAME $ROOT_PATH/$PROJECT_ROOT/$TARGET_ENTRY
cd $CURRENT_PATH
echo -----------------------------------------------
echo build successfully

eval "sudo chmod 777 $BUILD_WIN -R"
}

release()
{

declare -i sum=0

if [ ! -d $RELEASE_DIR ]
then
    mkdir $RELEASE_DIR -p
fi
cd $RELEASE_DIR
rm -rf *
mkdir bin conf

cd $RELEASE_DIR/conf

echo "set EXECUTABLE=\"../bin/$TARGET_NAME.exe\"" >setEnv.bat
echo "EXECUTABLE=\"../bin/$TARGET_NAME\"" >setEnv.sh
echo "create Env setting file:"
ls -al $RELEASE_DIR/conf/setEnv.*

cp -v $ROOT_PATH/$PROJECT_ROOT/conf/logging.*  $RELEASE_DIR/conf
cp -v $BUILD_WIN/dist/*   $RELEASE_DIR/bin
cp -v $BUILD_LINUX/dist/* $RELEASE_DIR/bin

cmd=dataWash
EXECUTE_LINUX="eval \"\$EXECUTABLE -op $cmd  \$@\""
echo "source setEnv.sh" >$cmd.sh
echo $EXECUTE_LINUX>>$cmd.sh
echo "$sum: create $cmd.sh"

EXECUTE_WIN="%EXECUTABLE% -op $cmd  %*"
echo "@echo off"       >$cmd.bat
echo "call setEnv.bat">>$cmd.bat
echo $EXECUTE_WIN     >>$cmd.bat
echo "$sum: create $cmd.bat"

}

package()
{
echo "-----------------------------------------------------------"
cd $RELEASE_DIR
chmod 777 * -R

eval "tar zcvf $PACKAGE_NAME.tgz  bin/$TARGET_NAME  conf/logging.*    conf/*.sh "
echo "----------- package into $PACKAGE_NAME.tgz done ------------"

eval "zip $PACKAGE_NAME.zip  bin/$TARGET_NAME.exe   conf/logging.*  conf/*.bat"
echo "----------- package into $PACKAGE_NAME.zip done ------------"

ls *.*
mv *.* ..
pwd
}

all()
{
	build
	sleep 3
	release
	sleep 3
	package
}

help(){
 echo "Usage:  $0 -r <build/release/all> "
 echo ""
 exit 1
}

if [[ "$1" == "" ]] || [[ "$1" == "-h" ]] ||[[ "$1" == "--help" ]];then
	help
	exit 1
fi

while getopts r: option
do
        case "${option}"
        in
                r)  eval "$OPTARG"
                    ;;
                \?) help
                    exit 1
                    ;;
        esac
done
