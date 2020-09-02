
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input( '../images/MFCC.png',width=10, height=4,to='(0,2.2,0)' ),
    to_Conv("conv1", "7x1", 32, offset="(1,1,0)", to="(0,0,0)", width=1, height=20, depth=35, caption="Conv Mish" ),

    to_Pool("maxpool1",zlabel='MaxPool 2x1', offset="(2,1,0)",width=1, height=15, depth=25, caption=""),
    to_connection("conv1","maxpool1"),
    to_Dropout( "dp2", dp_rate="Dropout 70\%", offset="(4,0.5,0)", to="(0,0,0)", width=1.5, height=3, depth=25),
    to_connection("maxpool1","dp2"),

    to_Conv("conv2", "5x1", 16, offset="(5,0,0)", to="(0,0,0)",width=1, height=15, depth=25, caption="Conv Mish" ),
    to_connection("dp2","conv2"),
    to_Pool("maxpool2",zlabel='MaxPool 2x1', offset="(7,0,0)",width=1, height=10, depth=25, caption=""),
    to_connection("conv2","maxpool2"),
    to_Dropout( "dp3", dp_rate="Dropout 70\%", offset="(9,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25),
    
    to_connection("maxpool2","dp3"),



    to_Conv("conv3", "3x1", 8, offset="(10,0,0)", to="(0,0,0)",width=1, height=10, depth=20, caption="Conv Mish" ),
    to_connection("dp3","conv3"),
    to_Pool("maxpool3",zlabel='MaxPool 2x1', offset="(12,0,0)",width=1, height=7, depth=20, caption=""),
    to_connection("conv3","maxpool3"),
    to_Dropout( "dp4", dp_rate="Dropout 70\%", offset="(14,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25),
    to_connection("conv3","dp4"),

    
    to_Conv("conv4", "2x1", 4, offset="(15,0,0)", to="(0,0,0)",width=1, height=7, depth=17, caption="Conv Mish" ),
    to_connection("dp4","conv4"),
    to_Pool("maxpool4",zlabel='MaxPool 2x1', offset="(17,0,0)",width=1, height=5, depth=17, caption=""),
    to_connection("conv4","maxpool4"),
    to_Dropout( "dp5", dp_rate="Dropout 70\%", offset="(19,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25),
    to_connection("conv4","dp5"),

    to_Dense("dense2", 100 ,offset="(21,0,0)", caption="FC Mish",depth=40,Color ="\FcEluColor" ),
    #to_SoftMax("soft2", 10 ,"(5,0,0)", caption="SoftMax"  ),
    to_connection("dp5","dense2"),
    to_Dropout( "dp6", dp_rate="Dropout 70\%", offset="(23,0.0,0)", to="(0,0,0)", width=1.5, height=3, depth=25),
    to_connection("dense2","dp6"),
    to_Dense("dense3", 1 ,offset="(25,0,0)", caption="FC Sigmoid",Color ="\FcSoftmaxColor",depth=15 ),
    to_connection("dp6","dense3"),
    
    #to_connection("dense1", "soft1"),  
    #to_connection("pool2", "soft1"),    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()

