from django.contrib import admin
from files.models import Blueprint, Document, Trigger, Condition, Action, Variable

admin.site.register(Blueprint)
admin.site.register(Document)
admin.site.register(Trigger)
admin.site.register(Condition)
admin.site.register(Action)
admin.site.register(Variable)