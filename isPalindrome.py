#!usr/bin

strg = 'y'
strgLength = len(strg)
i = 0
while i <= strgLength/2 :
	if(strg[i] == strg[strgLength - i - 1]) :
		i += 1
		continue
	else :
		break

if(i == (strgLength / 2) + 1) :
	print('yes')
