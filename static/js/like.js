"use strict";
const lCode = document.getElementById('lCode'),
    urlSite = `http://swiu.online/${lCode.value}`,
    acc = document.querySelectorAll('.accordion__title');

acc.forEach(event=>{
    event.addEventListener('click',event=>{
        const target = event.target;
        if (target.classList.contains('accordion__title')){
            const newEl = target.nextElementSibling;
            if (newEl.classList.contains('active')){
                newEl.classList.remove('active');
            }
            else{
                newEl.classList.add('active');
            }
        }
    })
})

const likeBtn = document.querySelectorAll('.like_btn'),
      csrfToken = document.getElementById('csrfTokenforLike'),
      sessionKey = document.getElementById('sessionKey');


async function liker(data){
     let liked = await fetch(`${urlSite}/creative/posts/like`,{
        method:"POST",
        headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "X-CSRFToken": csrfToken.value
        },
        body: JSON.stringify(data)
        
    })
    return await liked
}



if (likeBtn){
    likeBtn.forEach(like=>{

        like.addEventListener('click',btn=>{
             btn = btn.target;
    
             if (btn.classList.contains('like_btn')){
                 let url = btn.previousElementSibling.value;
                 let likeCount = btn.nextElementSibling;
                 let myData = {
                    'slug':url,
                    'session_key':sessionKey.value
                 }
                 console.log(myData);
                 liker(myData)
                 .then(render())
    
                 function render(){
                         if (btn.classList.contains('active')){
                             btn.classList.remove('active');
                             likeCount.innerHTML = parseInt(likeCount.innerHTML)-1;
                         }else{
                             btn.classList.add('active');
                             likeCount.innerHTML = parseInt(likeCount.innerHTML)+1;
                         }
                 }
             }
    
        })
    });
}
