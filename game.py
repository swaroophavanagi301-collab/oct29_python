
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NEON RUNNER | Dino Protocol</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@500;600;700&display=swap');

:root {
  --cyan: #00f5ff;
  --purple: #a855f7;
  --pink: #ff3cac;
  --bg: #050610;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  min-height: 100vh;
  background: var(--bg);
  color: white;
  font-family: 'Rajdhani', sans-serif;
  overflow-x: hidden;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse at 50% 40%, #152449 0%, transparent 55%),
    radial-gradient(ellipse at 10% 80%, #35104d55, transparent 45%);
  z-index: -2;
}

.grid {
  position: fixed;
  inset: 50% -50% -40%;
  background-image:
    linear-gradient(#00f5ff20 1px, transparent 1px),
    linear-gradient(90deg, #00f5ff20 1px, transparent 1px);
  background-size: 48px 48px;
  transform: perspective(350px) rotateX(58deg);
  transform-origin: top;
  mask-image: linear-gradient(transparent, black 30%, transparent);
  pointer-events: none;
  z-index: -1;
}

header {
  max-width: 1200px;
  margin: auto;
  padding: 25px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}

.logo {
  font: 900 20px 'Orbitron', sans-serif;
  letter-spacing: 2px;
}

.logo span { color: var(--cyan); }

.status {
  font: 12px 'Orbitron', sans-serif;
  letter-spacing: 2px;
  color: #8bffce;
}

.status::before {
  content: "";
  display: inline-block;
  width: 7px;
  height: 7px;
  background: #8bffce;
  border-radius: 50%;
  margin-right: 10px;
  box-shadow: 0 0 12px #8bffce;
}

main {
  max-width: 1150px;
  padding: 20px 24px 60px;
  margin: auto;
}

.hero { text-align: center; margin: 20px 0 30px; }

.eyebrow {
  color: var(--cyan);
  font: 11px 'Orbitron', sans-serif;
  letter-spacing: 5px;
}

h1 {
  font: 900 clamp(34px, 6vw, 72px) 'Orbitron', sans-serif;
  margin: 15px 0 8px;
  letter-spacing: -2px;
  line-height: 1.15;
  text-shadow: 0 0 35px #00f5ff35;
}

h1 span {
  color: var(--cyan);
  text-shadow: 0 0 25px #00f5ff90;
}

.subtitle {
  color: #9aa7c7;
  font-size: 18px;
  letter-spacing: 1px;
  margin: 15px 0;
}

.game-shell {
  position: relative;
  border: 1px solid #00f5ff50;
  background: #080c1c;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 0 45px #00f5ff12, 0 25px 100px #0009;
}

.game-shell::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 2;
  background: repeating-linear-gradient(
    transparent 0px, transparent 3px, #00000012 4px
  );
}

.hud {
  position: relative;
  z-index: 3;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 17px 22px;
  border-bottom: 1px solid #ffffff13;
  background: #080b18dd;
}

.hud-label {
  font: 10px 'Orbitron', sans-serif;
  letter-spacing: 2px;
  color: #7887a8;
}

.hud-value {
  font: 700 23px 'Orbitron', sans-serif;
  color: var(--cyan);
}

#canvas {
  width: 100%;
  display: block;
  height: auto;
  aspect-ratio: 900 / 340;
  touch-action: manipulation;
}

.overlay {
  position: absolute;
  z-index: 4;
  inset: 65px 0 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 20px;
  background: #05061065;
  backdrop-filter: blur(3px);
  transition: opacity .25s;
}

.overlay.hidden {
  opacity: 0;
  pointer-events: none;
}

.overlay h2 {
  font: 900 clamp(24px, 4vw, 43px) 'Orbitron', sans-serif;
  margin: 10px 0;
  text-shadow: 0 0 30px #00f5ff70;
}

.overlay p {
  color: #b2bfd9;
  font-size: 17px;
  margin: 8px 0 20px;
}

.main-btn {
  border: 1px solid var(--cyan);
  background: var(--cyan);
  color: #030713;
  padding: 15px 32px;
  font: 800 12px 'Orbitron', sans-serif;
  letter-spacing: 2px;
  cursor: pointer;
  border-radius: 4px;
  box-shadow: 0 0 30px #00f5ff35;
  transition: .2s;
}

.main-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 35px #00f5ff80;
}

.controls {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 22px;
}

.control {
  border: 1px solid #263451;
  background: #0c1121;
  color: #c4d0eb;
  padding: 12px 18px;
  border-radius: 7px;
  font-size: 15px;
}

kbd {
  font: 11px 'Orbitron', sans-serif;
  color: var(--cyan);
  border: 1px solid #00f5ff40;
  border-radius: 4px;
  padding: 5px 7px;
  margin-right: 8px;
}

.bottom-info {
  display: flex;
  justify-content: space-between;
  gap: 15px;
  flex-wrap: wrap;
  margin-top: 25px;
  color: #657391;
  font: 10px 'Orbitron', sans-serif;
  letter-spacing: 1px;
}

.bottom-info span { color: var(--cyan); }

.mobile-controls {
  display: none;
  gap: 12px;
  justify-content: center;
  margin-top: 18px;
}

.mobile-controls button {
  flex: 1;
  max-width: 200px;
  padding: 15px;
  background: #10182b;
  color: var(--cyan);
  border: 1px solid #00f5ff55;
  border-radius: 7px;
  font: 700 12px 'Orbitron', sans-serif;
  touch-action: none;
}

@media(max-width: 600px) {
  header { padding: 20px 15px; }
  main { padding: 10px 12px 40px; }
  .logo { font-size: 14px; }
  .status { font-size: 9px; }
  .hud { padding: 12px; }
  .hud-value { font-size: 17px; }
  .hud-label { font-size: 8px; letter-spacing: 1px; }
  .mobile-controls { display: flex; }
  .controls { gap: 6px; }
  .control { font-size: 12px; padding: 10px; }
  .bottom-info { font-size: 8px; }
}
</style>
</head>

<body>
<div class="grid"></div>

<header>
  <div class="logo">NEON<span>RUNNER</span></div>
  <div class="status">SYSTEM ONLINE</div>
</header>

<main>
  <section class="hero">
    <div class="eyebrow">THE OFFLINE LEGEND // REIMAGINED</div>
    <h1>DINO <span>PROTOCOL</span></h1>
    <p class="subtitle">One runner. Infinite darkness. Don't stop.</p>
  </section>

  <section class="game-shell">
    <div class="hud">
      <div>
        <div class="hud-label">DISTANCE SCORE</div>
        <div class="hud-value" id="score">00000</div>
      </div>
      <div style="text-align:center">
        <div class="hud-label">VELOCITY</div>
        <div class="hud-value" id="speed">01.0x</div>
      </div>
      <div style="text-align:right">
        <div class="hud-label">BEST RUN</div>
        <div class="hud-value" id="best">00000</div>
      </div>
    </div>

    <canvas id="canvas" width="900" height="340"></canvas>

    <div class="overlay" id="overlay">
      <div class="eyebrow">PROJECT // SURVIVAL</div>
      <h2 id="overlayTitle">THE RUN BEGINS</h2>
      <p id="overlayText">The world is offline. How far can you go?</p>
      <button class="main-btn" id="startBtn">INITIALIZE RUN &nbsp; →</button>
    </div>
  </section>

  <div class="controls">
    <div class="control"><kbd>SPACE</kbd> Jump</div>
    <div class="control"><kbd>↓</kbd> Duck</div>
    <div class="control"><kbd>ESC</kbd> Pause</div>
    <div class="control"><kbd>R</kbd> Restart</div>
  </div>

  <div class="mobile-controls">
    <button id="jumpBtn">↑ &nbsp; JUMP</button>
    <button id="duckBtn">↓ &nbsp; DUCK</button>
  </div>

  <div class="bottom-info">
    <div>ENGINE: <span>FLASK + CANVAS</span></div>
    <div>MODE: ENDLESS SURVIVAL</div>
    <div>VERSION <span>01.0.0</span></div>
  </div>
</main>

<script>
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const W = canvas.width, H = canvas.height;
const groundY = 275;

const $ = id => document.getElementById(id);

let state = "ready";
let score = 0;
let best = 0;
let speed = 5;
let frame = 0;
let world = 0;
let obstacles = [];
let particles = [];
let stars = [];
let lastTime = 0;
let accumulator = 0;
const STEP = 1000 / 60;

try {
  best = Number(localStorage.getItem("neonDinoBest")) || 0;
} catch(e) {}

$("best").textContent = String(best).padStart(5, "0");

const dino = {
  x: 100, y: groundY - 44, w: 42, h: 44,
  vy: 0, grounded: true, duck: false,
  anim: 0
};

for (let i = 0; i < 90; i++) {
  stars.push({
    x: Math.random() * W,
    y: Math.random() * 220,
    r: Math.random() * 1.6 + .3,
    a: Math.random() * .7 + .2
  });
}

function roundedRect(x, y, w, h, r, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.roundRect(x, y, w, h, r);
  ctx.fill();
}

function glowLine(x1, y1, x2, y2, color, width=1) {
  ctx.save();
  ctx.strokeStyle = color;
  ctx.lineWidth = width;
  ctx.shadowBlur = 12;
  ctx.shadowColor = color;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.restore();
}

function drawBackground() {
  const sky = ctx.createLinearGradient(0, 0, 0, H);
  sky.addColorStop(0, "#080b20");
  sky.addColorStop(.7, "#17122c");
  sky.addColorStop(1, "#21152e");
  ctx.fillStyle = sky;
  ctx.fillRect(0, 0, W, H);

  // Neon moon
  ctx.save();
  ctx.shadowBlur = 35;
  ctx.shadowColor = "#a855f7";
  const moon = ctx.createRadialGradient(700, 85, 2, 700, 85, 48);
  moon.addColorStop(0, "#f2eaff");
  moon.addColorStop(.6, "#b38cff");
  moon.addColorStop(1, "#8855ff00");
  ctx.fillStyle = moon;
  ctx.beginPath();
  ctx.arc(700, 85, 48, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();

  // Stars
  stars.forEach(s => {
    ctx.globalAlpha = s.a * (.7 + Math.sin(frame * .03 + s.x) * .3);
    ctx.fillStyle = "#c6d8ff";
    ctx.fillRect(s.x, s.y, s.r, s.r);
  });
  ctx.globalAlpha = 1;

  // Distant mountains
  ctx.fillStyle = "#17152f";
  ctx.beginPath();
  ctx.moveTo(0, 240);
  for (let x = 0; x <= W; x += 45) {
    ctx.lineTo(x, 205 + Math.sin(x * .018) * 22 +
      Math.sin(x * .041) * 12);
  }
  ctx.lineTo(W, groundY);
  ctx.lineTo(0, groundY);
  ctx.fill();

  // Near mountains
  ctx.fillStyle = "#211633";
  ctx.beginPath();
  ctx.moveTo(0, 260);
  for (let x = 0; x <= W; x += 35) {
    ctx.lineTo(x, 238 + Math.sin(x * .025 + 2) * 18);
  }
  ctx.lineTo(W, groundY);
  ctx.lineTo(0, groundY);
  ctx.fill();

  // Distant city silhouettes
  ctx.fillStyle = "#100f25";
  for (let x = 0; x < W; x += 38) {
    const bh = 12 + Math.abs(Math.sin(x * 2.1)) * 28;
    ctx.fillRect(x, groundY - bh, 23, bh);
    for (let wy = groundY - bh + 5; wy < groundY - 3; wy += 8) {
      ctx.fillStyle = "#a855f730";
      ctx.fillRect(x + 5, wy, 3, 3);
      ctx.fillRect(x + 14, wy, 3, 3);
      ctx.fillStyle = "#100f25";
    }
  }

  // Ground
  const floor = ctx.createLinearGradient(0, groundY, 0, H);
  floor.addColorStop(0, "#17152c");
  floor.addColorStop(1, "#080b18");
  ctx.fillStyle = floor;
  ctx.fillRect(0, groundY, W, H - groundY);

  glowLine(0, groundY, W, groundY, "#00f5ff", 2);

  // Scrolling ground dashes
  ctx.fillStyle = "#00f5ff65";
  const offset = world % 65;
  for (let x = -offset; x < W; x += 65) {
    ctx.fillRect(x, groundY + 22, 30, 2);
    ctx.fillRect(x + 20, groundY + 37, 12, 1);
  }

  // Horizon glow
  const haze = ctx.createLinearGradient(0, groundY - 28, 0, groundY + 5);
  haze.addColorStop(0, "#ff3cac00");
  haze.addColorStop(1, "#ff3cac24");
  ctx.fillStyle = haze;
  ctx.fillRect(0, groundY - 28, W, 33);
}

function drawDino() {
  const x = dino.x, y = dino.y;
  const duck = dino.duck && dino.grounded;
  const h = duck ? 27 : 44;
  const bodyY = groundY - h;

  ctx.save();
  ctx.shadowColor = "#00f5ff";
  ctx.shadowBlur = 15;

  // Tail
  ctx.fillStyle = "#00d9ee";
  ctx.beginPath();
  ctx.moveTo(x + 5, bodyY + h * .52);
  ctx.lineTo(x - 9, bodyY + h * .36);
  ctx.lineTo(x - 5, bodyY + h * .62);
  ctx.lineTo(x + 8, bodyY + h * .68);
  ctx.fill();

  // Body
  roundedRect(x + 5, bodyY + h * .35, 27, h * .55, 5, "#00d9ee");

  // Head
  roundedRect(x + 19, bodyY + 2, 23, 21, 4, "#53f8ff");

  // Eye
  ctx.shadowBlur = 0;
  ctx.fillStyle = "#061020";
  ctx.fillRect(x + 34, bodyY + 7, 4, 4);
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(x + 35, bodyY + 7, 1, 1);

  // Mouth
  ctx.fillStyle = "#06212d";
  ctx.fillRect(x + 34, bodyY + 17, 7, 2);

  // Legs animate while running
  const step = Math.sin(dino.anim) * 8;
  ctx.strokeStyle = "#53f8ff";
  ctx.lineWidth = 5;
  ctx.lineCap = "round";

  ctx.beginPath();
  if (!dino.grounded) {
    ctx.moveTo(x + 13, bodyY + h * .75);
    ctx.lineTo(x + 7, bodyY + h * .93);
    ctx.moveTo(x + 25, bodyY + h * .75);
    ctx.lineTo(x + 32, bodyY + h * .91);
  } else {
    ctx.moveTo(x + 13, bodyY + h * .77);
    ctx.lineTo(x + 13 + step, bodyY + h);
    ctx.moveTo(x + 27, bodyY + h * .77);
    ctx.lineTo(x + 27 - step, bodyY + h);
  }
  ctx.stroke();

  // Back spikes
  ctx.fillStyle = "#a855f7";
  for (let i = 0; i < 3; i++) {
    ctx.beginPath();
    ctx.moveTo(x + 9 + i * 7, bodyY + h * .35);
    ctx.lineTo(x + 13 + i * 7, bodyY + h * .18);
    ctx.lineTo(x + 18 + i * 7, bodyY + h * .36);
    ctx.fill();
  }
  ctx.restore();
}

function spawnObstacle() {
  const flying = score > 180 && Math.random() < .28;
  if (flying) {
    obstacles.push({
      x: W + 20, y: groundY - 65 - Math.random() * 30,
      w: 36, h: 20, type: "drone"
    });
  } else {
    const tall = Math.random() < .35;
    obstacles.push({
      x: W + 20, y: groundY - (tall ? 48 : 34),
      w: tall ? 24 : 18, h: tall ? 48 : 34,
      type: "cactus"
    });
  }
}

function drawObstacle(o) {
  ctx.save();
  ctx.shadowColor = o.type === "drone" ? "#ff3cac" : "#ff743c";
  ctx.shadowBlur = 14;

  if (o.type === "drone") {
    roundedRect(o.x, o.y, o.w, o.h, 6, "#ff3cac");
    roundedRect(o.x + 8, o.y + 6, o.w - 16, 5, 2, "#fff0ff");
    glowLine(o.x + 5, o.y - 4, o.x + o.w - 5, o.y - 4, "#ff3cac", 2);
  } else {
    roundedRect(o.x, o.y + 7, o.w, o.h - 7, 4, "#ff743c");
    roundedRect(o.x - 7, o.y + 15, 10, 6, 3, "#ff743c");
    if (o.h > 40) {
      roundedRect(o.x + 14, o.y + 22, 10, 6, 3, "#ff743c");
    }
    glowLine(o.x + 4, o.y + 12, o.x + 4, o.y + o.h - 5, "#ffd1b8", 1);
  }
  ctx.restore();
}

function burst(x, y, color) {
  for (let i = 0; i < 18; i++) {
    particles.push({
      x, y,
      vx: (Math.random() - .5) * 7,
      vy: (Math.random() - .5) * 7,
      life: 35,
      color
    });
  }
}

function drawParticles() {
  particles.forEach(p => {
    ctx.globalAlpha = Math.max(0, p.life / 35);
    ctx.fillStyle = p.color;
    ctx.fillRect(p.x, p.y, 3, 3);
  });
  ctx.globalAlpha = 1;
}

function updateParticles() {
  particles.forEach(p => {
    p.x += p.vx;
    p.y += p.vy;
    p.vy += .12;
    p.life--;
  });
  particles = particles.filter(p => p.life > 0);
}

function hit(a, b) {
  return a.x + a.w - 8 > b.x + 3 &&
         a.x + 7 < b.x + b.w - 3 &&
         a.y + a.h - 3 > b.y + 3 &&
         a.y + 5 < b.y + b.h;
}

function startGame() {
  score = 0;
  speed = 5;
  frame = 0;
  world = 0;
  obstacles = [];
  particles = [];
  dino.y = groundY - 44;
  dino.h = 44;
  dino.vy = 0;
  dino.grounded = true;
  dino.duck = false;
  dino.anim = 0;
  state = "running";
  $("overlay").classList.add("hidden");
  lastTime = 0;
  accumulator = 0;
  requestAnimationFrame(loop);
}

function endGame() {
  state = "over";
  burst(dino.x + 20, dino.y + 20, "#00f5ff");

  if (score > best) {
    best = score;
    try { localStorage.setItem("neonDinoBest", best); } catch(e) {}
  }

  $("best").textContent = String(best).padStart(5, "0");
  $("overlayTitle").textContent = "RUN TERMINATED";
  $("overlayText").textContent = "Distance: " + score +
    " points. Every ending is a new beginning.";
  $("startBtn").textContent = "RESTART RUN  →";
  $("overlay").classList.remove("hidden");
}

function jump() {
  if (state === "ready" || state === "over") {
    startGame();
    return;
  }
  if (state === "paused") return;
  if (dino.grounded) {
    dino.vy = -12.5;
    dino.grounded = false;
    dino.duck = false;
    burst(dino.x + 20, groundY - 5, "#00f5ff");
  }
}

function togglePause() {
  if (state === "running") {
    state = "paused";
    $("overlayTitle").textContent = "SYSTEM PAUSED";
    $("overlayText").textContent = "Catch your breath. The desert can wait.";
    $("startBtn").textContent = "RESUME RUN  →";
    $("overlay").classList.remove("hidden");
  } else if (state === "paused") {
    state = "running";
    $("overlay").classList.add("hidden");
    lastTime = 0;
    accumulator = 0;
    requestAnimationFrame(loop);
  }
}

function update() {
  frame++;
  world += speed;
  score += .18;
  speed = Math.min(12, 5 + score / 260);

  dino.anim += .22 + speed * .02;
  dino.h = dino.duck && dino.grounded ? 27 : 44;
  dino.y += dino.vy;
  dino.vy += .62;

  if (dino.y >= groundY - dino.h) {
    dino.y = groundY - dino.h;
    dino.vy = 0;
    dino.grounded = true;
  }

  if (frame % Math.max(34, Math.floor(95 - speed * 4)) === 0) {
    spawnObstacle();
  }

  obstacles.forEach(o => {
    o.x -= speed;
    if (hit(dino, o)) endGame();
  });
  obstacles = obstacles.filter(o => o.x + o.w > -10);

  updateParticles();

  $("score").textContent = String(Math.floor(score)).padStart(5, "0");
  $("speed").textContent = (speed / 5).toFixed(1) + "x";
}

function render() {
  drawBackground();
  obstacles.forEach(drawObstacle);
  drawDino();
  drawParticles();
}

function loop(time) {
  if (state !== "running") {
    render();
    return;
  }

  if (!lastTime) lastTime = time;
  const delta = Math.min(time - lastTime, 50);
  lastTime = time;
  accumulator += delta;

  while (accumulator >= STEP && state === "running") {
    update();
    accumulator -= STEP;
  }

  render();

  if (state === "running") requestAnimationFrame(loop);
}

$("startBtn").addEventListener("click", () => {
  if (state === "paused") togglePause();
  else startGame();
});

document.addEventListener("keydown", e => {
  if (["Space", "ArrowUp", "ArrowDown"].includes(e.code)) {
    e.preventDefault();
  }
  if (e.repeat) return;

  if (e.code === "Space" || e.code === "ArrowUp" || e.code === "KeyW") {
    jump();
  } else if (e.code === "ArrowDown" || e.code === "KeyS") {
    if (state === "running") dino.duck = true;
  } else if (e.code === "Escape") {
    togglePause();
  } else if (e.code === "KeyR") {
    startGame();
  }
});

document.addEventListener("keyup", e => {
  if (e.code === "ArrowDown" || e.code === "KeyS") dino.duck = false;
});

canvas.addEventListener("pointerdown", e => {
  if (state === "running") jump();
  else if (state === "ready" || state === "over") startGame();
});

$("jumpBtn").addEventListener("pointerdown", e => {
  e.preventDefault();
  jump();
});

$("duckBtn").addEventListener("pointerdown", e => {
  e.preventDefault();
  if (state === "running") dino.duck = true;
});

["pointerup", "pointercancel", "pointerleave"].forEach(evt => {
  $("duckBtn").addEventListener(evt, () => dino.duck = false);
});

drawBackground();
drawDino();
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
