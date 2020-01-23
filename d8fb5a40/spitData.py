import os,shutil
import json
import random

class COCO_Set():
    '''
    des:
    '''
    #定义类变量，完全不变
    categories = [
            {"supercategory": "\u74f6\u76d6\u7834\u635f", "id": 1, "name": "\u74f6\u76d6\u7834\u635f"},
            {"supercategory": "\u55b7\u7801\u6b63\u5e38", "id": 9, "name": "\u55b7\u7801\u6b63\u5e38"},
            {"supercategory": "\u74f6\u76d6\u65ad\u70b9", "id": 5, "name": "\u74f6\u76d6\u65ad\u70b9"},
            {"supercategory": "\u74f6\u76d6\u574f\u8fb9", "id": 3, "name": "\u74f6\u76d6\u574f\u8fb9"},
            {"supercategory": "\u74f6\u76d6\u6253\u65cb", "id": 4, "name": "\u74f6\u76d6\u6253\u65cb"},
            {"supercategory": "\u80cc\u666f", "id": 0, "name": "\u80cc\u666f"},
            {"supercategory": "\u74f6\u76d6\u53d8\u5f62", "id": 2, "name": "\u74f6\u76d6\u53d8\u5f62"},
            {"supercategory": "\u6807\u8d34\u6c14\u6ce1", "id": 8, "name": "\u6807\u8d34\u6c14\u6ce1"},
            {"supercategory": "\u6807\u8d34\u6b6a\u659c", "id": 6, "name": "\u6807\u8d34\u6b6a\u659c"},
            {"supercategory": "\u55b7\u7801\u5f02\u5e38", "id": 10, "name": "\u55b7\u7801\u5f02\u5e38"},
            {"supercategory": "\u6807\u8d34\u8d77\u76b1", "id": 7, "name": "\u6807\u8d34\u8d77\u76b1"}]        

    def __init__(self,name,images_path='./images/',json_path='./'):
        #初始化coco数据集基本信息
        self.name=name
        self.images_pth=images_path
        self.json_path=json_path
        self. info=[]
        self.images = []
        self.license = []
        self.annotations=[]
        self.json_file=None

    #转化json对象为python对象
    def load_json(self):
        with  open(self.json_path)  as f:
            self.json_file = json.load(f)     #读入到python对象
            return self.json_file
        return None
    #获取json values
    def get_items(self,key):
        return self.json_file[key]
    
    #写入json
    def write_file(self,json_name):        
        self.write_json = {'info':self.info,'images':self.images,'license':self.license,'categories':self.categories,'annotations':self.annotations} 
        with open(json_name, "w") as f:
            json.dump( self.write_json, f,indent=4)



def main():
    DATASET_PATH =  '/home/w/Desktop/TC/data/'
    Src = DATASET_PATH+'images/'
    origin_json=DATASET_PATH+'annotationsw.json'
    train_json=DATASET_PATH+'train/tra_annotations.json'
    val_json=DATASET_PATH+'val/val_annotations.json'
   
    origin_set=COCO_Set('origin',images_path=Src,json_path=origin_json)
    train_set=COCO_Set('train',images_path=Src,json_path=train_json)
    val_set=COCO_Set('val',images_path=Src,json_path=val_json)

    origin_json_obj = origin_set.load_json()
    # if not train_json_obj:
    #     return 
    
    images_list=origin_json_obj['images']   #获取json文件中的images的列表
    random.shuffle(images_list)   #随机打乱整个列表
    images_num=len(images_list)
    print(images_num)
    val_set.images=images_list[:int(0.3*images_num)]  #取出前30%的数据作为验证集存入val_set中
    train_set.images=images_list[int(0.3*images_num):]  #取出剩下的
    print(len( train_set.images))

    annotations_list=origin_set.get_items("annotations")
    print(len(annotations_list))
    image_id_list=[image['id'] for image in val_set.images ]    #获取val_set.images中每个元素的id形成新的列表
     #找出train与val重合的图片的annotations
    val_set.annotations=[annotation for  annotation in annotations_list if (annotation["image_id"] in image_id_list)] 
    print(len(val_set.annotations))
    val_set.write_file(val_json)
    
    #获取train_set.images中每个元素的id形成新的列表
    image_id_list=[image['id'] for image in train_set.images ] 
    #找出train与val重合的图片的annotations
    train_set.annotations=[annotation for  annotation in annotations_list if (annotation["image_id"] in image_id_list)]  
    print(len(train_set.annotations))
    train_set.write_file(train_json)


if __name__ == "__main__":
    main()
