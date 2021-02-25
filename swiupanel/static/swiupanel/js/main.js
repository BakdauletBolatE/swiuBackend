const search = document.getElementById('searchEdu');
const tableS = document.getElementById('tableSearch');
const tableAll = document.getElementById('tableAll');
if (search){
    search.addEventListener('change',e=>{
        const item = e.target.value;
        
        fetch('searchedu/'+item)
        .then(response => response.json())
        .then(result => {
            const tbody = document.createElement('tbody');
            tableS.appendChild(tbody);
            tableAll.style.display = "none";
            result.data.map(item=>{
                const tr = document.createElement('tr');
                const tdId = document.createElement('td');
                const tdName = document.createElement('td');
                tdId.textContent = item.id;
                tdName.textContent = item.name;
                tr.appendChild(tdId);
                tr.appendChild(tdName);
                tbody.appendChild(tr);
            });
            
        })
    });
}


const idName = document.getElementById('id_name_en');
const idTitle = document.getElementById('id_title_en');
let slug = document.getElementById('id_slug');

if (idName){
    idName.addEventListener('input',item=>{
        let string = item.target.value;
        let new_str = "";
        for (i=0;i<string.length;i++){
            if (string[i] == " "){
                new_str += "-";
            }
            else{
                new_str += string[i].toLowerCase();
            }
        }
        slug.value = new_str;
        
        
    })
}
if (idTitle){
    idTitle.addEventListener('input',item=>{
        let string = item.target.value;
        let new_str = "";
        for (i=0;i<string.length;i++){
            if (string[i] == " "){
                new_str += "-";
            }
            else{
                new_str += string[i].toLowerCase();
            }
        }
        slug.value = new_str;
        
        
    })
}
