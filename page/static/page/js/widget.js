let widgetitems = widgetgroup.querySelectorAll('.widget--item');
let editBtn = widgetgroup.querySelectorAll('.widget--item-editable');


async function UpdateWidget(data,url){
    let dataUpdate = await fetch(url,{
        method:"POST",
        headers: {
                   "Content-type": 'application/json; charset=utf-8',
                   "X-CSRFToken": csrfToken.value
       },
       body: JSON.stringify(data)
    })
}

editBtn.forEach(btn=>{
    btn.addEventListener('click',function(){
        hideWidgetItems();
        elem = this.parentElement;
        type = elem.querySelector('[name="type"]').value;
        id = elem.querySelector('.widget--id');
        title = elem.querySelector('[data-widget="title"]');
        desc = elem.querySelector('[data-widget="description"]');

        if (type == "widgettext"){
            let data = {
                'type': type,
                'title':title ? title.innerHTML : "",
                'description':desc ? desc.innerHTML : "",
            }
            console.log(data);
            return UpdateWidget(data,`/page-const/widget-text-update/${id.value}`);
        }
        if (type == "widgetonlytext"){
            let data = {
                'type': type,
                'description':desc ? desc.innerHTML : "",
            }
            return UpdateWidget(data,`/page-const/widget-text-update/${id.value}`);
        }
        if (type == "widgetphoto"){
            let data = {
                'type': type,
                'title':title ? title.innerHTML : "",
                'description':desc ? desc.innerHTML : "",
            }
            return UpdateWidget(data,`/page-const/widget-text-update/${id.value}`);
        }
        
        
    })
})


function hideWidgetItems(){
    widgetitems.forEach(elem=>{
        let btnHide = elem.querySelector('.widget--item-editable');
        btnHide.classList.remove('active');
        let titleHide = elem.querySelector('.widgetwihttext__title');
        if (titleHide){
            titleHide.setAttribute('contenteditable','false');
        }

        let descHide = elem.querySelector('.widgetwihttext__description');
        if (descHide){
            descHide.setAttribute('contenteditable','false');
        }

        let descFotoHide = elem.querySelector('.widgetwithphoto__description');
        if (descFotoHide){
            descFotoHide.setAttribute('contenteditable','false');
        }
    })
}


widgetitems.forEach(widget=>{
    widget.addEventListener('click',function(){
        
        if (this.classList.contains('widget--item')){
            elem = this;

            let btn = elem.querySelector('.widget--item-editable');
            btn.classList.add('active');
            let title = elem.querySelector('.widgetwihttext__title');
            if (title){
                title.setAttribute('contenteditable','true');
            }

            let desc = elem.querySelector('.widgetwihttext__description');
            if (desc){
                desc.setAttribute('contenteditable','true');
            }

            let descFoto = elem.querySelector('.widgetwithphoto__description');
            if (descFoto){
                descFoto.setAttribute('contenteditable','true');
            }
            }
    })
})