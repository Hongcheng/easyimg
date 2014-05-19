from mongoengine import *
import model
import uuid
import Image
import StringIO
# connect('Image')
import datetime
class ImgGroup(Document):
	Group_Img_List = ListField()
	Group_Name = StringField(max_length = 50, default = '')

# newGroup = ImgGroup()
# newGroup.Group_File_List.append('452e5d45-2c26-447f-8c4f-1056a023568c')
# newGroup.Group_File_List.append('a5443799-c52d-4a29-875a-e8b5e94f5589')
# newGroup.Group_File_List.append('9b025854-b73b-428b-a04b-beb9885cdd42')
# newGroup.Group_Name = "baidu"
# newGroup.save()

# newGroup = ImgGroup.objects()
# for i in newGroup:
# 	print i.Group_File_List

class ImgTemp(Document):
	Img = FileField()
	DateTime = DateTimeField()


class ImgSingle(Document):
	# UUID = StringField()
	Img = FileField()
	# comment = StringField()
# print uuid.uuid4()
# print int(uuid.uuid4())
# newImg = ImgSingle()
# img = open('../static/Img/7.jpg')
# newImg.UUID=	str(uuid.uuid4())
# newImg.Img = img
# newImg.comment="baidu3"
# newImg.save()

# imgs = ImgSingle.objects( UUID = "452e5d45-2c26-447f-8c4f-1056a023568c")
# for img in imgs:
# 	print  img.UUID
# 	Image.open(StringIO.StringIO(img.Img.read())).show()

'''insert the baoqiang and baidu img to mongoengine'''
# a = open('../static/Img/1.jpg')
# print type(a)
# newGroup = ImgGroup()
# newGroup.Group_Name="baobao"
# for i in range(4):
# 	newImg = ImgSingle()
# 	newImg.Img = open('../static/Img/'+str(i+1)+'.jpg')
# 	newImg.save()
# 	newGroup.Group_Img_List.append(newImg.id)
# newGroup.save()

# newGroup = ImgGroup()
# newGroup.Group_Name="baidu"
# for i in range(3):
# 	newImg = ImgSingle()
# 	newImg.Img = open('../static/Img/'+str(i+5)+'.jpg')
# 	newImg.save()
# 	newGroup.Group_Img_List.append(newImg.id)
# newGroup.save()

'''remove the temp Img,you should first delete the FileField.seconds was the timeout second'''
imgs = ImgTemp.objects()
for img in imgs:
	if  datetime.datetime.now() - img.DateTime > datetime.timedelta(seconds=60):
		print datetime.datetime.now() - img.DateTime
		img.Img.delete()
		img.delete()



# Image.open(StringIO.StringIO(img[0].Img.read())).show()