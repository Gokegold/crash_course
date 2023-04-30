#!/bin/bash
#function File {
    # think you are inside the file
    # Change Here
#    echo $#
#}

# Do not change anything
#if [ ! $# -lt 1 ]; then
#    File $*
#    exit 0
#fi

# change here
# here you can pass the arguments
#bash prog.sh Shell is fun
'''
echo -e "Enter file_name: \c"
read file_name
if [ -d $file_name ]
then
    echo "FOUND"
elif [ ! -d $file_name ]
then
    mkdir -p $file_name && echo "JUST CREATED"
fi
'''
let win=0
let lose=0
x=""

if [ "$#" -lt 2 ]
then
    echo "How many times do you want to roll"
    read rolls

    echo "How many dice do you want to roll"
    read dice_num

else
    rolls=$1
    dice_num=$2
fi

dice=[ red yellow yellow green green green ]

for i in $(seq 1 $dice_num)
do
    for y in $(seq 1 $dice_num)
    do
        x="${x}${dice[$(($RANDOM%5))]},"
    done

    echo "$x"
    outcome="$(echo "$x"|grep red|grep -v green)"
    if [ "$outcome" == ""]
    then
        let win+=1
    fi
done
