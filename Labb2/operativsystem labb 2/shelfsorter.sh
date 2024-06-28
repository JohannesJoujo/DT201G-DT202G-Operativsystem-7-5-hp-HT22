#! /bin/bash

inp=$1
in=$2


if [[ $in == i ]] && [[ $inp == -s ]]; 
then
head -1
sort  -k1 | sed "s/,/ /g" 
fi


if [[ $in == n ]] && [[ $inp == -s ]]; 
then
head -1
sort  -k2 |sed "s/,/ /g"  
fi


if [[ $in == v ]] && [[ $inp == -s ]]; 
then
head -1
sort   -t "," -nk3 | sed "s/,/ /g" 
fi

if [[ $in == l ]] && [[ $inp == -s ]]; 
then
head -1
sort  -t "," -nk4 | sed "s/,/ /g" 
fi


if [[ $in == b ]] && [[ $inp == -s ]]; 
then
head -1
sort  -t "," -nk5 | sed "s/,/ /g" 
fi

if [[ $in == h ]] && [[ $inp == -s ]]; 
then
head -1
sort -t "," -nk6 | sed "s/,/ /g" 
fi

if [[ $inp == -p ]]; 
then
head -1
sed "s/,/ /g" 
 
fi

if [[ $inp == --help ]]; 
then

echo "Usage : shelfsorter [ - p | - s { i | n | v | l | b | h }]"
echo "Used primarily for sorting furniture data which is"
echo "read through stdin ."
echo "-p print data contents and exit"
echo "-s sort by additional argument : id ( i ) ,"
echo "name ( n ) , weight ( v ) , length ( l )"
echo "width ( b ) , height ( h ) , print data"
echo "contents and exit"
echo "-- help display this help and exit"

fi
