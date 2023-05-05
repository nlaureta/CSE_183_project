class Circle{
  constructor(){
    this.type = 'circle';
    this.position = [0.0,0.0,0.0];
    this.color = [1.0,1.0,1.0,1.0];
    this.size = 5.0;
    this.seg = 3.0;
  }

  render(){
    var xy   = this.position;
    var rgba = this.color;
    var size = this.size;
    var d = this.size/200.0;
    let s = this.seg;
    let vertices = [];

    // Pass the color of point to u_FragColor variable
    gl.uniform4f(u_FragColor, rgba[0], rgba[1], rgba[2], rgba[3]);
    // Pass the size of point to u_Size variable
    gl.uniform1f(u_Size, size);
    // Draw 
    for (var i = 0; i <= s; i++){
      let angle = 2 * Math.PI * i / s;
      let x = xy[0] + d/2 * Math.cos(angle);
      let y = xy[1] + d/2 * Math.sin(angle);
      vertices.push(x, y);
    }
    
    drawCircle(s, vertices);
  }
}

function drawCircle(seg, vertices) {
var n = seg;

// Create a buffer object
var vertexBuffer = gl.createBuffer();
if (!vertexBuffer) {
  console.log('Failed to create the buffer object');
  return -1;
}

// Bind the buffer object to target
gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
// Write date into the buffer object
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.DYNAMIC_DRAW);
// Assign the buffer object to a_Position variable
gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, 0, 0);
// Enable the assignment to a_Position variable
gl.enableVertexAttribArray(a_Position);
// Draw
gl.drawArrays(gl.TRIANGLE_FAN, 0, n);
} 