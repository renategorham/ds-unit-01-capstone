s(){ source $BASH_SOURCE; }
v(){ vi $BASH_SOURCE; }
c(){ spellcheck $BASH_SOURCE; }
alias t='clean-readbyline ./data/FIN.Mx_1x1.txt'

clean-readbyline(){
    while read line; do
        re="[0-9]\."
	re2="\. "
	repl=0.0
	if [[ $line =~ $re2 ]] && [[ ! $line =~ $re ]]  ; then
           tr $re2 $repl	
	   echo $line
        fi
    done < $1
}
