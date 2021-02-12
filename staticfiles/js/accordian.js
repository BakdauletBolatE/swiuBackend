const acc = document.querySelectorAll('.accordion__title');

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