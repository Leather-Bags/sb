from time import sleep


def elapsed_time(begin: int, end: int) -> str:  # Convert time to '<hours>h <minutes>m <seconds>s' style
    elapsed = end - begin
    if elapsed // 60 > 0:
        if (elapsed // 60) // 60 > 0:
            return f'{(elapsed // 60) // 60}h {(elapsed // 60) % 60}m {(elapsed % 60) % 60}s'
        else:
            return f'{elapsed // 60}m {elapsed % 60}s'
    else:
        return f'{elapsed}s'


def bytes_convert(b: int) -> str:  # Convert bytes to Pb/Tb/Gb/Mb/Kb style
    r = ['B', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']
    mr = 0
    while True:
        if b / 1024 > 1:
            b = b / 1024
            mr += 1
        else:
            b = round(b, 2)
            break
    return f'{b}{r[mr]}'


def hertz_convert(hz: int) -> str:  # Convert Hertz to Mhz/Ghz style
    r = ['Mhz', 'Ghz']
    mr = 0
    while True:
        if hz / 1000 > 1:
            hz = hz / 1000
            mr += 1
        else:
            hz = round(hz, 3)
            break
    return f'{hz}{r[mr]}'


def freeze(delay: int = 0):
    if delay:
        sleep(delay)
    else:
        while True:
            sleep(1)
