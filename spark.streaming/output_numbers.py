from sys    import stdout
from time   import sleep
from random import choice

cycle_through = range(50)
while True:
    for i in cycle_through:
        sleep(1.0)
        times_ten = i * 10
        print choice( range(times_ten, times_ten + 10) )
        stdout.flush()
