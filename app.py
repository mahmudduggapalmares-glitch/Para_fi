import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página para que se vea bien en móviles y PC
st.set_page_config(page_title="Para el amor de mi vida", layout="wide", initial_sidebar_state="collapsed")

# Inyectamos el CSS directamente para limpiar la interfaz de Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body { background-color: #000000; }
    .stApp { background-color: #000000; }
    </style>
""", unsafe_allow_html=True)

# El bloque de HTML, CSS y JS todo en uno
html_final = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { margin: 0; overflow: hidden; background: #000; font-family: 'Georgia', serif; color: white; }
        canvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; }
        .main-container {
            position: relative; z-index: 10;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            height: 100vh; text-align: center;
            padding: 20px;
            background: radial-gradient(circle, rgba(0,0,0,0) 30%, rgba(0,0,0,0.8) 100%);
        }
        .poem-box { 
            animation: fadeIn 5s ease-in; 
            max-width: 600px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        h1 { font-weight: 100; letter-spacing: 6px; margin-bottom: 20px; }
        p { font-style: italic; line-height: 1.8; font-size: 1.1rem; color: #ccc; }
        
        .star-clickable {
            position: absolute; width: 4px; height: 4px; background: white;
            border-radius: 50%; cursor: pointer; box-shadow: 0 0 10px #fff;
            transition: transform 0.3s;
        }
        .star-clickable:hover { transform: scale(3); }

        #toast {
            position: fixed; bottom: 10%; left: 50%; transform: translateX(-50%);
            background: rgba(255,255,255,0.1); backdrop-filter: blur(10px);
            padding: 15px 25px; border-radius: 30px; display: none;
            z-index: 100; font-size: 0.9rem; border: 0.5px solid rgba(255,255,255,0.2);
        }

        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>
    <canvas id="starCanvas"></canvas>
    
    <div class="main-container">
        <div class="poem-box">
            <h1>Perdóname</h1>
            <p>
                Éramos dos almas bailando en la oscuridad,<br>
                y yo, en mi ceguera, solté tu mano.<br>
                Extraño el eco de tu voz y la paz de tu mirada,<br>
                fui un tonto al romper el cristal de lo humano.
            </p>
            <p style="font-size: 0.8rem; margin-top: 30px; opacity: 0.6;">
                (Hay mensajes ocultos en las estrellas que brillan más...)
            </p>
        </div>
    </div>

    <div id="toast"></div>

    <iframe style="display:none" width="0" height="0" 
        src="https://www.youtube.com/embed/soRmpPJOIwo?autoplay=1&loop=1&playlist=soRmpPJOIwo" 
        frameborder="0" allow="autoplay">
    </iframe>

    <script>
        const canvas = document.getElementById('starCanvas');
        const ctx = canvas.getContext('2d');
        let w, h;
        
        function setCanvasSize() {
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', setCanvasSize);
        setCanvasSize();

        const stars = Array.from({length: 250}, () => ({
            x: Math.random() * w,
            y: Math.random() * h,
            size: Math.random() * 1.5,
            speed: Math.random() * 0.05
        }));

        function animate() {
            ctx.clearRect(0,0,w,h);
            ctx.fillStyle = "white";
            stars.forEach(s => {
                ctx.globalAlpha = Math.random() * 0.5 + 0.5;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.size, 0, Math.PI*2);
                ctx.fill();
            });
            requestAnimationFrame(animate);
        }
        animate();

        const frases = [
            "Te extraño en cada silencio.",
            "Fui un tonto por no valorar lo que teníamos.",
            "Eres el amor de mi vida, ayer y hoy.",
            "Daría lo que fuera por volver a verte reír.",
            "Te amo más de lo que las palabras pueden decir."
        ];

        frases.forEach(texto => {
            const s = document.createElement('div');
            s.className = 'star-clickable';
            s.style.top = (Math.random() * 70 + 15) + '%';
            s.style.left = (Math.random() * 70 + 15) + '%';
            s.onclick = () => {
                const t = document.getElementById('toast');
                t.innerText = texto;
                t.style.display = 'block';
                setTimeout(() => t.style.display = 'none', 3000);
            };
            document.body.appendChild(s);
        });
    </script>
</body>
</html>
"""

# Renderizamos el HTML
components.html(html_final, height=700, scrolling=False)

# Carta final debajo
st.markdown("<div style='text-align: center; color: #888; padding: 20px;'>", unsafe_allow_html=True)
st.write("---")
st.write("### Mi Carta para Ti")
st.write("""
Escribo esto con el alma rota pero con una certeza absoluta: **Te amo**. 
Me tomó perderte para entender que eres la luz que guiaba mis pasos. 
Fui débil, fui tonto y dañé lo que más quería proteger. 

No espero que esto lo arregle todo al instante, pero quiero que sepas que sigo aquí, 
extrañando ese pasado juntos y deseando haber hecho las cosas de otra manera. 
Eres el amor de mi vida.
""")
st.markdown("</div>", unsafe_allow_html=True)

