from mongoengine import *
import os
import ImageFont
import Image
import ImageDraw

connect('picture')

# class Picture(Document):
# 	Pic_File = FileField()
# 	Pic_Tag = ListField()

class Group(Document):
	Group_File_List = ListField()
	Group_Name = StringField(max_length = 50, default = '')

# newGroup = Group()
# newGroup.Group_File_List.append('1.jpg')
# newGroup.Group_File_List.append('2.jpg')
# newGroup.Group_File_List.append('3.jpg')
# newGroup.Group_File_List.append('4.jpg')
# newGroup.Group_Name = "baidu"
# newGroup.save()

# newGroup = Group.objects()
# for i in newGroup:
# 	print i.delete()

# newGroup = Group.objects()
# for i in newGroup:
# 	print i.Group_File_List

def ImgHandler(filepath,TextList):
	FontFolder = 'static/Font'
	font = ImageFont.truetype(FontFolder + "/simsun.ttc",34)
	width = 400
	height=0
	h_pos = 0
	pic_number=len(filepath)

	im=[]
	for path in filepath:
		tmpim = Image.open(path)
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
	return ret
