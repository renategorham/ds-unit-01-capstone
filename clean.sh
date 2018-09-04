s(){ source $BASH_SOURCE; }
v(){ vi $BASH_SOURCE; }
c(){ spellcheck $BASH_SOURCE; }
alias t='clean-readbyline ./data/FIN.Mx_1x1.txt'

 clean-readbyline(){
    #while read line; do
    while IFS=, read line; do
        re="[0-9]\.[0-9]+"
	re2="\s\."
	repl=0.0
	if [[ $line =~ $re2 ]] ; then 
	# && [[ ! $line =~ $re ]]  ; then
	echo "${line//./0.0}"
        fi   
    done < $1
}
