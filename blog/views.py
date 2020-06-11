from django.shortcuts import render, redirect, get_object_or_404
from .models import Post #model에 있는 Post 객체 가져오기
from .forms import PostForm

# Create your views here.

def main(request):
    posts = Post.objects.order_by('-date') #Post.objects를 posts 변수에 담기, 최신순 정렬
    return render(request, 'posts.html', {'posts':posts}) #인자 3개 : request, templates, context

def create(request):
    if request.method=='POST': #POST vs GET 분기
        form=PostForm( request.POST ) #form 변수에 PostForm 할당
        if form.is_valid(): #유효성 검증 통과한다면
            form.save #저장하고
            return redirect('main') #main 페이지로 가기 
    else:
        form=PostForm() # 빈 form 열기'
    print(Post.objects.all())
    return render(request, 'create.html', {'form':form})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #해당 객체가 있으면 가져오고 없으면 404 에러 pk로 pk 사용
    return render(request, 'detail.html', {'post':post})     

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST' :
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post) #post 객체 가져와서 form 생성
        return render(request, 'update.html', {'form':form})
        
def delete(request, pk):
    post = Post.objects.get(pk=pk) 
    post.delete() #delete 함수 실행
    return redirect ('main')


