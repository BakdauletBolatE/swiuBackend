const search = document.getElementById('searchEdu');
const tableS = document.getElementById('tableSearch');
const tableAll = document.getElementById('tableAll');
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