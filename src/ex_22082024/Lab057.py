# Continue -> Skips the current iteration for a loop and moves to the next iteration
"""
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
  """
for number in range(10):
    if number % 2 == 0:
        continue  # we can also use Pass, but pass is a keyword which can be used in statements, functions, classes,
        # object, but continue can not be used in functions
    else:
        print(number)
