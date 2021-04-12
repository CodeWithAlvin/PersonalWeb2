let nav=document.getElementsByTagName("nav");
let burger=document.getElementById("Layer_1");

burger.addEventListener("click",()=>{
    nav[0].classList.toggle("showlink");
});