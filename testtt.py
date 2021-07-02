def bracket_match(text):
  # lis = []
  count = 0
  res = 0
  for i in range(len(text)):
    if text[i] == '(':
      count += 1
    elif text[i] == ')' and count == 0:
      res += 1
    else:
      count -= 1
  return res + count

print(bracket_match(')(()'))