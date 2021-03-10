class CommandLine() :
    
    def __init__(self, inOpts=None) :
        
        import argparse
        self.parser = argparse.ArgumentParser(description = 'Extended Depth of Focus Image Processing Algorithm', 
                                             epilog = 'Takes, in multiple layers of image data of a given subject, and spits out a single infocus image of said subject.',  
                                             add_help = True, 
                                             prefix_chars = '-', 
                                             usage = '%(prog)s [options] -option1[default] <input >output'
                                             )

        self.parser.add_argument('-i','--images',action='append',default = None, help='Select the image/folder of images you choose to run the algorithm on.')
        self.parser.add_argument('-a','--algorithm', action = 'store', choices=('laplacian','sobel') , default = 'laplacian', help='Select the type of algorithm you want to run. Either Laplacian, or Sobel.' )
        self.parser.add_argument('-o','--outputD',action='store', help ='Name the output directory you wish to output to.')
        self.parser.add_argument('-n','--namingS',action = 'store', type = str, default= 'EDoFIP Output', help = 'Name the naming scheme you wish for the output images.')

        if inOpts is None :
            self.args = self.parser.parse_args()
        else :
            self.args = self.parser.parse_args(inOpts) 