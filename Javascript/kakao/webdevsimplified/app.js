const draggables = document.querySelectorAll('.draggable');
const containers = document.querySelectorAll('.drag-container');

const dragState = {
  dragging: null,
};

const dragStart = (draggable) => {
  draggable.classList.add('dragging');
  dragState.dragging = draggable;
};

const dragEnd = (draggable) => {
  draggable.classList.remove('dragging');
  dragState.dragging = null;
};

const dragOver = (e, container) => {
  e.preventDefault();
  container.appendChild(dragState.dragging)
};

for (const draggable of draggables) {
  draggable.addEventListener('dragstart', () => dragStart(draggable));
  draggable.addEventListener('dragend', () => dragEnd(draggable));
}

for (const container of containers) {
  container.addEventListener('dragover', e => dragOver(e, container))
}