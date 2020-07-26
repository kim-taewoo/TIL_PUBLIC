const mouseMove = (e) => {

}

const mouseUp = (e) => {

}

const mouseDown = (e) => {
  window.addEventListener('mousemove', mouseMove);
  window.addEventListener('mouseup', mouseUp);

  let prevX = e.clientX;
  let prevY = e.clientY;

}

const el = document.querySelector('.item')

el.addEventListener('mousedown', mouseDown)

