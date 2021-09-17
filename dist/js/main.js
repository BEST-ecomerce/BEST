const bars = document.getElementById("bars");
const navbar = document.getElementById("navbar");

bars.addEventListener('click', ()=>{
    if(navbar.classList.contains("hidden")){
        navbar.classList.remove('hidden');
        navbar.classList.add('block');
    }else{
        navbar.classList.remove('block');
        navbar.classList.add('hidden')
    }
});

