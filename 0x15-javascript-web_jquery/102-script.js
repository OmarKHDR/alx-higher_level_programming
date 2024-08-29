window.onload = ()=>{
  $('input#btn_translate').click(()=>{
    let lang = $('input#language_code').val()
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`,(out)=>{
        $('div#hello').text(out.hello);
    })
  })
}