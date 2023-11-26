from django.contrib.postgres.search import SearchVector
from django.db import connection
from django.db.models import Q, F, Max, Min, Avg, Case, When, Value,Sum
from django.db.models.functions import Upper


from posts.models import Post

# post = Post.objects.all()
# post = Post.objects.get(id=1)
# post = Post.objects.filter(title__icontains='s')
# post = Post.objects.filter(uniqueId__isnull=True)
# post = Post.objects.filter(id__in=[3, 2])
# post = Post.objects.filter(Q(id=1) | Q(id=3))
# post = Post.objects.filter(Q(id=1) & Q(id=3))
# post = Post.objects.get(id=1)
#
# post.views += 1
#
# post.save()


# post = Post.objects.filter(id=1).update(views=F('views') + 1)
# post = Post.objects.order_by('-pub_date')
# post = Post.objects.count()
# post = Post.objects.distinct()
# post = Post.objects.exclude(title__icontains='s')
# post = Post.objects.values('title', 'slug')
# post = Post.objects.values_list('title', flat=True)
# post = Post.objects.filter(id=1).aggregate(Max('views'), Min('views'), Avg('views'))
# post = Post.objects.aggregate(
#     max=Max('views'),
#     min=Min('views'),
#     avg=Avg('views')
# )

# post = Post.objects.filter(id=2).annotate(title_up=Upper('title'))

# post = Post.objects.annotate(
#     is_trend=Case(
#         When(views__gte=15, then=Value('trend')),
#         When(views__lt=15, then=Value('general')),
#     )
# )

# post = Post.objects.filter(author__username='hesam')


# post = Post.objects.aggregate(views=Sum('views'))

# print(post)
# print("\n")
#
# print(connection.queries)
