# Start of Units of Time
d = int(input("Enter a number of days: "))
h = int(input("Enter a number of hours: "))
m = int(input("Enter a number of minutes: "))
s = int(input("Enter a number of seconds: "))

Totalsec = ((d * 24 * 60 * 60) + (h * 60 * 60) + (m * 60) + (s))

Totalsec = str(Totalsec)

print("The total number of seconds is " + Totalsec)
# End of Units of Time


# Start of Units of Time (again)
S = int(input("Enter number of seconds: "))

ps = S % 60
pm = (S//60)
ph = (pm//60)
pd = (ph//24)
pm = (pm % 60)
ph = (ph % 24)

if (ps < 10):
    ps = str(ps)
    ps = "0" + ps
if (pm < 10):
    pm = str(pm)
    pm = "0" + pm
if (ph < 10):
    ph = str(ph)
    ph = "0" + ph
if (pd < 10):
    pd = str(pd)
    pd = "0" + pd

ps = str(ps)
pm = str(pm)
ph = str(ph)
pd = str(pd)

print(pd + " " + "days" + " " + ph + " " + "hours" + " " + pm + " " + "minutes" + " " + ps + " " + "seconds")
# End of Units of Time (again)


# Start of Current Time
import time

p = time.asctime()

print(p)
# End of Current Time