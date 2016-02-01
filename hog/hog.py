from die import Die

d = Die(6)
for r in range(100000):
    d.roll()

d.histogram()
