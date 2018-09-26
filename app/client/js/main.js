//http://www.html5rocks.com/en/tutorials/file/dndfiles/
//https://github.com/shiffman/Programming-from-A-to-Z-F14/blob/master/week1/05_fileinput_p5/04_loadFile_DragDrop/sketch.js

var myTxt;
var pimg;

function setup() {

  var cvs = createCanvas(window.innerWidth*0.5, window.innerHeight*0.66);
  cvs.background(255);
  cvs.class("c2");

  myTxt = [" - ", " - ", " - ", " - ", " - ", " - "]

  //pimg = loadImage("img/perumap.png");

  button = createButton('Ver informe');
  button.class("myButton");
  button.position(window.innerWidth*0.7, window.innerHeight*0.05);
  button.mousePressed(gotoPath);
}

function gotoPath(){

  window.open("path.html","","height=600,width=600,scrollbars=yes");
}

function draw(){

  background(255);
  var x = width/16, y = height/25;
  textSize(24);
  text("Datos del grafo seleccionado", width*(1/4), y*2);
  textSize(12);
  text("CODCP", x, y+y*3);
  text("DEP", x, y+y*6);
  text("PROV ", x, y+y*9);
  text("DIST ", x, y+y*12);
  text("NOMCP", x, y+y*15);
  text("MNOMC ", x, y+y*18);

  for(var i = 0; i < 6; i++){

    text(myTxt[i], x+x*2.4, y+(((i+1)*3)*y));
  }

  //image(pimg, width*0.5, height*0.15, width*0.37, height*0.8);
}

$.getJSON('json/graph.json', selectableForceDirectedGraph);

function showInfo(u){

  $.getJSON('json/info.json', function (data) {

    //# CODCP DEP PROV DIST NOMCP MNOMCP
    console.log(u.x/100, -u.y/100);
    myTxt[0] = data.lugar[u.index].CODCP;
    myTxt[1] = data.lugar[u.index].DEP;
    myTxt[2] = data.lugar[u.index].PROV;
    myTxt[3] = data.lugar[u.index].DIST;
    myTxt[4] = data.lugar[u.index].NOMCP;
    myTxt[5] = data.lugar[u.index].MNOMCP;

    var text = document.getElementById("info");
    text.innerHTML = info;
  });
}
