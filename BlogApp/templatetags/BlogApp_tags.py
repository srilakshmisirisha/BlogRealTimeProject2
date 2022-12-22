from django import template
from BlogApp.models import Post
register = template.Library()
from django.db.models import Count

#@register.simple_tag
@register.simple_tag(name='my_tag')

def total_posts():
    return Post.objects.count()

@register.inclusion_tag('BlogApp/latest_posts.html')
def show_latestposts(count=5):
    latestposts = Post.objects.order_by('-publish')[:count]
    return {'latestposts':latestposts}

#@register.assignment_tag
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]