// based on http://www.html5rocks.com/en/tutorials/file/dndfiles/

// When we get text we'll just make a paragraph element with the text

//https://github.com/shiffman/Programming-from-A-to-Z-F14/blob/master/week1/05_fileinput_p5/04_loadFile_DragDrop/sketch.js

var jsonTest;

function process(text) {
  createP(text);
}

function setup() {

  noCanvas();
  
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    console.log('Great success! All the File APIs are supported');
  } else {
    alert('The File APIs are not fully supported in this browser.');
  }
  
  $.ajax({
    url: "http://localhost:80", // -> url: "/server"
    type: "POST",
    data: event.target.result,
    dataType: "text",
    success: function(data) {
      jsonTest = data;
      selectableForceDirectedGraph(data);
  }});
  
  var txt = createDiv('<p align="center"> >\Explicación <\ </p>');
  txt.style('background','#EEEEEE');
  
  // This div is create to the graph
  var nd = createDiv();
  nd.id('d3_selectable_force_directed_graph');
  nd.style('align', 'center');
}
