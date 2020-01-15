from django.db import models
from django.conf import settings
from post.models import Post

# 달력의 데이터
# 사용자, 게시물, 게시물ID, 모임제목, 모임 시간
# 사용자 계정이 삭제되거나 참여한 Post가 삭제된 경우, 해당하는 Schedule데이터도 삭제됨
# postID는 게시물에 참여하기와 탈퇴하기를 진행하기 위해 존재함
class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=0)
    postID = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    time = models.DateField()