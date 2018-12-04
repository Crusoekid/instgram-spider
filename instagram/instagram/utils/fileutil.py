import os
from ..spiders.constantant import *


class fileHandler:
    def existuserfolder(self,username):
        path = SAVE_PHOTO_PATH.format(username)
        if not os.path.exists(path):
            os.mkdir(path)
        return path
    
    def existphotofolder(self):
        if not os.path.exists(BASE_PHOTO_PATH):
            os.mkdir(BASE_PHOTO_PATH)

    def existtestfolder(self):
        if not os.path.exists(SAVE_TEST_PATH):
            os.mkdir(SAVE_TEST_PATH)

    def existportraitfolder(self):
        if not os.path.exists(SAVE_PORTRAIT_PATH):
            os.mkdir(SAVE_PORTRAIT_PATH)

    def writefile(self, imgs):
        if os.path.exists(SAVE_TEST_PATH + SAVE_PIC_LINK):
            with open(SAVE_TEST_PATH + SAVE_PIC_LINK, 'w') as file:
                file.write(imgs) 
        else:
            with open(SAVE_TEST_PATH + SAVE_PIC_LINK, 'a') as file:
                file.write(imgs)
        file.close()