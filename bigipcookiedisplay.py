import sys;
#Input
if(len(sys.argv)>1):
        string = sys.argv[1];
else:
        print('Introduce la cookie:');
        string = input();
#Split with '.'
parts = string.split(".");
if(len(parts)!=3):
        print('El formato no coincide')
        sys.exit();
#IP
ip = hex(int(parts[0]));
ip = str(int(ip[8:10], base=16))+"."+str(int(ip[6:8], base=16))+"."+str(int(ip[4:6], base=16))+"."+str(int(ip[2:4], base=16));
#Port
port = hex(int(parts[1]));
port = str(int(port[4:6]+port[2:4] ,base=16));
#Print
print('La IP es:');
print('----------------');
print(ip+':'+port);
