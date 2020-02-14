$('DIV#add_item').click(e => {
  const element = '<li>Item</li>';
  $('UL.my_list').append(element);
});
