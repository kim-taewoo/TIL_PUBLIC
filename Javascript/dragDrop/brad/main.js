const fill = document.querySelector('.fill')
const empties = document.querySelectorAll('.empty');

fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);

// Loop empties and call drag events

for (const empty of empties) {
  empty.addEventListener('dragover', dragOver);
  empty.addEventListener('dragenter', dragEnter);
  empty.addEventListener('dragleave', dragLeave);
  empty.addEventListener('drop', dragDrop);
}

function dragStart(e) {
  e.target.classList.add('hold');
  setTimeout(() => (e.target.className = 'invisible'), 0);
}

function dragEnd(e) {
  e.target.className = 'fill'
}

function dragOver(e) {
  e.preventDefault();
}

function dragEnter(e) {
  this.classList.add('hovered');
}

function dragLeave () {
  this.className = 'empty'
}

function dragDrop() {
  this.className = 'empty'
  this.append(fill)
}