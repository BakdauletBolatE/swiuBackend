const widgetContainer = document.getElementById('widgets'),
      widgetBtn = document.getElementById('sidebar__btn'),
      widgets = document.querySelectorAll('.widget-form'),
      widgetsSelectBtn = document.querySelectorAll('.widget__item'),
      csrfToken = document.getElementById('csrf_token');

      

let widgetgroup = document.getElementById('realpage');

function UpdateDataOrder(list,listClass){
    let widgetgrouparray = []
    items = list.querySelectorAll('.'+listClass);
    items.forEach((item,i)=>{
        widgetgrouparray.push(
            {
                "pk":item.getAttribute('data-pk'),
                "order":i
            }
        )
    })

    return widgetgrouparray
}


async function FetchToUpdate(data,url){
    let liked = await fetch(url,{
       method:"POST",
       headers: {
                   "Content-type": 'application/json; charset=utf-8',
                   "X-CSRFToken": csrfToken.value
       },
       body: JSON.stringify(data)
   })
   return await liked
}

if (widgetgroup){
    let sortable = new Sortable(widgetgroup, {
        animation: 150,
        onUpdate: function (evt) {
            let data = UpdateDataOrder(widgetgroup,'widget--item');
            console.log(data);
            FetchToUpdate(data,'/page-const/ordered-widgets/');
        },
        
    });
}



let pagegroup = document.getElementById('page-group');

if (pagegroup){
    let sortable2 = new Sortable(pagegroup, {
        animation: 150,
        handle:'.pagelist__icon',
        dragClass: "pagelist__item-drag",
        chosenClass: "pagelist__item-chosen",
        onUpdate: function (evt) {
            let data = UpdateDataOrder(pagegroup,'pagelist__item');
            FetchToUpdate(data,'/page-const/ordered-pages/');
        },
    });
}






// function initWidgets(){
//     widgets = document.querySelectorAll('.widget');
//     widgetsSelectBtn = document.querySelectorAll('.widgets-group__item');
// }


function hideAllWidgets(){
    widgets.forEach(widget=>{
        widget.classList.add('hide');
    });
}

function visibleWidget(num){
    widgets[num].classList.remove('hide');
}

hideAllWidgets();

widgetsSelectBtn.forEach((widgetBtn,i)=>{
    widgetBtn.addEventListener('click',()=>{
        hideAllWidgets();
        visibleWidget(i);
    })
})



if (widgetBtn){
    widgetBtn.addEventListener('click',()=>{
        hideAllWidgets();
        widgetContainer.classList.toggle('active');
    })
}
