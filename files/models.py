import os
from django.db import models
from django.contrib.auth.models import User
from ui import utils

def get_upload_file_name(instance, filename):
	return os.path.join('{} - {}'.format(instance.blueprint.user_id,
	 	instance.blueprint.user.username),
		instance.blueprint.name,
		'templates',
		filename)

class Blueprint(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now=True)

class Document(models.Model):
	blueprint = models.ForeignKey(Blueprint)
	name = models.CharField(max_length=30)
	extension = models.CharField(max_length=5)
	doc_file = models.FileField(upload_to=get_upload_file_name)
	date_created = models.DateTimeField(auto_now=True)

class Trigger(models.Model):
	blueprint = models.ForeignKey(Blueprint)
	name = models.CharField(max_length=30, default='default name')
	date_created = models.DateTimeField(auto_now=True)

class Condition(models.Model):
	trigger = models.ForeignKey(Trigger)
	date_created = models.DateTimeField(auto_now=True)

class Action(models.Model):
	trigger = models.ForeignKey(Trigger)
	date_created = models.DateTimeField(auto_now=True)

class Variable(models.Model):
	document = models.ForeignKey(Document)

