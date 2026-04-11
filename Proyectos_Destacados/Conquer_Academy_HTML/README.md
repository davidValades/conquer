# 🎓 Conquer Academy | HTML Semantic Structure

![Status](https://img.shields.io/badge/Estado-En_Desarrollo_🚀-2ea44f?style=for-the-badge)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

Primer proyecto práctico del **Master en Desarrollo Web Full Stack** de ConquerBlocks. Este proyecto se centra exclusivamente en la arquitectura, semántica y estructuración de la información mediante HTML5, sentando bases sólidas antes de introducir la capa de presentación (CSS).

## 🎯 Objetivo del Proyecto

Construir el esqueleto de una plataforma web para una academia online ("Conquer Academy"). El reto principal consiste en estructurar múltiples vistas interconectadas asegurando una navegación lógica, el uso correcto de etiquetas de SEO básico y una accesibilidad semántica estricta.

## ✨ Características Principales y Aprendizajes

- **Estructura Semántica:** Uso riguroso de etiquetas de HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`) para dar significado al contenido más allá de su apariencia.
- **Jerarquía de Contenidos:** Implementación estructurada de niveles de encabezados (`<h1>` a `<h6>`) para mejorar la lectura por parte de navegadores y tecnologías de asistencia.
- **Formularios HTML:** Creación de vistas de Login, Registro y Contacto utilizando los tipos de `input` adecuados (`email`, `password`, `date`, etc.) para una validación nativa.
- **Navegación Relativa:** Sistema de enlaces internos completamente funcional, organizado en una arquitectura de carpetas escalable y profesional.
- **Optimización Base (SEO):** Inclusión de meta etiquetas únicas (`title`, `description`) por página y uso de imágenes responsive.

## 📂 Arquitectura del Proyecto

El proyecto sigue una organización de directorios limpia para separar las vistas por contexto:

```text
conquer-academy-html/
├── assets/                 # Recursos estáticos
│   └── images/             # Imágenes optimizadas y logos
├── pages/                  # Vistas secundarias
│   ├── auth/
│   │   ├── login.html
│   │   └── registro.html
│   ├── blog/
│   │   ├── blog.html
│   │   └── detalle-noticia.html
│   ├── courses/
│   │   ├── cursos.html
│   │   └── detalle-curso.html
│   ├── legal/
│   │   └── aviso-legal.html
│   ├── contacto.html
│   └── quienes-somos.html
├── index.html              # Landing page principal (Home)
└── README.md               # Documentación del proyecto
```

## 🛠️ Tecnologías Utilizadas

- **Estructura:** HTML5 Puro.

- **Entorno:** Visual Studio Code.

- **Control de Versiones:** Git & GitHub.

⭐ Proyecto desarrollado por David Valadés Navarro como parte del currículo de ConquerBlocks.
