def flat_list(a):
  return s_r(a,r=[])
def s_r(a, r):
  if type(a)!=list: r.append(a)
  else:
    for i in a: s_r(i,r)
  return r

if __name__ == '__main__':
  assert flat_list([1, 2, 3]) == [1, 2, 3], "1"
  assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "2"
  assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "3"
  assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "4"
