// Fraction Bars: drag a slider to split a bar into equal parts and shade some of them.
let parts;
function setup() { createCanvas(400, 120); parts = createSlider(1, 12, 4); }
function draw() { background(255); const n = parts.value(); for (let i = 0; i < n; i++) rect(i * width / n, 20, width / n, 60); }
