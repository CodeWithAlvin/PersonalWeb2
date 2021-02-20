function ToggleNav(){ 
	let menu=document.getElementById("menu");
	let nav=document.getElementById("navbar");
	
	if (nav.style.display==""){
		nav.style.display="flex";
	}
	else{
		nav.style.display="";
	}
	
	menu.classList.toggle('opened');
	menu.setAttribute('aria-expanded', menu.classList.contains('opened'));
}