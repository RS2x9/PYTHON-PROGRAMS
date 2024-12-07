class Time :
    print('hi')
time = Time()
start,duration=Time(), Time()
start.h=0 ; start.m=0 ; start.s=0 ; duration.h=1 ; duration.m=35 ; duration.s=0
def add_time(t1,t2):
    sums = Time()
    sums.h=t1.h+t2.h ; sums.m=t1.m + t2.m ; sums.s=t1.s+t2.s ; return sums
def print_time(t):
    print('%d:%d:%d' % (t.h,t.m,t.s))
f"{print_time(add_time(start,duration))}".center(100)
