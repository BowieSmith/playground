let x = 0;

function setup() {
    createCanvas(600,600);
}

function draw() {
    let rad = random() * (2 * PI);
    let length = random() * 400;
    line(mouseX, mouseY, mouseX + cos(rad) * length, mouseY + sin(rad) * length);
}
