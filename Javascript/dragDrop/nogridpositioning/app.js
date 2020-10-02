function makeResizableDiv(div) {
  const element = document.querySelector(div);
  const resizers = document.querySelectorAll(div + ' .resizer');
  for (let i = 0; i < resizers.length; i++) {
    const currentResizer = resizers[i];
    currentResizer.addEventListener('mousedown', function (e) {
      e.preventDefault();
      window.addEventListener('mousemove', resize);
      window.addEventListener('mouseup', stopResize);
    });

    function resize(e) {
      if (currentResizer.classList.contains('bottom-right')) {
        element.style.width =
          e.pageX - element.getBoundingClientRect().left + 'px';
      }
    }

    function stopResize() {
      window.removeEventListener('mousemove', resize);
    }
  }
}

makeResizableDiv('.resizable');
