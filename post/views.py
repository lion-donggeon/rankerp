from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from main.models import Question
from django.db.models import Q

from django.utils import timezone

# Create your views here.

def list(request, category='main'):

    """
    main 목록 출력
    """
    #현재 날짜
    today = timezone.now()

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Question.objects.filter(category=category).order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'today': today, 'category': category}
    return render(request, 'main/question_list.html', context)