// Resize an embedded MicroSim iframe to the height the MicroSim reports.
// The overlay engines in docs/sims/shared-libs post { type: 'microsim-resize', height } to the parent page.
window.addEventListener('message', function (event) {
  if (!event.data || event.data.type !== 'microsim-resize') return;
  var iframes = document.querySelectorAll('iframe');
  for (var i = 0; i < iframes.length; i++) {
    if (iframes[i].contentWindow === event.source) {
      iframes[i].style.height = event.data.height + 'px';
      break;
    }
  }
});
