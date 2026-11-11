(function(){
  var root=document.documentElement;
  function set(l){
    root.setAttribute("data-lang",l);
    root.lang=l;
    document.querySelectorAll("[data-set-lang]").forEach(function(b){b.classList.toggle("on",b.dataset.setLang===l)});
    if(l==="ru"){if(location.hash!=="#ru")history.replaceState(null,"",location.pathname+"#ru")}
    else if(location.hash==="#ru")history.replaceState(null,"",location.pathname);
  }
  set(root.getAttribute("data-lang")==="ru"?"ru":"uk");
  document.querySelectorAll("[data-set-lang]").forEach(function(b){b.addEventListener("click",function(){set(b.dataset.setLang)})});
  window.addEventListener("hashchange",function(){if(location.hash==="#ru")set("ru")});
})();
