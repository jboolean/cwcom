from django import template
register = template.Library()


# Roughly based on https://medium.com/hceverything/applying-srcset-choosing-the-right-sizes-for-responsive-images-at-different-breakpoints-a0433450a4a3
# And the widths of the thumbnail images
WIDTHS = [350, 700, 1366, 1600, 1920]

@register.filter
def srcset(file):
    url = file.url
    return ', '.join(list(map(lambda w: '%s?width=%d %dw' % (url, w, w), WIDTHS)) + [url+'?width=full'])
