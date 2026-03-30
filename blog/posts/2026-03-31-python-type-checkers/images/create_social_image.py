"""Create a 2x2 social image compositing four Python type checker logos."""

import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(
    "/Users/austin/repos/positron-website"
    "/blog/posts/2026-03-25-python-type-checkers/social.png"
)

# --- Logo SVG sources ---

TY_SVG = '''<svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="100" height="100" rx="20" fill="#261230"/>
<path d="M70 36.4H53.2V30H33.2V36.4H30V51.6H33.2V62.2136C33.2 66.5139 36.6861 70 40.9864 70H70V54.8H53.2V51.6H62.2136C66.5139 51.6 70 48.1139 70 43.8136V36.4Z" fill="#46EBE1"/>
</svg>'''

PYREFLY_SVG = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 489.36 386.49">
<defs>
<style>
  .pf1{fill:url(#pf-lg2);}
  .pf2{fill:url(#pf-lg1);}
  .pf3{fill:#394048;}
</style>
<linearGradient id="pf-lg1" x1="244.69" y1="178.14" x2="244.69" y2="77.23" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#bdc5cf"/><stop offset="1" stop-color="#6d737a"/></linearGradient>
<linearGradient id="pf-lg2" x1="243.99" y1="356.44" x2="243.99" y2="129.44" gradientUnits="userSpaceOnUse"><stop offset=".15" stop-color="#ff4602"/><stop offset=".85" stop-color="#ff9a00"/></linearGradient>
</defs>
<path class="pf2" d="M244.69,77.23l-169.28,82.08c62.43,38.76,112.53,9.97,141.57-17.49.02-.04.04-.06.06-.06,17.19-16.29,27-32.09,27.61-33.08.02-.04.04-.06.04-.06,0,0,.02.02.04.06.61.99,10.42,16.79,27.61,33.08.02,0,.04.02.06.06,29.04,27.46,79.14,56.25,141.57,17.49l-169.28-82.08Z"/>
<path class="pf3" d="M281.4,73.52v-5.87c0-20.77-16.83-37.6-37.6-37.6s-37.6,16.83-37.6,37.6v5.48L30.98,33.84c12.79,42.15,47.26,76.4,93.32,86.73,30.47,6.82,60.85,2.02,86.46-11.49,4.4-2.31,8.67-4.88,12.77-7.7l21.13-14.16,21.13,14.16c.4.28.82.52,1.23.79,1.34.9,2.69,1.77,4.06,2.62.6.37,1.2.73,1.8,1.09,1.7,1.01,3.43,1.98,5.18,2.92.17.09.33.19.5.28h0c25.63,13.5,56.01,18.32,86.49,11.49,46.06-10.33,80.53-44.58,93.32-86.72l-176.98,39.68Z"/>
<path class="pf1" d="M268.84,311.09c-4.54,5.93-7.79,9.45-8.14,9.81.29-25.86-3.51-34.7-16.86-50.02-.04-.02-.08-.02-.11-.04-24.56,42.71-16.79,82.38-16.14,85.41,0,.04.04.08.04.1.02.06.02.1.02.1-32.32-50.92-42.72-90.71-41.77-121.35.21-7.15,1.31-13.78,2.36-20.01,2.73-16.39,10.12-29.8,18.69-40.38.46-.55.93-1.11,1.39-1.68l36.36-43.58,37.66,45.13,1.62,1.94c11,13.63,16.27,27.96,17.76,42.11,4.04,38.38-19.8,75.37-32.87,92.46Z"/>
</svg>'''

ZUBAN_SVG = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 253.11 226.62">
  <defs>
    <style>
      .z1 { fill: none; }
      .z12 { fill: url(#zgs); }
      .z17 { fill: url(#zgsc2); }
      .z14 { fill: url(#zlg); }
      .z11 { fill: url(#zlg2); }
      .z28 { fill: url(#zgs2); }
      .z27 { fill: url(#zgs3); }
      .z10 { fill: url(#zlg3); }
      .z9 { fill: url(#zlg4); }
      .z6 { fill: url(#zlg5); }
      .z7 { fill: url(#zlg6); }
      .z5 { fill: url(#zlg7); }
      .z30 { fill: url(#zgsc); }
      .z4 { fill: url(#zlg8); }
      .z25 { fill: url(#zgs4); }
      .z8 { fill: url(#zlg9); }
      .z18 { fill: url(#zlg10); }
      .z29 { fill: url(#zgs3a); }
      .z23 { fill: url(#zgs5); }
      .z19 { fill: url(#zlg11); }
      .z31 { clip-path: url(#zcp); }
      .z2 { fill: url(#zgs3b); }
      .z20 { fill: url(#zlg12); }
      .z26 { fill: url(#zgs6); }
      .z24 { fill: url(#zgs7); }
      .z21 { fill: url(#zlg13); }
      .z15 { clip-path: url(#zcp1); }
      .z16 { clip-path: url(#zcp2); }
      .z22 { fill: url(#zlg14); }
      .z13 { fill: url(#zrg); }
      .z3 { fill: #fff5d7; }
    </style>
    <linearGradient id="zgs" x1="181.28" y1="83.8" x2="193.53" y2="118.18" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <linearGradient id="zgsc2" x1="114.39" y1="150.47" x2="42.64" y2="228.81" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3c0030"/><stop offset=".11" stop-color="#63004c"/><stop offset=".89" stop-color="#e1141e"/>
    </linearGradient>
    <linearGradient id="zlg" x1="196.87" y1="121.19" x2="109.64" y2="212.78" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zlg2" x1="95.69" y1="112.78" x2="26.33" y2="36.24" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f52d0f"/><stop offset=".68" stop-color="#ff9119"/><stop offset="1" stop-color="#ffa000"/>
    </linearGradient>
    <linearGradient id="zgs2" x1="33.47" y1="44.65" x2="109.67" y2="135.15" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <linearGradient id="zgs3" x1="207.34" y1="210.92" x2="189.4" y2="183.57" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <clipPath id="zcp">
      <path class="z1" d="M252.69,158.16c-1.72-3.72-10.3-21.37-24.52-33.04-37.68-30.93-71.12-13.14-71.12-13.14-64.55-11.81-89.36,26.01-89.36,26.01h0l-21.6,25.42L3.94,213.02l39.6-24.74c12.1-6.06,14.06,9.05,35.14-1.27,8.56-4.19,18.05-12.74,26.31-21.41,32.21,22.93,77.77,53.04,105.24,61.02-.39-.4-37.28-38.03-21.22-49.33,16.15-11.36,30.25,14.72,49.63-.3,5.98-4.63,16.74-13.01,14.05-18.84Z"/>
    </clipPath>
    <linearGradient id="zlg3" x1="-256.85" y1="384.04" x2="-407.78" y2="360.03" gradientTransform="translate(518.59 -280.74) rotate(-11.94) scale(1.47 1)" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ffa000"/><stop offset=".14" stop-color="#ff8d19"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zlg4" x1="190.72" y1="190.08" x2="59.17" y2="169.16" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zlg5" x1="261.06" y1="136.13" x2="98.12" y2="162.74" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zlg6" x1="116.76" y1="130.41" x2="278.16" y2="138.14" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zlg7" x1="61.72" y1="155.13" x2="143.05" y2="115.07" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f52d0f"/><stop offset="1" stop-color="#ff9119"/>
    </linearGradient>
    <linearGradient id="zgsc" x1="225.62" y1="176.69" x2="250.48" y2="152.78" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zlg8" x1="161.33" y1="147.04" x2="252.95" y2="201.22" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zgs4" x1="120.98" y1="111.88" x2="172.7" y2="111.88" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <linearGradient id="zlg9" x1="179.49" y1="164.69" x2="201.69" y2="190.7" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#63004c"/><stop offset="1" stop-color="#e1141e"/>
    </linearGradient>
    <linearGradient id="zlg10" x1="200.46" y1="220.32" x2="52.17" y2="127.03" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f52d0f"/><stop offset="1" stop-color="#ff9119"/>
    </linearGradient>
    <linearGradient id="zgs3a" x1="-26.12" y1="206.84" x2="100.12" y2="206.84" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#c93109"/><stop offset="1" stop-color="#ff0700"/>
    </linearGradient>
    <linearGradient id="zgs5" x1="113.74" y1="176.69" x2="111.18" y2="148.76" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <linearGradient id="zlg11" x1="18.35" y1="156.06" x2="28.44" y2="204.72" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <clipPath id="zcp1">
      <path class="z1" d="M78.68,187.01c21.08-10.32,47.84-47.09,47.84-47.09l-73.66,20.74-6.77,2.75L3.94,213.02l39.6-24.74c12.1-6.06,14.06,9.05,35.14-1.27Z"/>
    </clipPath>
    <linearGradient id="zgs3b" x1="68.96" y1="158.91" x2="109.02" y2="194.79" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#c93109"/><stop offset="1" stop-color="#ff0700"/>
    </linearGradient>
    <linearGradient id="zlg12" x1="18.35" y1="156.06" x2="28.44" y2="204.72" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <linearGradient id="zgs6" x1="243.88" y1="169.65" x2="248.81" y2="159.79" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <linearGradient id="zgs7" x1="248.56" y1="156.5" x2="242.73" y2="193.87" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e1141e"/><stop offset="1" stop-color="#63004c"/>
    </linearGradient>
    <linearGradient id="zlg13" x1="133.81" y1="85.83" x2="208.71" y2="142.34" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff9119"/><stop offset="1" stop-color="#f52d0f"/>
    </linearGradient>
    <clipPath id="zcp2">
      <path class="z1" d="M199.43,117.59c-17.54-15.17-44.26-23.69-57.79-27.27-3.69-.97-6.9,2.77-5.32,6.24,11.81,25.92,32.85,30.19,36.38,30.74,6-3.05,14.82-6.72,26.73-9.71Z"/>
    </clipPath>
    <linearGradient id="zlg14" x1="144.72" y1="114" x2="170.91" y2="105.64" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff4f00"/><stop offset=".19" stop-color="#fd4a02"/><stop offset=".4" stop-color="#f93c07"/><stop offset=".56" stop-color="#f52d0f"/><stop offset=".99" stop-color="#c40036"/>
    </linearGradient>
    <radialGradient id="zrg" cx="202.32" cy="137.67" fx="202.32" fy="137.67" r="38.61" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3c0030"/><stop offset=".19" stop-color="#63004c"/><stop offset=".84" stop-color="#e1141e"/>
    </radialGradient>
  </defs>
  <g>
    <g>
      <path class="z12" d="M181.8,110.83c-10-5.25-16.69-16.84-20.21-24.51-1.45-3.15,1.51-6.55,4.83-5.57,42.86,12.61,53.17,53.13,53.17,53.13l-37.79-23.04Z"/>
      <path class="z17" d="M73.97,167.71l-13.67,7.16-16.92,37.75,30.64-16.66c11.45-7.2,14.69,4.39,34.68-7.92,8.11-5,16.73-14.42,24.11-23.86l-39.79-23.87-19.04,27.39"/>
      <path class="z14" d="M252.69,158.16c-1.72-3.72-10.3-21.37-24.52-33.04-37.68-30.93-71.12-13.14-71.12-13.14-64.55-11.81-89.36,26.01-89.36,26.01h0l-21.6,25.42L3.94,213.02l39.6-24.74c12.1-6.06,14.06,9.05,35.14-1.27,8.56-4.19,18.05-12.74,26.31-21.41,32.21,22.93,77.77,53.04,105.24,61.02-.39-.4-37.28-38.03-21.22-49.33,16.15-11.36,30.25,14.72,49.63-.3,5.98-4.63,16.74-13.01,14.05-18.84Z"/>
      <polygon class="z11" points="144.18 110.14 96.4 96.41 105.5 68.56 3.27 0 39.56 70.2 0 62.1 69.41 139.92 144.18 110.14"/>
      <path class="z28" d="M36.44,40.87c1.27.85,53.78,35.61,53.78,35.61l-8.93,25.02,33.76,14.21-33.01,13.57c-.08.04-.17.02-.23-.04l-39.73-38.79,21.72-3.11c.1-.04-27.36-46.47-27.36-46.47Z"/>
      <path class="z27" d="M192.44,151.95c.67.45,6.16,18.36,37.52,61.07,0,0-28.78,1.21-77.14-48.96l39.62-12.1Z"/>
      <path class="z14" d="M252.69,158.16c-1.72-3.72-10.3-21.37-24.52-33.04-37.68-30.93-71.12-13.14-71.12-13.14-64.55-11.81-89.36,26.01-89.36,26.01h0l-21.6,25.42L3.94,213.02l39.6-24.74c12.1-6.06,14.06,9.05,35.14-1.27,8.56-4.19,18.05-12.74,26.31-21.41,32.21,22.93,77.77,53.04,105.24,61.02-.39-.4-37.28-38.03-21.22-49.33,16.15-11.36,30.25,14.72,49.63-.3,5.98-4.63,16.74-13.01,14.05-18.84Z"/>
      <g class="z31">
        <path class="z10" d="M102.52,132.16s41.67,50.32,112.87,98.51l56.36-84.64s-122.31-33.16-169.22-13.87Z"/>
        <path class="z9" d="M118.99,149.6s6.24,18.44,91.24,77.02l7.8-53.07s-34.49-27.01-99.04-23.95Z"/>
        <path class="z6" d="M172.7,127.3l-18.23,9.94c42.97,6.72,88.05,25.19,88.05,25.19-1.09-7.15-20.86-38.19-69.83-35.13Z"/>
        <path class="z7" d="M242.52,162.43c-2.24-1.14-24.14-27.8-69.83-35.13,0,0-36.9-16.06-2.37-21.88,44.42-7.5,97.52,44.58,95.28,55.25s-23.09,1.77-23.09,1.77Z"/>
        <path class="z5" d="M46.09,163.41s62.99-63.54,126.61-36.11l-33.61-25.32s-61.07-4.93-92.99,61.43Z"/>
        <path class="z30" d="M244.2,165.6c-4.45,9.47-22.31,12.16-31.21,4.74,0,0,17.2,12.86,23.63,12.16s13.16-14,13.16-14l-5.57-2.89Z"/>
        <path class="z4" d="M173.67,164.84s38.8,28.69,51.8,25.1c12.16-3.36,10.94-10.31,10.17-10.91-11.52,2.71-17.58-8.16-30.46-12.27-14.16-4.51-31.51-1.92-31.51-1.92Z"/>
        <path class="z25" d="M172.7,127.3s-36.7,2.76-51.72-30.87c0,0,27.5-1.87,51.72,30.87"/>
        <path class="z8" d="M214.33,179.2s-11.6-11.04-22.94-13.14c-10.3-1.91-17.72-1.22-17.72-1.22-1.67,1.51,3.37,18.23,7.92,26.67,5.85,10.82,11.93,14.65,11.93,14.65l20.8-26.96Z"/>
        <path class="z18" d="M210.23,226.62s-78.86-57.41-91.24-77.02l-14.61,23.52s49.71,51.87,105.85,53.5Z"/>
        <path class="z29" d="M81.56,179.04c10.57-3.8,18.56-8.61,18.56-8.61l-32.64,61.1-20.36,11.73-73.26-37.48,69.5-29.31c15.91-5,10.94,12.37,38.18,2.57Z"/>
        <polygon class="z23" points="104.99 165.6 106.25 178.05 118.99 149.6 104.99 165.6"/>
      </g>
      <polygon class="z19" points="31.8 169.21 3.94 213.02 46.09 163.41 31.8 169.21"/>
      <g class="z15">
        <path class="z2" d="M91.01,173.27c-28.97,20.56-40.84,13.57-40.84,13.57l5.26,14.08h54.56l9-51.33c-16.03,12.31-22.53,19.03-27.99,23.67Z"/>
      </g>
      <polygon class="z20" points="31.8 169.21 3.94 213.02 46.09 163.41 31.8 169.21"/>
      <path class="z26" d="M247.78,169.21c3.44-3.47,6-7.2,5.17-10.32-3.13.24-8.2.89-10.23,2.71-.97.87,1.49,4.79,5.06,7.61Z"/>
      <path class="z24" d="M252.95,158.9c-3.13.24-8.2.89-10.23,2.71-.19.17-.25.45-.19.82,1.61-.4,5.46-1.17,10.42-.98.2-.88.22-1.73,0-2.55Z"/>
      <path class="z21" d="M199.43,117.59c-17.54-15.17-44.26-23.69-57.79-27.27-3.69-.97-6.9,2.77-5.32,6.24,11.81,25.92,32.85,30.19,36.38,30.74,6-3.05,14.82-6.72,26.73-9.71Z"/>
      <g class="z16">
        <path class="z22" d="M183.24,122.76c-1.08-4.92-8.2-19.7-40.15-29.62-2.56-.79-4.89,1.74-3.84,4.17,10.53,24.4,31.77,28.75,35.05,29.24,2.48-1.24,5.38-2.43,8.95-3.79Z"/>
      </g>
      <path class="z13" d="M231.05,152.39l-4.94-2.28c-1.95,2.41-4.84,4.06-8.18,4.34-6.5.54-12.21-4.29-12.74-10.79-.17-2.08.22-4.06,1.03-5.83l-6.09-3.1s7.47-4.83,17.5.89,13.43,16.78,13.43,16.78Z"/>
      <path class="z3" d="M216.28,142.58c-.47.18-.92.68-1.09,1.26-.56,1.88.08,3.84,1.64,4.68,1.28.68,2.83.43,4.04-.51.89-.69,1.34-2.06.97-2.91-.28-.64-.78-1.42-1.68-2.15-1.34-1.09-2.97-.72-3.89-.37Z"/>
      <path class="z3" d="M209.36,144.1c-.48.97.14,2.09,1.18,2.39.55.16,1.1.09,1.5-.24.38-.31.55-.8.53-1.33-.05-1.12-1.15-1.94-2.21-1.59-.13.04-.26.1-.39.16-.29.15-.48.37-.6.61Z"/>
    </g>
  </g>
</svg>'''

# basedpyright: extract dominant color from the logo PNG, recreate as SVG
bp_img = Image.open("/tmp/basedpyright_logo.png").convert("RGB")
colors: dict[tuple[int, int, int], int] = {}
for x in range(bp_img.width):
    for y in range(bp_img.height):
        r, g, b = bp_img.getpixel((x, y))
        if r > 150 and g > 100 and b < 100:
            key = (r, g, b)
            colors[key] = colors.get(key, 0) + 1
dominant = max(colors, key=colors.get) if colors else (239, 170, 31)
hex_color = f"#{dominant[0]:02x}{dominant[1]:02x}{dominant[2]:02x}"
print(f"basedpyright color: {hex_color}")

BASEDPYRIGHT_SVG = f'''<svg viewBox="0 0 82 22" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="22" height="22" rx="1" fill="{hex_color}"/>
  <rect x="30" y="0" width="22" height="22" rx="1" fill="{hex_color}"/>
  <rect x="60" y="0" width="22" height="22" rx="1" fill="{hex_color}"/>
</svg>'''


def svg_to_png(svg_string: str, width: int) -> Image.Image:
    """Convert SVG string to PIL Image using rsvg-convert."""
    with tempfile.NamedTemporaryFile(suffix=".svg", mode="w") as svg_f:
        svg_f.write(svg_string)
        svg_f.flush()
        with tempfile.NamedTemporaryFile(suffix=".png") as png_f:
            subprocess.run(
                [
                    "rsvg-convert",
                    "-w", str(width),
                    "-f", "png",
                    "-o", png_f.name,
                    svg_f.name,
                ],
                check=True,
            )
            return Image.open(png_f.name).copy().convert("RGBA")


# Canvas: 1200x630 (OG image standard)
W, H = 1200, 630
CELL_W, CELL_H = W // 2, H // 2
PAD = 60

logo_size = min(CELL_W, CELL_H) - 2 * PAD

pyrefly_img = svg_to_png(PYREFLY_SVG, logo_size)
ty_img = svg_to_png(TY_SVG, logo_size)
bp_img_rendered = svg_to_png(BASEDPYRIGHT_SVG, logo_size)
zuban_img = svg_to_png(ZUBAN_SVG, logo_size)

print(f"pyrefly: {pyrefly_img.size}")
print(f"ty: {ty_img.size}")
print(f"basedpyright: {bp_img_rendered.size}")
print(f"zuban: {zuban_img.size}")

canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
draw = ImageDraw.Draw(canvas)

# Grid lines and border (same style)
line_color = (220, 220, 220, 255)
line_width = 2
corner_radius = 12
draw.line([(W // 2, 0), (W // 2, H)], fill=line_color, width=line_width)
draw.line([(0, H // 2), (W, H // 2)], fill=line_color, width=line_width)
draw.rounded_rectangle(
    [(0, 0), (W - 1, H - 1)],
    radius=corner_radius,
    outline=line_color,
    width=line_width,
)


def paste_centered(
    canvas: Image.Image, logo: Image.Image, cell_x: int, cell_y: int
) -> None:
    x = cell_x + (CELL_W - logo.width) // 2
    y = cell_y + (CELL_H - logo.height) // 2
    canvas.paste(logo, (x, y), logo)


# pyrefly=top-left, ty=top-right, basedpyright=bottom-left, zuban=bottom-right
paste_centered(canvas, pyrefly_img, 0, 0)
paste_centered(canvas, ty_img, CELL_W, 0)
paste_centered(canvas, bp_img_rendered, 0, CELL_H)
paste_centered(canvas, zuban_img, CELL_W, CELL_H)

canvas.convert("RGB").save(str(OUT), "PNG", optimize=True)
print(f"Saved to {OUT}")
print(f"Size: {canvas.width}x{canvas.height}")
