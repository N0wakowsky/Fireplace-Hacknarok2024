document.addEventListener('visibilitychange', function() {
  /*
    if (document.hidden) {
      alert("chuj");
    } else {
      alert("nie chuj");
    }
  */
    if (document.onblur) {
      alert("kutaśnie")
    } else {
      alert('smerfastycznie')
    }

});