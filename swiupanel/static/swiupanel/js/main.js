// const selectCat = document.getElementById('id_staffCat');
// selectCat.setAttribute('class','form-control')
// const containerCat = document.getElementById('containerFacult');
// const containerDepartment = document.getElementById('containerDepartment');
// const containerEduPrograms = document.getElementById('containerEducationalPrograms');
// const stub = document.createElement('option'); 

// selectCat.addEventListener('change',item=>{
//     containerCat.innerHTML = "";
//     containerDepartment.innerHTML = "";
//     containerEduPrograms.innerHTML = "";
//     target = item.target.value;
//     const selectFacult = document.createElement('select');
//     selectFacult.setAttribute('name','facult');
//     selectFacult.setAttribute('id','id_facult');
//     selectFacult.setAttribute('class','form-control');
    
//     getJsonF('../get-facult-json/',target,selectFacult,containerCat);    
//     console.log(selectFacult.children.length);
//     if (selectFacult.lastElementChild){
       
//     }
//     else{
//         console.log("Page false");
//         selectFacult.addEventListener('change',item=>{
//             containerDepartment.innerHTML = "";
//             containerEduPrograms.innerHTML = "";
//             target = item.target.value;
//             const selectDepartment = document.createElement('select');
//             selectDepartment.setAttribute('name','department');
//             selectDepartment.setAttribute('id','id_department');
//             selectDepartment.setAttribute('class','form-control');

//             getJson('../getd/',target,selectDepartment,containerDepartment);

//             selectDepartment.addEventListener('change',item=>{
//                 containerEduPrograms.innerHTML = "";
//                 target = item.target.value;
//                 const selectEdu = document.createElement('select');
//                 selectEdu.setAttribute('name','department');
//                 selectEdu.setAttribute('id','id_department');
//                 selectEdu.setAttribute('class','form-control');

//                 getJson('../get-op-json/',target,selectEdu,containerEduPrograms);
//             })
//         })
//     }
// });
