dic = [
   ['lets', 2],
   ['write', 1],
   ['a', 9],
   ['program', 1],
   ['that', 5],
   ['analyzes', 1],
   ['text', 1],
   ['line', 1],
   ['code', 1],
   ['something', 1],
   ['like', 1],
   ['example', 3]
]


def main():
   dic.sort()
   dic.sort(key=byFrequency, reverse=True)

   for pair in dic:
      print(" {:>15}: {}".format(*pair))


def byFrequency(pair):
   return pair[1]


main()
