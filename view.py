#coding:utf8
import os
from util import APIBaseHandler
from first.model import ImgSingle
from first.model import ImgGroup


class APIGetImg(APIBaseHandler):
	def get(self,img_id):
		try:
			imgs=ImgSingle.objects(id=img_id)
			self.write(imgs.first().Img.read())
