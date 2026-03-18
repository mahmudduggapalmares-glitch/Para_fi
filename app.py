import streamlit as st
import streamlit.components.v1 as components

# Configuración de página
st.set_page_config(page_title="Para Ti", layout="wide", initial_sidebar_state="collapsed")

# CSS para limpiar la interfaz de Streamlit y forzar fondo negro
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #000000; }
    iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

# Código HTML/JS mejorado para interactividad táctil
html_final = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; overflow: hidden; background: #000; font-family: 'serif'; color: white; touch-action: manipulation; }
        canvas { position: fixed; top: 0; left: 0; z-index: 1; }
        
        .main-content {
            position: relative; z-index: 5;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            height: 100vh; text-align: center;
            pointer-events: none; /* Permite tocar las estrellas detrás del texto */
        }

        .poem-box { pointer-events: auto; background: rgba(0,0,0,0.4); padding: 20px; border-radius: 20px; }

        /* Estrellas interactivas más grandes para móvil */
        .star-clickable {
            position: absolute; 
            width: 15px; height: 15px; 
            background: radial-gradient(circle, #fff 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%; 
            cursor: pointer; 
            z-index: 10;
            display: flex; align-items: center; justify-content: center;
        }
        .star-inner { width: 4px; height: 4px; background: white; border-radius: 50%; box-shadow: 0 0 10px #fff; }

        #message-display {
            position: fixed; top: 20%; left: 50%; transform: translate(-50%, -50%);
            background: rgba(255,255,255,0.1); backdrop-filter: blur(15px);
            padding: 20px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.3);
            display: none; z-index: 100; text-align: center; width: 80%;
            box-shadow: 0 0 30px rgba(255,255,255,0.1);
        }
    </style>
</head>
<body>
    <canvas id="starCanvas"></canvas>
    <div id="message-display"></div>

    <div class="main-content">
        <div class="poem-box">
            <h1 style="font-weight:100; letter-spacing:4px;">Perdóname</h1>
            <p style="font-style:italic; color:#ccc;">"Fui un tonto por haber dañado nuestro pasado..."</p>
            <p style="font-size: 0.7rem; opacity: 0.5;">Toca las luces que titilan para leer lo que siento</p>
        </div>
    </div>

    <iframe style="display:none" width="0" height="0" 
        src="https://www.youtube.com/embed/soRmpPJOIwo?autoplay=1&loop=1&playlist=soRmpPJOIwo" 
        allow="autoplay">
    </iframe>

    <script>
        const canvas = document.getElementById('starCanvas');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = window.innerWidth;
        let h = canvas.height = window.innerHeight;

        // Estrellas de fondo decorativas
        const bgStars = Array.from({length: 150}, () => ({
            x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.2
        }));

        function draw() {
            ctx.clearRect(0,0,w,h);
            ctx.fillStyle = "white";
            bgStars.forEach(s => {
                ctx.globalAlpha = Math.random() * 0.5 + 0.3;
                ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.fill();
            });
            requestAnimationFrame(draw);
        }
        draw();

        const frases = [
            "Te amo más que a nada en este mundo.",
            "Extraño cada segundo que pasamos juntos.",
            "Me duele el alma haberte fallado.",
            "Eres y serás siempre mi único gran amor.",
            "Daría mi vida por recuperar tu sonrisa.",
            "Perdón por ser un tonto y no valorarte.",
            "Mi corazón te busca en cada estrella."
        ];

        // Crear estrellas interactivas
        frases.forEach((texto) => {
            const container = document.createElement('div');
            container.className = 'star-clickable';
            container.style.top = (Math.random() * 80 + 10) + '%';
            container.style.left = (Math.random() * 80 + 10) + '%';
            
            const dot = document.createElement('div');
            dot.className = 'star-inner';
            container.appendChild(dot);

            container.onclick = (e) => {
                e.stopPropagation();
                const display = document.getElementById('message-display');
                display.innerText = texto;
                display.style.display = 'block';
                setTimeout(() => { display.style.display = 'none'; }, 3000);
            };
            document.body.appendChild(container);
        });
    </script>
</body>
</html>
"""

# Renderizado con altura suficiente para ver todo
components.html(html_final, height=600)

# Carta emocional final (con estilo Streamlit)
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: white; font-weight: 100;'>Mi Carta de Amor</h2>", unsafe_allow_html=True)
st.write(f"""
<div style="text-align: center; color: #bbb; line-height: 1.8; padding: 20px;">
    Escribo esto con el alma en la mano. Te amo con una intensidad que no puedo explicar, 
    y me odio a mí mismo por haber sido el responsable de dañar algo tan puro. 
    <br><br>
    Extraño nuestro pasado, extraño ser tu lugar seguro. Fui un tonto, me equivoqué, 
    y daría lo que fuera por retroceder el tiempo y abrazarte más fuerte. 
    <br><br>
    <b>Eres el amor de mi vida.</b>
</div>
""", unsafe_allow_html=True)

