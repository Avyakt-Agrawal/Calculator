var list = document.querySelector('#movie-list ul  '); 

 list.addEventListener('click', function(e){
   if(e.target.className === 'delete'){          // We want to get where did the click happened, so className
     //console.log(e.target);
     var li = e.target.parentElement;         // this is the li which is the parent to the delete and we want to delete it.
     //console.log(li);
     //li.parentNode.removeChild(li);
     list.removeChild(li);

   }
 })