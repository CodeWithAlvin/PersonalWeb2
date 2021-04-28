let nav=document.getElementsByTagName("nav");
let burger=document.getElementById("Layer_1");
let messages=document.getElementById("messages")
let close= document.getElementById("close")

burger.addEventListener("click",()=>{
    nav[0].classList.toggle("showlink");
});

close.addEventListener("click",()=>{
	messages.style.display="none";
})

