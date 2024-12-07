class Time:
    def print_time(time):
        print('%d:%d:%d' % (time.hour,time.minutes,time.s))
start=Time()
start.hour=9 ; start.minutes=45 ; start.s=00
start.print_time() ; print() ; Time.print_time(start)
