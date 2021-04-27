from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def renderWidget(widgetQS):

    widget = widgetQS.content_object

    widgetType = widgetQS.widgettype

    if widgetType == "widgettext":

        if widget.title:
            title = widget.title
        else:
            title = ""

        if widget.description:
            description = widget.description
        else:
            description = ""
        
        

        template = f"""
            <div data-pk='{widgetQS.id}' class="widget--item widgetwihttext">
                <h2 class="widgetwihttext__title">{title}</h2>
                <p class="widgetwihttext__description">{description}</p>
            </div>
        """
        return mark_safe(template)


    elif widgetType == "widgetonlytext":

    
        if widget.description:
            description = widget.description
        else:
            description = ""
        
        

        template = f"""
            <div data-pk='{widgetQS.id}' class="widget--item widgetwihttext">
                            <p class="widgetwihttext__description">{description}</p>
            </div>
        """
        return mark_safe(template)
    elif widgetType == "widgetphoto":
        if widget.title:
            title = widget.title
        else:
            title = ""

        if widget.description:
            description = widget.description
        else:
            description = ""

        if widget.image:
            image = widget.image.url
        else:
            image = ""

        template = f"""
            <div data-pk='{widgetQS.id}' class="widget--item widgetwithphoto">
              
                <p class="widgetwithphoto__description">{description}</p>
                <div class="widgetwithphoto__photo-block">
                    <img class="widgetwithphoto__photo" src="{image}" alt="">
                </div>
            </div>
        """

        return mark_safe(template)

    elif widgetType == "widgetgallery":
        if widget.title:
            title = widget.title
        else:
            title = ""


        if widget.images.all:
            images = widget.images.all()
        else:
            images = ""

        template = f"<div data-pk='{widgetQS.id}' class='widget--item widgetwithgallery'>"  
        for image in images:
            template += f"""
                <div  class="widgetwithphoto__photo-block">
                    <img class="widgetwithphoto__photo" src="{image.image.url}" alt="">
                </div>
            """            
        template += '</div>'

        return mark_safe(template)
        