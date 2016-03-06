
$(function(){


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

  $('ul.tabs').tabs();
  $('select').material_select();
  $('.collapsible').collapsible({
    accordion : false
  });
});
