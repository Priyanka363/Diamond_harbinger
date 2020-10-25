var nav1 = document.getElementById('navv');

window.onscroll = function() {

  if(window.pageYOffset >100) {
    navv.style.background="white";
    navv.style.boxShadow="5px 2px 15px black";
  }

  else {
    navv.style.background="transparent";
    navv.style.boxShadow="none";
  }

}