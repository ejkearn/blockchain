def do_print(funct, *inf):
  for x in inf:
    print('the stuff{:^20}'.format(funct(x)))

do_print(lambda thing: thing +2, 1,2,3,4,5)

