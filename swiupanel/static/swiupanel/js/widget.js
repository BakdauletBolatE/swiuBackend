const btnSW = document.getElementById('btnSW');
const selectWidgetType = document.getElementById('selectWidgetType');
const idPage = document.getElementById('pageID');
const csrfTokenBody = document.getElementById('csrfToken');
const row = document.getElementById('row');
csrfToken = csrfTokenBody.value;
const cardbody = document.querySelectorAll('.image_row');

btnSW.addEventListener('click',e=>{
    widgetType = selectWidgetType.value;
    url = '/swiu-panel/widgettype/add/';
    id = idPage.value;
    widgetTypeData = {
        'id': id,
        'widgetType': widgetType
    }
    fetch(url,{
        method:"POST",
        headers: {
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(widgetTypeData)
    })
    .then(function (data) {
        console.log('Request succeeded with JSON response', data);
        })
    .then(view)
    .catch(function (error) {
        console.log('Request failed', error);
    });

    function view(){
        container = document.createElement('div');
        
        fetch('/swiu-panel/getjson-widget/')
        .then(response => response.json())
        .then(widgets => {
            widgets.widget.map(widget=>{
               
                if (widget.widget_type_id == 1){
                    container.innerHTML = `
                    <form enctype="multipart/form-data" class="addWidgetItemForm" method="POST" action="">
                    <div class="col-12">
                                   Галерея
<p><label for="id_widget_photo">Фото для виджета:</label> <input type="file" name="widget_photo" accept="image/*" id="id_widget_photo"></p>
<p><input type="text" name="widget" value="${widget.id}" id="id_widget"></p>
<button class="clickToadd" >Создать</button>                                   
                               </div>
                               </form>
                               `
                             
                               ;
                               row.appendChild(container);
                }
                else if (widget.widget_type_id == 2)
                {
                    container.innerHTML = `
                    <div class="col-12">
                                   Артикл Блок
                                   <form enctype="multipart/form-data" class="addWidgetItemForm"  action="" method="POST">
                                   <p><label for="id_title">Загаловок виджета:</label> <input type="text" name="title" maxlength="255" id="id_title"></p>
<p><label for="id_widget_photo">Фото для виджета:</label> <input type="file" name="widget_photo" accept="image/*" id="id_widget_photo"></p>
<p><input type="hidden" name="widget" value="${widget.id}" id="id_widget"></p>
<button class="clickToadd">Создать</button>                                   
                               </div>`;

                row.appendChild(container);
                }
                row.appendChild(container);
                
            })
        })
    }

    
})
row.addEventListener('click',item=>{
        if (item.target.classList.contains('clickToadd')){
            btn = item.target;
            form = btn.parentElement.parentElement;
            form.addEventListener('submit',e=>{
                e.preventDefault();
                target = e.target;
                widgetItemData = new FormData(target);
                console.log(widgetItemData);
                
                fetch('/swiu-panel/widgetitem/add',{
                method:"POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: widgetItemData
                })
                .then(function (data) {
                    console.log('Request succeeded with JSON response', data);
                    })
                .catch(function (error) {
                    console.log('Request failed', error);
                });
            })
        }
        else{
            console.log(item.target);
        }
        
        // if (item.target.classList.contains('clickToadd')){
        //     console.log(item.target)
            // addWidgetItemForm = item.target;
            // console.log(addWidgetItemForm);
            // addWidgetItemForm.preventDefault();
            // addWidgetItemForm.addEventListener('submit',e=>{
            //     e.target.preventDefault();
            //     console.log(e);
                // target = e.target;
                
        //     })
        // }
        // else{
        //     console.log(item.target);
        // }
    });





