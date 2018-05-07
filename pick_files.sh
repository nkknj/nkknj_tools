#!/bin/bash
#$1: Input directory
#$2: filename
#$3: Output directory

indir=$1
filename=$2
outdir=$3

list=$(find $indir -name $filename -type f)

for f in $list ; do
	temp=${f#$indir/}
	temp=$(echo $temp | sed 's/\//_/g')
	cp $f $outdir/$temp
done

