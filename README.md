# ole_vba_extractor
Extract ole and vbs data from multiple file using oledump and olevba tools just past the microsoft files in feed folder and get output in output folder
# Required
- Python 2
first execute following commands in terminal
<code>pip install yara-python</code><br>
<code>pip install olefile</code><br>
<code>pip install oletools</code><br>
# Procedure
- Paste all the files in feed folder
- Run <code>chmod u+x ./script.sh</code> command in terminal
- Run <code>./script.sh</code>
# Known Bugs
<emp> Doesn't work on files with name contraining spaces </emp>
