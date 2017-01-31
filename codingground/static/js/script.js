 /*
 $('body').keyup(function(e) {
    console.log('keyup called');
    var code = e.keyCode || e.which;
    if (code == '9') {
    alert('Tab pressed');
    }
 });
 */

 $('.comment').keydown(function(e) {
   console.log('keyup called');
   var code = e.keyCode || e.which;
   if (code == '9') {
     alert('Tab pressed');

   return false;
   }

});