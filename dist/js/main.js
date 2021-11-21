const bars = document.getElementById("bars");
const navbar = document.getElementById("navbar");

bars.addEventListener('click', ()=>{
    if(navbar.classList.contains("hidden")){
        navbar.classList.remove('hidden');
        navbar.classList.add('block');
        bars.classList.remove('far-bars');
        bars.classList.add('fa-times')
    }else{
        navbar.classList.remove('block');
        navbar.classList.add('hidden')
        bars.classList.remove('fa-times');
        bars.classList.add('fa-bars')
    }
});

