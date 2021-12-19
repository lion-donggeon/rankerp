from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q

from django.utils import timezone


import logging
logger = logging.getLogger('main')



def index(request):

    logger.info("INFO 레벨로 출력")


    """
    main 목록 출력
    """
    #현재 날짜
    today = timezone.now()

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Question.objects.order_by('-create_date')
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

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'today': today}
    return render(request, 'main/question_list.html', context)

def detail(request, question_id):
    """
    main 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'main/question_detail.html', context)