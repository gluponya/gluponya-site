(function(){
  var root=document.documentElement;
  function set(l){
    root.setAttribute("data-lang",l);
    root.lang=l;
    document.querySelectorAll("[data-set-lang]").forEach(function(b){b.classList.toggle("on",b.dataset.setLang===l)});
    if(l==="en"){if(location.hash!=="#en")history.replaceState(null,"","#en")}
    else if(location.hash==="#en")history.replaceState(null,"",location.pathname);
  }
  set(location.hash==="#en"?"en":"uk");
  document.querySelectorAll("[data-set-lang]").forEach(function(b){b.addEventListener("click",function(){set(b.dataset.setLang)})});
  window.addEventListener("hashchange",function(){if(location.hash==="#en")set("en")});
})();
