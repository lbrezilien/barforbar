

$('#accountForm').on('submit',function(e){
  e.preventDefault();
  $.post('/users/update_account', $(this).serialize()).done(function(){
    debugger;

  });
});

$('#aboutForm').on('submit', function(e){
  e.preventDefault();
  $.post('/users/update_about', $(this).serialize()).done(function(){
    debugger;

  });
});

$(document).ready(function(){
  $('ul.tabs').tabs();
});

$(document).ready(function(){

  $('.collapsible').collapsible({
    accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
  });
});
