// based on http://www.html5rocks.com/en/tutorials/file/dndfiles/

// When we get text we'll just make a paragraph element with the text

//https://github.com/shiffman/Programming-from-A-to-Z-F14/blob/master/week1/05_fileinput_p5/04_loadFile_DragDrop/sketch.js

function process(text) {
  createP(text);
}

function setup() {

  noCanvas();
  // Check for the various File API support.
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    console.log('Great success! All the File APIs are supported');
  } else {
    alert('The File APIs are not fully supported in this browser.');
  }

  // <div id="drop_zone">Arraste el archivo aqui
  // Make a div to drag a file on
  var dropZone = createDiv('<p align="center"> >\Arraste el archivo aqui <\ </p>');
  dropZone.id('drop_zone');
  dropZone.style('background','#EEEEEE');

  // A description of files
  var dfile = createDiv();
  dfile.id('dfile');

  // This div is create to the graph
  var nd = createDiv();
  nd.id('d3_selectable_force_directed_graph');
  nd.style('align', 'center');

  // Add some events
  dropZone.elt.addEventListener('dragover', handleDragOver, false);
  dropZone.elt.addEventListener('drop', handleFileSelect, false);
  dropZone.elt.addEventListener('dragleave', handleDragLeave, false);

  // When you drag a file on top
  function handleDragOver(evt) {
    // Stop the default browser behavior
    evt.stopPropagation();
    evt.preventDefault();
    dropZone.style('background','#AAAAAA');
  }

  // If the mosue leaves
  function handleDragLeave(evt) {
    evt.stopPropagation();
    evt.preventDefault();
  }

  // If you drop the file
  function handleFileSelect(evt) {

    evt.stopPropagation();
    evt.preventDefault();
    dropZone.style('background','#EEEEEE');

    var f = evt.dataTransfer.files[0];

    if ( f.type == 'application/json'){
      
      document.getElementById('dfile').innerHTML = ('Nombre: [' + f.name + '] Tipo: [' + f.type + '] Tamaño: [' + f.size + ']');
      reader = new FileReader();
      reader.onload = function(event) {
        selectableForceDirectedGraph(event.target.result);
      }
      reader.readAsBinaryString(f);
    }
    else{
      document.getElementById('dfile').innerHTML = 'El archivo no es comprensible.';
    }
  }
}
