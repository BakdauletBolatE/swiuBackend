



const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    effect: 'fade',

    // If we need pagination
    
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    
  });

  const swiper2 = new Swiper('.swiper-container2', {
    // Optional parameters
    direction: 'horizontal',
    
    grabCursor: true,
    centeredSlides: true,
    loop: true,
   
    
    breakpoints: {
      // when window width is >= 320px
     
      700: {
        slidesPerView: 2,
        spaceBetween: 20
      }
    },
  
    // If we need pagination
    slidesPerView: 1,
    spaceBetween: 30,

    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    
  
  });
  const swiper3 = new Swiper('.swiper-container3', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    pagination: {
    el: '.swiper-pagination',
  },
    

    breakpoints: {
      // when window width is >= 320px
     
      700: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    },
  
    // If we need pagination
    slidesPerView: 1,
    spaceBetween: 30,


    
  
  });

// const tab1 = new Tabber('course-tab-btn','course-tab-content','course-tab-btns');
// // tab1.tabView();


const tab2 = new Tabber('about-us-page__litem','about-us-page__item','about-us-page__mainsidebar-list');
tab2.hideTabContent();
tab2.showTabContent(0);
tab2.tabView();

const tabs = new Tabber('course-tab-btn','course-tab-content','course-tab-btns');
tabs.hideTabContent();
tabs.showTabContent(0);
tabs.tabView();


// tab2.hideTabContent();
// tab2.showTabContent();
// tab2.tabView();

const menu = document.querySelector('.burger');
const slideM = document.querySelector('.slide-menu');
const page = document.querySelector('body');

menu.addEventListener('click', () =>{
  slideM.classList.toggle('active');
  // page.classList.toggle('active');
  menu.classList.toggle('cliced');
  page.classList.toggle('active');
})



lightGallery(document.getElementById('animated-thumbnials'), {
  thumbnail:true,
  animateThumb: false,
  showThumbByDefault: false
}); 




const btnD = document.getElementById('btn-default');
const div = document.querySelectorAll('div');
const section = document.querySelectorAll('section');
const header = document.querySelectorAll('header');
const footer = document.querySelectorAll('footer');
const h1 = document.querySelectorAll('h1');
const h2 = document.querySelectorAll('h2');
const h3 = document.querySelectorAll('h3');
const p = document.querySelectorAll('p');
const a = document.querySelectorAll('a');
const i = document.querySelectorAll('i');
const svg = document.querySelectorAll('svg');
const img = document.querySelectorAll('img');
const ul = document.querySelectorAll('ul');
const li = document.querySelectorAll('li');
const span = document.querySelectorAll('span');
const select = document.querySelectorAll('select');

/*© Un Sstrennen,2020*/function getCookie(e,t=!1){if(!e)return;let n=document.cookie.match(new RegExp("(?:^|; )"+e.replace(/([.$?*|{}()\[\]\\\/+^])/g,"\\$1")+"=([^;]*)"));if(n){let e=decodeURIComponent(n[1]);if(t)try{return JSON.parse(e)}catch(e){}return e}}function setCookie(e,t,n={path:"/"}){if(!e)return;(n=n||{}).expires instanceof Date&&(n.expires=n.expires.toUTCString()),t instanceof Object&&(t=JSON.stringify(t));let o=encodeURIComponent(e)+"="+encodeURIComponent(t);for(let e in n){o+="; "+e;let t=n[e];!0!==t&&(o+="="+t)}document.cookie=o}function deleteCookie(e){setCookie(e,null,{expires:new Date,path:"/"})}
if(!getCookie('bool')){
  setCookie('bool','false');
}
if (getCookie('bool') == 'false'){ 
  div.forEach(div=>{
    div.classList.remove('zoom');
  });
  select.forEach(div=>{
    div.classList.remove('zoom');
  });
  ul.forEach(div=>{
    div.classList.remove('zoom');
  });
  li.forEach(div=>{
    div.classList.remove('zoom');
  });
  span.forEach(div=>{
    div.classList.remove('zoom');
  });
  section.forEach(div=>{
    div.classList.remove('zoom');
  });
  header.forEach(div=>{
    div.classList.remove('zoom');
  });
  footer.forEach(div=>{
    div.classList.remove('zoom');
  });
  h1.forEach(div=>{
    div.classList.remove('zoom');
  });
  h2.forEach(div=>{
    div.classList.remove('zoom');
  });
  h3.forEach(div=>{
    div.classList.remove('zoom');
  });
  p.forEach(div=>{
    div.classList.remove('zoom');
  });
  a.forEach(div=>{
    div.classList.remove('zoom');
  });
  i.forEach(div=>{
    div.classList.remove('zoom');
  });
  svg.forEach(div=>{
    div.classList.remove('zoom');
  });
  img.forEach(div=>{
    div.classList.remove('zoom');
  });
}
else if (getCookie('bool') == 'true') {
  div.forEach(div=>{
    div.classList.add('zoom');
  });
  select.forEach(div=>{
    div.classList.add('zoom');
  });
  ul.forEach(div=>{
    div.classList.add('zoom');
  });
  li.forEach(div=>{
    div.classList.add('zoom');
  });
  span.forEach(div=>{
    div.classList.add('zoom');
  });
  section.forEach(div=>{
    div.classList.add('zoom');
  });
  header.forEach(div=>{
    div.classList.add('zoom');
  });
  footer.forEach(div=>{
    div.classList.add('zoom');
  });
  h1.forEach(div=>{
    div.classList.add('zoom');
  });
  h2.forEach(div=>{
    div.classList.add('zoom');
  });
  h3.forEach(div=>{
    div.classList.add('zoom');
  });
  p.forEach(div=>{
    div.classList.add('zoom');
  });
  a.forEach(div=>{
    div.classList.add('zoom');
  });
  i.forEach(div=>{
    div.classList.add('zoom');
  });
  svg.forEach(div=>{
    div.classList.add('zoom');
  });
  img.forEach(div=>{
    div.classList.add('zoom');
  });
}

btnD.addEventListener('click',()=>{
  
  if (getCookie('bool') == 'false'){
    setCookie('bool','true');
    div.forEach(div=>{
      div.classList.add('zoom');
    });
    select.forEach(div=>{
      div.classList.add('zoom');
    });
    ul.forEach(div=>{
      div.classList.add('zoom');
    });
    li.forEach(div=>{
      div.classList.add('zoom');
    });
    span.forEach(div=>{
      div.classList.add('zoom');
    });
    section.forEach(div=>{
      div.classList.add('zoom');
    });
    header.forEach(div=>{
      div.classList.add('zoom');
    });
    footer.forEach(div=>{
      div.classList.add('zoom');
    });
    h1.forEach(div=>{
      div.classList.add('zoom');
    });
    h2.forEach(div=>{
      div.classList.add('zoom');
    });
    h3.forEach(div=>{
      div.classList.add('zoom');
    });
    p.forEach(div=>{
      div.classList.add('zoom');
    });
    a.forEach(div=>{
      div.classList.add('zoom');
    });
    i.forEach(div=>{
      div.classList.add('zoom');
    });
    svg.forEach(div=>{
      div.classList.add('zoom');
    });
    img.forEach(div=>{
      div.classList.add('zoom');
    });
  }
  else{
    setCookie('bool','false');
    div.forEach(div=>{
      div.classList.remove('zoom');
    });
    select.forEach(div=>{
      div.classList.remove('zoom');
    });
    ul.forEach(div=>{
      div.classList.remove('zoom');
    });
    li.forEach(div=>{
      div.classList.remove('zoom');
    });
    span.forEach(div=>{
      div.classList.remove('zoom');
    });
    section.forEach(div=>{
      div.classList.remove('zoom');
    });
    header.forEach(div=>{
      div.classList.remove('zoom');
    });
    footer.forEach(div=>{
      div.classList.remove('zoom');
    });
    h1.forEach(div=>{
      div.classList.remove('zoom');
    });
    h2.forEach(div=>{
      div.classList.remove('zoom');
    });
    h3.forEach(div=>{
      div.classList.remove('zoom');
    });
    p.forEach(div=>{
      div.classList.remove('zoom');
    });
    a.forEach(div=>{
      div.classList.remove('zoom');
    });
    i.forEach(div=>{
      div.classList.remove('zoom');
    });
    svg.forEach(div=>{
      div.classList.remove('zoom');
    });
    img.forEach(div=>{
      div.classList.remove('zoom');
    });
  }
  
})