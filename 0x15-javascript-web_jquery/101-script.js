$(document).ready(() => {
  const element = '<li>Item</li>';
  const list = $('UL.my_list');

  $('div').click(e => {
    switch (e.target.id) {
      case 'add_item':
        $(list).append(element);
        break;

      case 'remove_item':
        $('li').last().remove();
        break;

      case 'clear_list':
        $('li').remove();
        break;

      default:
        break;
    }
  });
});
