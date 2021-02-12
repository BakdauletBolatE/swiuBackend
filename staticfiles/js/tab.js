
class Tabber{
    constructor(tabs,tabsContent,tabsParent) {
        this.tabs = document.querySelectorAll('.'+tabs);
        this.tabsContent = document.querySelectorAll('.'+tabsContent);
        this.tabsParent = document.querySelector('.'+tabsParent);
        this.tabsName = tabs;
    }
    


    hideTabContent() {
        this.tabsContent.forEach(item =>{
            item.style.display = "none";
        })
        // this.tabsContent.forEach(item => {
        //     item.style.display = "none";
        // });

        this.tabs.forEach(item =>{
            item.classList.remove(this.tabsName+'--active');
        });
    }

    showTabContent(i) {
        if(this.tabsContent[i] == null){

        }
        else{
            this.tabsContent[i].style.display = 'block';
            this.tabs[i].classList.add(this.tabsName+'--active');
        }
        
    }

    tabView() {
        if (this.tabsParent == null){

        }
        else{
            this.tabsParent.addEventListener('click',(event)=>{
                const target = event.target;
                
                if (target && target.classList.contains(this.tabsName)){
                    
                    this.tabs.forEach((item,i)=>{
                        if (target == item){   
                            this.hideTabContent();
                            this.showTabContent(i);
                        }
                    });
                }
            });
        }
        
    }

}


