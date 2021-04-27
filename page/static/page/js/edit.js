const textArea = document.getElementById('widget-textarea'),
      btns = document.querySelectorAll('.toolbar__btn');


      btns.forEach(btn=>{
          btn.addEventListener('click',(e)=>{
              console.log(btn);
              let cmd = e.target.dataset['command'];
              document.execCommand(cmd,false,null);
          })
      })