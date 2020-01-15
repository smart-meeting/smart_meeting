from django.db import models
from django.conf import settings

# 게시물의 데이터
# 제목, 작성자, 모이는 시간, 모임 유형, 모이는 장소, 상세 내용, 최소 인원 수, 최대 인운 수, 생성 시간, 수정 시간
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateField()
    type_choice = (
        ('술팟', '술팟'),
        ('게임팟', '게임팟'),      
        ('운동팟', '운동팟'),
        ('기타', '기타')
    )
    type_meet = models.CharField(max_length=10, choices=type_choice, default='술팟')
    place = models.CharField(max_length=50)
    content = models.CharField(max_length=200, help_text="최소 10자 입력 가능합니다.")
    min_count = models.IntegerField(default=2)
    max_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # created_at 기준으로 정렬
    class Meta:
        ordering = ['created_at']
    

    