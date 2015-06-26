$( document ).ready(function() {
  console.log("ready!");
  $('.container').onclick = function(){
    console.log("2");
  }
  document.getElementById('button').onclick = function(){
    console.log("test1");
      $.ajax({
      url: "test",
    }).done(function() {
      console.log("sent POST!");
    });
  }
});