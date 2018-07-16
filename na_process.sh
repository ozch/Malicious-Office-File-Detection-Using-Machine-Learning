X=1
for file in *.doc;
do
 echo "RENAMING:" $file
 mv "$file" "DOC$X.doc";
 X=$((X+1))
done
X=1
for file in *.docx;
do
 echo "RENAMING:" $file
 mv "$file" "DOCX$X.docx";
 X=$((X+1))
done


X=1
for file in *.DOC;
do
 echo "RENAMING:" $file
 mv "$file" "DOC$X.doc";
 X=$((X+1))
done
X=1
for file in *.DOCX;
do
 echo "RENAMING:" $file
 mv "$file" "DOCX$X.docx";
 X=$((X+1))
done

X=1
for file in *.PPTX;
do
 echo "RENAMING:" $file
 mv "$file" "PPTX$X.pptx";
 X=$((X+1))
done
X=1
for file in *.PPT;
do
 echo "RENAMING:" $file
 mv "$file" "PPT$X.ppt";
 X=$((X+1))
done

X=1
for file in *.pptx;
do
 echo "RENAMING:" $file
 mv "$file" "PPTX$X.pptx";
 X=$((X+1))
done
X=1
for file in *.ppt;
do
 echo "RENAMING:" $file
 mv "$file" "PPT$X.ppt";
 X=$((X+1))
done
