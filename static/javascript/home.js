$( document ).ready(function() {
  console.log("ready!");
  $('button').click(function(){
    console.log("test1");
      $.get("/test");
  });
});