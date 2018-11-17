#!/bin/bash
for i in $( ls ); do
  if [[ $i = *.ui ]]
  then
    pyuic5 $i -o ${i%.*}.py
  fi
done
mv *.py ../src
