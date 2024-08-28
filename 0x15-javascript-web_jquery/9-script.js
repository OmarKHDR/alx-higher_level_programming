window.onload = $.get('https://hellosalut.stefanbohacek.dev/?lang=fr').done((data)=>{
    $('header').text(data.hello)
});