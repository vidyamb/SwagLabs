class nm:
  def digit_pattern(n):
    for i in n:
        print("|", end=" ")
        print("*" * int(i))
n = "1234"
nm.digit_pattern(n)
