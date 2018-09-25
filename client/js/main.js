//http://www.html5rocks.com/en/tutorials/file/dndfiles/
//https://github.com/shiffman/Programming-from-A-to-Z-F14/blob/master/week1/05_fileinput_p5/04_loadFile_DragDrop/sketch.js

function setup() {

  noCanvas();
}

$.getJSON('json/graph.json', selectableForceDirectedGraph);

function showInfo(u){

  $.getJSON('json/info.json', function (data) {

    //# CODCP DEP PROV DIST NOMCP MNOMCP
    var info = "Datos: "+
    "CODCP: " + data.lugar[u.index].CODCP + ", " +
    "DEP: " + data.lugar[u.index].DEP + ", " +
    "PROV: " + data.lugar[u.index].PROV + ", " +
    "DIST: " + data.lugar[u.index].DIST + ", " +
    "NOMCP: " + data.lugar[u.index].NOMCP + ", " +
    "MNOMCP: " + data.lugar[u.index].MNOMCP;

    var text = document.getElementById("info");
    text.innerHTML = info;
  });
}
