#!/bin/python
print "*%\@/*%$%*\@/*%$%*\@/*%$%*\@/*%$%*<*>*%$%*\@/*%$%*\@/*%$%*\@/*%$%*\@/*%$%*\@/*"
print "*  X   !   X   !   X   !   X   !       !   X   !   X   !   X   !   X   !   X *"
print "*      O       O       O    *** I   LOVE  XNXX ***     O       O       O     *"
print "*  X   !   X   !   X   !   X   !       !   X   !   X   !   X   !   X   !   X *"
print "*%/@\*%$%*/@\*%$%*/@\*%$%*/@\*%$%*<*>*%$%*/@\*%$%*/@\*%$%*/@\*%$%*/@\*%$%*/@\*"
try:
	year=input("Enter year.........eg.'1885','1988','2016',etc\n:")
	month=input("Enter month..........eg.'1','9','12',etc\n:")
	day=input("Enter day.........eg.'1','12','20','31',etc\n:")
except:
	print "fuck you baby.something is wrong"
else:
	myear=year
	mmonth=month
	mday=day

	if month == 1 :
		mh=0;
		hm=3;
	elif month == 10 :
		mh=0;
		hm=4;
	elif month == 5 :
		mh=1;
		hm=5;
	elif month == 8 :
		mh=2;
		hm=6;
	elif month == 2 :
		mh=3;
		hm=6;
	elif month == 3 :
		mh=3
		hm=0
	elif month == 11 :
		mh=3
		hm=0
	elif month == 6 :
		mh=4
		hm=1
	elif month == 9 :
		mh=5
		hm=2
	elif month == 12 :
		mh=5
		hm=2
	elif month == 4 :
		mh=6
		hm=3
	elif month == 7 :
		mh=6
		hm=3
	else:
		print "fuck you baby.something is wrong"
	while year>28:
		year-=28
	y=year%4
	if y==0 :
		x=year/4
		result=year+x+hm+day-5
		result=result%7
	else:
		x=year/4
		result=year+x+mh+day-1
		result=result%7
	if result == 0 :
		ans="saturday"
	elif result == 1 :
		ans="sunday"
	elif result == 2 :
		ans="monday"
	elif result == 3 :
		ans="tuesday"
	elif result == 4 :
		ans="wednessday"
	elif result == 5 :
		ans="thursday"
	elif result == 6 :
		ans="friday"
	print "your day is:"
	print ans
	if mmonth == 4 :
		if day<17 :
			myanyear=myear-639
		else:
			myanyear=myear-638
	elif mmonth<4 :
		myanyear=myear-639
	else:
		myanyear=myear-638
	print "your myanmar year is:" 
	print myanyear
	if ans == "sunday" :
		d=1
		e=1
	elif ans == "monday" :
		d=2
		e=2
	elif ans == "tuesday" :
		d=3
		e=3
	elif ans == "wednessday" :
		d=4
		e=4
	elif ans == "thursday" :
		d=5
		e=6
	elif ans == "friday" :
		d=6
		e=0
	elif ans == "saturday" :
		d=7
		e=5
	else:
		print "fuck you baby.something is wrong"  

	while myanyear>7:
		myanyear-=7

	if myanyear<d :
		myanyear+=7
	x=myanyear-d
	if x == 0 :
		print "you are bingaphwar"
	elif x == 1 :
		print "you are ahtunphwar"
	elif x == 2 :
		print "you are rarzaphwar"
	elif x == 3 :
		print "you are adipatiphwar"
	elif x == 4 :
		print "you are maranaphwar"
	elif x == 5 :
		print "you are thikephwar"
	elif x == 6 :
		print "you are putiphwar"
	else:
		print "Fuck You,something is wrong"
	raw_input("press enter to continue")
	print "*%\@/*%$%*\@/*%$%*\@/*%$%*\@/*%$%*<*>*%$%*\@/*%$%*\@/*%$%*\@/*%$%*\@/*%$%*\@/*"
	try:
		age=input("\n enter your age\n")
	except:
		print "Fuck You,something is wrong"
	else:	
		b=0
		if y == "sunday":
			b+=1
		elif y == "monday":
			b+=2
		elif y == "tuesday":
			b+=3
		elif y == "wednessday":
			b+=4
		elif y == "thursday":
			b+=6
		elif y == "friday":
			b+=0
		elif y == "saturday":
			b+=5
		else:
			print "thank you\n"
		cur=age+b-1
		cur%=8
		if cur == 1:
			print "you are in sun"	
		elif cur == 2:
			print "you are in moon"
		elif cur == 3:
			print "you are in mars"
		elif cur == 4:
			print "you are in marcury"
		elif cur == 5:
			print "you are in saturn"
		elif cur == 6:
			print "you are in jupiter"
		elif cur == 7:
			print "you are in rahu"
		elif cur == 0:
			print "you are in venus"
		else:
			print "fuck you , something is wrong"
raw_input("press <enter> to restarting")	

















