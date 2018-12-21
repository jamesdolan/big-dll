

for i in range(0,100):
  f = open('src/functions%d.cpp' % i,  'w')
  for j in range(0,1000):
    idx = i*1000 + j
    f.write('__declspec(dllexport) int function%d(int i) { return i + %d; }\n' % (idx, idx))
