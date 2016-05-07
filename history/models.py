from __future__ import unicode_literals

from django.db import models
import threading
import time
from datetime import datetime


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Counter(threading.Thread):

    __metaclass__ = Singleton

    def __init__(self):
        threading.Thread.__init__(self)
        self.count = 0

    def run(self):
        while True:
            time.sleep(1)
            self.count += 1

counter = Counter()
counter.start()


class Category(models.Model):
    name = models.CharField(max_length=10)

    def master_count(self):
        return self.master_set.count()

    def __unicode__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    year_start = models.IntegerField(null=True, blank=True)
    year_end = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=200, blank=True)
    tag = models.CharField(max_length=500, blank=True)

    def log_count(self):
        return self.log_set.count()

    def status(self):
        if self.log_set.count() > 0:
            if self.log_set.filter(last=True).count() > 0:
                return "Complete"
            else:
                return "In Progress"
        else:
            return "Not Started"

    def is_not_started(self):
        return self.log_set.count() == 0

    def __unicode__(self):
        return self.name


class MasterProxy(Master):
    class Meta:
        proxy = True


class Log(models.Model):
    log_dt = models.DateField()
    episode = models.CharField(max_length=10, blank=True)
    last = models.BooleanField(default=True)
    master = models.ForeignKey(Master)

    def __unicode__(self):
        return "%s@%s" % (self.master, self.log_dt.strftime("%Y-%m-%d"))



