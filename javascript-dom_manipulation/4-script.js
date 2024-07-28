#!/usr/bin/node
/* task 4
Write a JavaScript script that adds a `li` element
to a list when the user clicks on the element with id `add_item`:

The new element must be: `<li>Item</li>`
The new element must be added to the `ul`
element with class `my_list`
*/

const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');
setItem.addEventListener('click', () => {
  const nuevo = document.createElement('li');
  nuevo.textContent = 'Item';
  listClass.appendChild(nuevo);
});
