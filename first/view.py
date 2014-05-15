#coding:utf8
import os
from util import APIBaseHandler
from .model import ImgGroup
from .model import ImgHandler
from .model import ImgSingle
import uuid
import json
import Image
class APIFirstHandler(APIBaseHandler):
	def get(self):
		# self.write("123")
		newGroup = ImgGroup.objects()
		filepath = []
		gn=0
		for i in range(len(newGroup[gn].Group_Img_List)):
			filepath.append("/api/img/"+str(newGroup[gn].Group_Img_List[i]))
		# print filepath
		self.render("FirstGet.html",filepath=filepath)
	# def post(self):
	# 	newGroup = Group.objects()
	# 	filepath = []
	# 	gn=0
	# 	for i in range(len(newGroup[gn].Group_Img_List)):
	# 		filepath.append(("static/Img/"+newGroup[gn].Group_Img_List[i]))
	# 	words = self.get_arguments("words")
	# 	ret = ImgHandler(filepath,words)

	# 	filename = uuid.uuid4()
	# 	filepath = 'static/temp/'+str(filename)+'.jpg'
	# 	ret.save(filepath)
	# 	self.render("FirstPost.html",filepath=filepath)

class APIFirstNextGroup(APIBaseHandler):
	def get(self):
		newGroup = ImgGroup.objects()
		filepath=[]
		gnum = int(self.get_arguments("group")[0])
		for i in range(len(newGroup[gnum].Group_Img_List)):
			filepath.append("/api/img/"+str(newGroup[gnum].Group_Img_List[i]))
		# print filepath
		result = json.dumps(filepath)
		self.write(result)

class APIFirstResult(APIBaseHandler):
	def post(self):
		restGroup = ImgGroup.objects()
		filepath=[]
		# print len(self.get_arguments("group"))
		gnum = int(self.get_arguments("group")[0])
		for i in range(len(restGroup[gnum].Group_Img_List)):
			filepath.append((str(restGroup[gnum].Group_Img_List[i])))
		words = self.get_arguments("words")[0]
		# print type(words)
		# print words
		words = json.loads(words)

		ret = ImgHandler(filepath,words)

		filename = uuid.uuid4()
		filepath = 'static/temp/'+str(filename)+'.jpg'
		ret.save(filepath)
		filepath = json.dumps(filepath)
		self.write(filepath)
class APIFirstGroupNum(APIBaseHandler):
	def get(self):
		restGroup = ImgGroup.objects()
		# print len(restGroup)
		self.write(str(len(restGroup)))

class APIGetImg(APIBaseHandler):
	def get(self,img_id):
		imgs=ImgSingle.objects(id=str(img_id))
		# imgs[0].Img.read().show()
		# Image.open(StringIO.StringIO(imgs[0].Img.read())).show()
		self.write(imgs[0].Img.read())
