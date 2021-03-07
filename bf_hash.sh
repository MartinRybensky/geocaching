#!/bin/bash

SALT=
DESIRED_HASH=
for XXX in {000..999}
do

  for YYY in {000..999}
  do 

    echo "N49:50."$XXX"E014:39."$YYY >> vysledky.txt
    mkpasswd -m md5 "N49:50."$XXX"E014:39."$YYY OBHyaf1O >> vysledky.txt
    echo " " >> vysledky.txt

    
  done

done



