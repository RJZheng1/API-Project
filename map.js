document.addEventListener("load", initialize());
console.log("B");

var map;

function initialize() {
    console.log("A");
    var canvas = document.getElementById("map-canvas");
    map = new google.maps.Map(document.getElementById("map-canvas"), {
	zoom: 13,
    });  
}
