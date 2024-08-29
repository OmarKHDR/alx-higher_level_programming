
window.onload = ()=>{
    $('DIV#add_item').click(()=>{
    $('ul').append('<li>Item</li>');
});

$('DIV#remove_item').click(()=>{
    $('ul li:last-child').remove();
});
$('DIV#clear_list').click(()=>{
    $('ul li').empty();
});
}