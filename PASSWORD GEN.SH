#!/bin/bash

echo "please enter password lenght"
read PASS_LENGTH

for p in $(seq 1 5);
do
    openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done


#!/bin/bash

echo "please enter password lenght"
read PASS_LENGTH

for p in $(seq 1);
do
    openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done


test_shadow test_passwd(){
if [ -e /etc/passwd ];

echo "please enter password lenght"
read PASS_LENGTH

for p in $(seq 1 5);
do
    openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done
