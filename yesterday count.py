f=open("yesterday.song.txt",'r')
yesterday_lyric=""
while 1:
    line = f.readline()
    if not line: break
    yesterday_lyric = yesterday_lyric + line.strip() +"\n"
f.close()
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
print "Number of A Word 'YESTERDAY'", n_of_yesterday

print "=============================="
