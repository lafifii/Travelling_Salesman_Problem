
$.getJSON('json/path.json', function (data) {

  for(var i = 0; i < data[0].node.length; i++){

    var nd = document.createElement("li");
    var textnode = document.createTextNode(data[0].node[i]+" -> ");
    nd.appendChild(textnode);
    document.getElementById("myList").appendChild(nd);
  }
});
