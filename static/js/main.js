



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
    effect: 'coverflow',
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    
    grabCursor: true,
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

    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    
  
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
const page = document.querySelector('.page');

menu.addEventListener('click', () =>{
  slideM.classList.toggle('active');
  // page.classList.toggle('active');
  menu.classList.toggle('cliced');
})





