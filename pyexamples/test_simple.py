
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input( '../examples/fcn8s/cats.jpg' ),
    to_Dense("dense1", 100 ,offset="(0,0,0)", caption="FC1" ),
    to_SoftMax("soft1", 10 ,"(4,0,0)", caption="SOFT"  ),
    to_connection("dense1", "soft1"),  
    #to_connection("pool2", "soft1"),    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
