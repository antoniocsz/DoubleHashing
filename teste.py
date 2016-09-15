import os, pickle, struct

myfile = open('_teste.dat', 'w+b')
myfile.write(struct.pack('L', 0)) # write a long of zeroes
index = []
for o in objects:
    index.append(myfile.tell())
    pickle.dump(o, myfile)
index_loc = myfile.tell()
pickle.dump(index, myfile)
myfile.seek(0, 0,  os.SEEK_SET)
myfile.write(struct.pack('L', index_loc))
