const addWidget = document.getElementById('addWidget');
const widgetType = document.getElementById('selectWidgetType');
const page = document.getElementById('pageID');
const csrfTokenBody = document.getElementById('csrfToken');

csrfToken = csrfTokenBody.value;

const pageId = page.value;
addWidget.addEventListener('click',(widgetbtn)=>{
    
    const widgetTypeId = widgetType.value;

    addWidgetData = {
        'widgetType':widgetTypeId,
        'pageId': pageId,
        
    }
    console.log(addWidgetData);
    fetch('/swiu-panel/widgettype/add/',{
        method:"POST",
        headers: {
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(addWidgetData)
    })
    .then(function (data) {
        console.log('Request succeeded with JSON response', data);
    })
});