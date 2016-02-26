import filecmp
import traceback
import os
import time

from PIL import Image

class imageHandler():

    def __init__(self):
        pass

    def __del__(self):
        del self

    def ImageComp(self, img1, img2, ResultFile, bound=(0, 0, 0, 0)):
        TIMEFORMAT='%Y_%m_%d-%H-%M-%S'
        
        try:
            if bound == (0, 0, 0, 0):
                self.img1 = os.path.join(os.path.dirname(img2),img1.split('\\')[-1].split('.png')[0]+'_RefFor%s'%(ResultFile)+'.png')
                self.img2 = time.strftime(TIMEFORMAT,time.localtime(time.time()))+''+ResultFile+''+'.png'
                Image.open(img1).save(self.img1)
                Image.open(img2).save(self.img2)
                return filecmp.cmp(self.img1,self.img2)
            else:
                self.img1 = os.path.join(os.path.dirname(img2),img1.split('\\')[-1].split('.png')[0]+'_RefFor%s_Cropped'%(img2.split('\\')[-1].split('.png')[0])+str(bound)+'.png')
                self.img2 = os.path.join(os.path.dirname(img2),time.strftime(TIMEFORMAT,time.localtime(time.time()))+''+ResultFile+'_Cropped'+str(bound)+'.png')
                Image.open(img1).crop(bound).save(self.img1)
                Image.open(img2).crop(bound).save(self.img2)
                return filecmp.cmp(self.img1,self.img2)
        except:
            raise Exception(traceback.print_exc())
