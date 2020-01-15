from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from main.models import Schedule
from .forms import PostForm

# 모든 게시물을 표시
def tables(request):
    posts = Post.objects.all()
    return render(request, 'post/tables.html', {'posts' : posts})

# 게시물 작성
# 게시물을 작성할 때마다 Post테이블과 Schedule테이블에 데이터가 생성됨
@login_required
def table_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            Schedule.objects.create(user=request.user, post=post, postID=post.id, title=post.title, time=post.time)
            messages.info(request, "글을 등록하였습니다.")
            return redirect('post:tables')
    else:
        form = PostForm()
    return render(request, 'post/tables.html', {
        'form' : form,
    })

# 게시물 자세히 보기
# joins - 모임에 참여한 유저들

def table_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    joins = Schedule.objects.filter(postID=pk)
    count = joins.count()
    return render(request, 'post/table_detail.html', {
        'posts' : posts, 
        'count':count, 
        'joins':joins
    })

# 참여하기
# 할 때마다, Schedule테이블에 데이터가 생성됨
@login_required
def join(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
#       count - 현재 참여한 인원 수
        count = Schedule.objects.filter(postID=pk).count()
#       현재 인원 수가 최대 인원 수 이상일 경우, 더 이상 참여가 불가능함
        if count >= post.max_count:
            messages.info(request, "정원이 다 차서 참여가 실패하였습니다.")
            return redirect('post:tables')
        else:
            Schedule.objects.create(user=request.user, post=post, postID=pk, title=post.title, time=post.time)
            messages.info(request, "참여에 성공하였습니다.")
            return redirect('post:tables')

# 탈퇴하기
# Schedule테이블에 데이터가 삭제됨
@login_required        
def unjoin(request, pk):
    if request.method == 'POST':
        schedule = Schedule.objects.filter(postID=pk)
#       Schedule테이블에 탈퇴를 요청하는 유저의 정보가 존재한다면 탈퇴하기 수행
        if schedule.filter(user=request.user).exists():
            schedule.filter(user=request.user).delete()
            messages.info(request, "탈퇴완료")
            return redirect('post:tables')
        else:
            messages.info(request, "잘못된 접근")
            return redirect('post:tables')
        