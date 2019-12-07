
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input( '../images/espectrogram.png',width=10, height=4,to='(0,2.2,0)' ),

    to_Dropout( "dp0", dp_rate="40\%", offset="(-0.2,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, caption="Dropout"),
    to_Rnn("dense1", 128 ,offset="(2,0,0)", caption="RNN ReLU",Color ="\FcReluColor",depth=5,width=5, height=5 ),#relu color is default
    to_connection("dp0","dense1"),
    #to_SoftMax("soft1", 10 ,"(2,0,0)", caption="Elu"  ),
    to_Dropout( "dp1", dp_rate="40\%", offset="(4.5,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, caption="Dropout"),
    to_connection("dense1","dp1"),
    to_Dense("dense2", 570 ,offset="(7.5,0,0)", caption="FC2 ReLU",depth=60 ),
    
    #to_SoftMax("soft2", 10 ,"(5,0,0)", caption="SoftMax"  ),
    to_connection("dp1","dense2"),
    to_Dropout( "dp2", dp_rate="40\%", offset="(9.5,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, caption="Dropout"),
    to_connection("dense2","dp2"),
    to_Dense("dense3", 20 ,offset="(11.5,0,0)", caption="FC3 SoftMax",Color ="\FcSoftmaxColor",depth=30 ),
    to_connection("dp2","dense3"),
    
    #to_connection("dense1", "soft1"),  
    #to_connection("pool2", "soft1"),    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
