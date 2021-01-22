// rolar a tela automaticamente quando clicar em um link
$('div a').click(function(e){
   e.preventDefault();
   var id = $(this).attr('href'),
      targetOffset = $(id).offset().top;
   $('html, body').animate({
      scrollTop: targetOffset
   }, 10000);
});
