from django import template

register = template.Library()


@register.filter
def inject_adsense_after_paragraph(content, ad_code):
    paragraphs = content.split("</p>")
    result = ""
    ad_inserted = False

    for index, paragraph in enumerate(paragraphs):
        if index == 2 and not ad_inserted:
            result += f"{paragraph}</p>{ad_code}"
            ad_inserted = True
        else:
            result += f"{paragraph}</p>"

    return result
