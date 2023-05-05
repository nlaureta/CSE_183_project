// ColoredPoint.js (c) 2012 matsuda
// Vertex shader program
var VSHADER_SOURCE = `
  attribute vec4 a_Position;
  uniform float u_Size;
  void main() {
    gl_Position = a_Position;
    gl_PointSize = u_Size; 
  }`

// Fragment shader program
var FSHADER_SOURCE = `
  precision mediump float;
  uniform vec4 u_FragColor;
  void main() {
    gl_FragColor = u_FragColor;
  }`

// Constant Variable
const POINT = 0;
const TRIANGLE = 1;
const CIRCLE = 2;

// Global Variable
let canvas;
let gl;
let a_Position;
let u_FragColor;
let u_Size;
var g_shapesList = [];
let g_selectedColor = [1.0,1.0,1.0,1.0];
let g_selectedSize = 5;
let g_selectedType = POINT;
let g_selectedSeg = 3;

function setUpWebGL(){
  // Retrieve <canvas> element
  canvas = document.getElementById('webgl');

  // Get the rendering context for WebGL
  gl = canvas.getContext("webgl", {preseveDrawingBuffer: true});
  if (!gl) {
    console.log('Failed to get the rendering context for WebGL');
    return;
  }
}

function connectVariablesToGLSL(){
  // Initialize shaders
  if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
    console.log('Failed to intialize shaders.');
    return;
  }

  // Get the storage location of a_Position
  a_Position = gl.getAttribLocation(gl.program, 'a_Position');
  if (a_Position < 0) {
    console.log('Failed to get the storage location of a_Position');
    return;
  }

  // Get the storage location of u_FragColor
  u_FragColor = gl.getUniformLocation(gl.program, 'u_FragColor');
  if (!u_FragColor) {
    console.log('Failed to get the storage location of u_FragColor');
    return;
  }

  // Get the storage location of u_Size
  u_Size = gl.getUniformLocation(gl.program, 'u_Size');
  if (!u_Size) {
    console.log('Failed to get the storage location of u_Size');
    return;
  }
}

// set up actions for HTML UI elements
function addActionForHtmlUI(){
  // Buttons Events
  document.getElementById('clear').onclick = function() {
    g_shapesList = [];
    renderAllShapes();
  }; 
  document.getElementById('pointButton').onclick = function() {g_selectedType = POINT;}; 
  document.getElementById('triglButton').onclick = function() {g_selectedType = TRIANGLE;};
  document.getElementById('circlButton').onclick = function() {g_selectedType = CIRCLE;};

  // Slider Events
  document.getElementById('redSlide').addEventListener('mouseup', function() {g_selectedColor[0] = this.value/100;});
  document.getElementById('greSlide').addEventListener('mouseup', function() {g_selectedColor[1] = this.value/100;});
  document.getElementById('bluSlide').addEventListener('mouseup', function() {g_selectedColor[2] = this.value/100;});
  
  document.getElementById('sizeSlide').addEventListener('mouseup', function() {g_selectedSize = this.value;});

  document.getElementById('segSlide').addEventListener('mouseup', function() {g_selectedSeg = this.value;});
}

function main() {
  // Set up canvas and gl variables
  setUpWebGL();

  // Set up GLSL shader programs and connect GLSL variables
  connectVariablesToGLSL();

  // Set up actions for the HTML UI elements
  addActionForHtmlUI();

  // Regiseter function (event handler) to be called on a mouse press
  canvas.onmousedown = click;
  canvas.onmousemove = function(ev) {if(ev.buttons==1) {click(ev)}}; 
  
  // Specify the color for clearing <canvas>
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  // Clear canvas <canvas>
  gl.clear(gl.COLOR_BUFFER_BIT);
}

function click(ev) {
  let [x, y] = convertCoordinatesEventToGL(ev);

  let point;
  if(g_selectedType == POINT) {
    point = new Point();
  }

  else if(g_selectedType == TRIANGLE) {
    point = new Triangle();
  }
   
  else {
    point = new Circle();
    point.seg = g_selectedSeg;
  }

  point.position = [x, y];
  point.color = g_selectedColor.slice();
  point.size  = g_selectedSize;
  g_shapesList.push(point);

  renderAllShapes();
}

function convertCoordinatesEventToGL(ev){
  var x = ev.clientX;
  var y = ev.clientY;
  var rect = ev.target.getBoundingClientRect();

  x = ((x - rect.left) - canvas.width/2)/(canvas.width/2);
  y = (canvas.height/2 - (y - rect.top))/(canvas.height/2);
  return ([x,y]);
}

function renderAllShapes(){
  // Clear canvas
  gl.clear(gl.COLOR_BUFFER_BIT);

  var len = g_shapesList.length;
  for(var i = 0; i < len; i++) {
    g_shapesList[i].render();
  }
}