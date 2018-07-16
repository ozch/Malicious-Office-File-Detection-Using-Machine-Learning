#/bin/bash
ADD=$0
IN_DIR="./feed/*"
IN_DIRO="./feed/"
OUT_DIR="./output/"
LEN=${#IN_DIR}
ULEN=$((LEN-1))

echo "List of Files to be Processed..."
echo "================================================================"
for file in $IN_DIR
 do
  echo $file
 done

echo "================================================================"
echo "Starting Now..."


for file in $IN_DIR
 do
  VR1=${file:7}
  echo "File Name : $VR1"
  VR="$OUT_DIR$VR1"
  VRS=${VR:2}
  echo "Check if the Directory Exist at Loc : $VRS"
  P1=${ADD//script.sh/$VSR}
  P2=$P1$VRS
  P3=${P2//./_}
  P4=${P3// /_}
  P5=${P4:1}
  PT="$PWD$P5"
  echo $PT
  if [ ! -d $PT ]; then
    mkdir $PT;
  fi;
  OUTX=${PT:30:25}
  OUTY=".$OUTX"
  echo $OUTY
  echo "================================================================"
  VRG="python oledump.py $file --dir $OUTY"
  echo ">> Executing Command : $VRG"
  $VRG
  vba="python olevba.py -d $file"
  echo ">> Executing Command : $vba"
  $vba >> "$OUTY/Macros.txt"
  
 done

#python oledump.py ./feed/docm.docm --dir ./output/docx.docx
