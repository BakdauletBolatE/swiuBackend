function getJson(url,target,append,container){
    fetch(url+target)
    .then(response => response.json())
    .then(data=>{
        data.data.map(item=>{
            const option = document.createElement('option');
            option.setAttribute('value',item.id);
            option.textContent =  item.name;
            append.appendChild(option);
        })
        if (append){
            container.appendChild(append);
        }
    })
}
// function getJsonF(url,target,append,container){
//     let page = false;
//     return fetch(url+target)  
//     .then(response => response.json())
//     .then(data=>{
//         const hiddsen = document.createElement('option');
//         data.data.map(item=>{
//             const option = document.createElement('option');
//             if (item.name){
//                 option.setAttribute('value',item.id);
//                 option.textContent =  item.name;
//                 hiddsen.setAttribute('value','False');
//                 append.appendChild(option);
//                 page = false;
                
//             }
//             else{
//                 page = true;
//                 option.setAttribute('value',item.id);
//                 option.textContent =  item.title;
//                 hiddsen.setAttribute('value','True');
//                 append.appendChild(option);
//             }
//         })

//         if (append){
//             container.appendChild(append);
//         } 
          
//     });
// }

