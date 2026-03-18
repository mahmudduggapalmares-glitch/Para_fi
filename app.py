<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Ti</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #050505;
            font-family: 'Georgia', serif;
            color: white;
        }

        /* Fondo de vacío con estrellas */
        #canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: 0;
        }

        .container {
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
            background: radial-gradient(circle, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%);
        }

        .letter-content {
            max-width: 600px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(5px);
            border-radius: 15px;
            animation: fadeIn 5s ease-in;
        }

        h1 { font-weight: lighter; letter-spacing: 5px; opacity: 0.8; }
        p { line-height: 1.6; font-size: 1.1rem; color: #ddd; }

        /* Estrellas con notas (Interactivas) */
        .star-note {
            position: absolute;
            width: 4px;
            height: 4px;
            background: white;
            border-radius: 50%;
            cursor: pointer;
            box-shadow: 0 0 10px white;
            transition: transform 0.3s;
        }

        .star-note:hover { transform: scale(2); }

        /* Música oculta (YouTube) */
        #music-container {
            position: fixed;
            bottom: -100px;
        }

        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        .hidden-message {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,0.9);
            padding: 20px;
            border: 1px solid #444;
            display: none;
            z-index: 10;
        }
    </style>
</head>
<body>

    <canvas id="canvas"></canvas>

    <div class="container">
        <div class="letter-content">
            <h1>Perdóname</h1>
            <p><i>"Fui un tonto por romper lo más puro que tenía..."</i></p>
            <br>
            <p>
                Te extraño en el silencio de cada noche. Extraño ese pasado donde éramos uno solo, 
                donde el mundo no importaba porque te tenía a mi lado. Me duele saber que fui yo 
                quien dañó este camino, y daría lo que fuera por volver a verte sonreír sin miedos.
            </p>
            <p>Te amo, más allá del tiempo y del error.</p>
        </div>
    </div>

    <div id="music-container">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/soRmpPJOIwo?autoplay=1&loop=1&playlist=soRmpPJOIwo" frameborder="0" allow="autoplay"></iframe>
    </div>

    <div id="msg-box" class="hidden-message"></div>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        let stars = [];

        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }

        window.addEventListener('resize', resize);
        resize();

        // Crear estrellas de fondo
        for(let i = 0; i < 200; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 1.5,
                opacity: Math.random()
            });
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            stars.forEach(s => {
                ctx.fillStyle = `rgba(255, 255, 255, ${s.opacity})`;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
                ctx.fill();
            });
            requestAnimationFrame(draw);
        }
        draw();

        // Estrellas con mensajes ocultos
        const mensajes = [
            "Eres el recuerdo más lindo de mi vida.",
            "Nadie podrá ocupar tu lugar jamás.",
            "Perdón por no saber cuidarte.",
            "Aún guardo tu risa en mi memoria.",
            "Te sigo amando en cada estrella que veo."
        ];

        mensajes.forEach((m, i) => {
            let star = document.createElement('div');
            star.className = 'star-note';
            star.style.top = Math.random() * 80 + 10 + '%';
            star.style.left = Math.random() * 80 + 10 + '%';
            star.onclick = () => {
                const box = document.getElementById('msg-box');
                box.innerText = m;
                box.style.display = 'block';
                setTimeout(() => box.style.display = 'none', 3000);
            };
            document.body.appendChild(star);
        });
    </script>
</body>
</html>

