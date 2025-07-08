from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from datetime import date


class BlogPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    template = 'a_blog/blog_page.html'

    def get_context(self, request):
        tag = request.GET.get('tag')
        if tag:
            articles = ArticlePage.objects.filter(tags__name=tag).live().order_by('-first_published_at')
        else:
            articles = self.get_children().live().order_by('-first_published_at')
        context = super().get_context(request)
        context['articles'] = articles
        context['tag'] = tag
        return context

class ArticlePage(Page):
    intro = models.CharField(max_length=80)
    body = RichTextField(blank=True)
    date = models.DateField("Post date", default=date.today)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=80, blank=True)
    tags = ClusterTaggableManager(through='ArticleTag', blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('tags'),
    ]

class ArticleTag(TaggedItemBase):
    content_object = ParentalKey('ArticlePage', related_name='tagged_items', on_delete=models.CASCADE)