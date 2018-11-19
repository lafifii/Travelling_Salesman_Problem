//http://www.html5rocks.com/en/tutorials/file/dndfiles/
//https://github.com/shiffman/Programming-from-A-to-Z-F14/blob/master/week1/05_fileinput_p5/04_loadFile_DragDrop/sketch.js

var myTxt;
var pimg;

var jsoninfo;
var inCP;

function setup() {

  var cvs = createCanvas(window.innerWidth*0.5, window.innerHeight*0.66);
  cvs.background(255);
  cvs.class("c2");

  myTxt = [" - ", " - ", " - ", " - ", " - ", " - "]

  pimg = loadImage("img/perumap.png");

  button = createButton('Ver informe');
  button.class("myButton");
  button.position(window.innerWidth*0.8, window.innerHeight*0.05);
  button.mousePressed(gotoPath);
  selGraph();
}

function selGraph(){
  
  myTxt = [" - ", " - ", " - ", " - ", " - ", " - "]
  var cnv = document.getElementById('d3_selectable_force_directed_graph');
  while (cnv.firstChild) {
    cnv.removeChild(cnv.firstChild);
  }
  
  var alg = document.getElementById("ALG").value;
  var lug = document.getElementById("LUG").value;

  var dirAlg = "";
  var dirLug = "";

  if(alg=="Held Carp"){
    dirAlg = "DP";
  }
  else if(alg=="Disjoint Pair Clustering"){
    dirAlg = "DPC";
  }
  else if(alg=="Greedy"){
    dirAlg = "MST";
  }
  
  var ss = "Distancia recorrida: ";
  
  if(lug=="Centros Poblados"){
    dirLug = "CP";
    inCP = true;
    if(alg=="Held Carp"){
      ss+="3109";
    }
    else if(alg=="Disjoint Pair Clustering"){
      ss+="29096";
    }
    else if(alg=="Greedy"){
      ss+="";
    }
  }
  else if(lug=="Locales Escolares"){
    dirLug = "LE";
    inCP = false;
    
    if(alg=="Held Carp"){
      ss+="978";
    }
    else if(alg=="Disjoint Pair Clustering"){
      ss+="27217";
    }
    else if(alg=="Greedy"){
      ss+="13245";
    }
  }
  var dr = document.getElementById("distrec");
  dr.innerHTML = ss;

  console.log(dirAlg, ", ", dirLug);
  
  $.getJSON('json/'+dirAlg+'/'+dirLug+'/'+'info.json', function (data) {
    jsoninfo = data.lugar;
    console.log(jsoninfo);
  });
  $.getJSON('json/'+dirAlg+'/'+dirLug+'/'+'graph.json', selectableForceDirectedGraph);
  
}

function gotoPath(){

  window.open("https://docs.google.com/document/d/15HaeZNwWEzzftJX7wHV89RrxSecl6PZafJLNJdmRtpQ/edit?usp=sharing","","height=600,width=600,scrollbars=yes");
}

function draw(){


  background(255);
  var x = width/16, y = height/25;
  textSize(24);
  text("Datos del nodo seleccionado", width*(1/4), y*2);
  textSize(12);
  if(inCP){
    text("CODCP", x, y+y*3);
    text("DEP", x, y+y*6);
    text("PROV ", x, y+y*9);
    text("DIST ", x, y+y*12);
    text("NOMCP", x, y+y*15);
    text("MNOMC ", x, y+y*18);
    for(var i = 0; i < 6; i++){

      text(myTxt[i], x+x*2.4, y+(((i+1)*3)*y));
    }
  }
  else{
    
    text("CODCPSIG", x, y+y*3);
    text("CEN_EDU_L", x, y+y*6);
    text("NOMCPSIG ", x, y+y*9);
    for(var i = 0; i < 3; i++){

      text(myTxt[i], x+x*2.8, y+(((i+1)*3)*y));
    }
  }
  
  image(pimg, width*0.5, height*0.15, width*0.35, width*0.57);
}

function showInfo(u){
  
  myTxt = [" - ", " - ", " - ", " - ", " - ", " - "]
  console.log(u);
  var i;
  for(i = 0; i < jsoninfo.length; i++){
    if(jsoninfo[i].CODCP == u.cod && inCP){
      var d = jsoninfo[i];
      //# CODCP DEP PROV DIST NOMCP MNOMCP
      myTxt[0] = d.CODCP;
      myTxt[1] = d.DEP;
      myTxt[2] = d.PROV;
      myTxt[3] = d.DIST;
      myTxt[4] = d.NOMCP;
      myTxt[5] = d.MNOMCP;
      console.log("Encontrado!");
      break;
    }
    else if(jsoninfo[i].CODCPSIG == u.cod && !inCP){
      var d = jsoninfo[i];
      //# CODCPSIG CEN_EDU_L NOMCPSIG
      myTxt[0] = d.CODCPSIG;
      myTxt[1] = d.CEN_EDU_L;
      myTxt[2] = d.NOMCPSIG;
      console.log("Encontrado!");
      break;
    }
  }
  if(i==jsoninfo.length){
    console.log("No se encontró!");
  }
}
