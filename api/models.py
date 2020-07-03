from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

import datetime

# get the user model
User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=250)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TrackableItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    available_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=14)))
    estimated_time = models.IntegerField(default=8)
    trackable_items = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    Type = (("assigment", "Assigment"),
            ("sub-assignment", "Sub Assigment"),
            ("oh", "Office Hours"),
            ("video", "Video"),
            )
    ti_type = models.CharField(max_length=20, choices=Type, default="assigment")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class QRCode(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trackable_item = models.ForeignKey(TrackableItem, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.title + " " + self.trackable_item.title


class TimeRecord(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trackable_items = models.ForeignKey(TrackableItem, on_delete=models.CASCADE)
    started = models.DateTimeField()
    ended = models.DateTimeField()
    duration = models.DecimalField(max_digits=8, decimal_places=2)
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user + " : " + self.started


class CourseUser(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CharField)
    ROLE = (
        ('student', 'Student'),
        ('ta', 'Teaching Assistance'),
        ('co-instructor', 'Co Instructor'),
    )
    role = models.CharField(max_length=50, choices=ROLE, default='student')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
