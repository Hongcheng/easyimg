from mongoengine import *
import os
import ImageFont
import Image
import ImageDraw
import StringIO
import datetime
import uuid
connect('Image')

class ImgSingle(Document):
	Img = FileField()
	
class ImgGroup(Document):
	Group_Img_List = ListField()
	Group_Name = StringField(max_length = 50, default = '')

class ImgTemp(Document):
	Img = FileField()
	DateTime = DateTimeField()

def PathGroup(gunm):
	newGroup = ImgGroup.objects()
	filepath = []

	for i in range(len(newGroup[gunm].Group_Img_List)):
		filepath.append("/api/img/"+str(newGroup[gunm].Group_Img_List[i]))
	return filepath


def ImgHandler(gnum,TextList):
	FontFolder = 'static/Font'
	font = ImageFont.truetype(FontFolder + "/simsun.ttc",34)
	width = 200
	height=0
	h_pos = 0

	restGroup = ImgGroup.objects()
	filepath=[]

	for i in range(len(restGroup[gnum].Group_Img_List)):
		filepath.append((str(restGroup[gnum].Group_Img_List[i])))
	pic_number=len(filepath)

	im=[]
	for path in filepath:
		# print path
		imgs=ImgSingle.objects(id=str(path))
		tmpim = Image.open(StringIO.StringIO(imgs[0].Img.read()))
		w,h = tmpim.size
		h = (width*h)/w
		height+=h
		tmpim = tmpim.resize((width,h))
		im.append(tmpim)

	ret = Image.new('RGBA',(width,height+100*pic_number))
	draw = ImageDraw.Draw(ret)

	for i in range(pic_number):
		ret.paste(im[i],(0,h_pos))
		w,h = im[i].size
		h_pos += h+10
		draw.text((20,h_pos),TextList[i],font=font,fill="#ffffff")
		h_pos += 90
		# print h_pos
	# newTemp = ImgTemp()
	# output=StringIO.StringIO()
	# ret.save(output)
	# newTemp.Img = output
	# newTemp.DateTime = datetime.datetime.now()
	# newTemp.save()

	# filename = uuid.uuid4()
	# filepath = 'static/temp/'+str(filename)+'.jpg'
	# ret.save(filepath)
	# print type(filepath),filepath
	imagefile = StringIO.StringIO()
	ret.save(imagefile,format='JPEG')

	newTemp = ImgTemp()
	newTemp.Img = imagefile.getvalue()
	newTemp.DateTime = datetime.datetime.now()

	newTemp.save()
	# os.remove(filepath)
	return newTemp.id
