---
author: Oldhimaster1
avatar: https://avatars.githubusercontent.com/u/179153474?v=4
categories:
- app
color: '#5a635b'
color_bg: '#5a635b'
created: '2026-04-03T20:43:47Z'
description: Interactive OpenStreetMap and satellite map viewer with GPS tracking,
  offline tile caching, place search, and route planning.
download_filter: \.3dsx$
download_page: https://github.com/Oldhimaster1/3ds-Google-Maps/releases
downloads:
  3ds_google_maps.3dsx:
    size: 5349864
    size_str: 5 MiB
    url: https://github.com/Oldhimaster1/3ds-Google-Maps/releases/download/v2.3.1/3ds_google_maps.3dsx
github: Oldhimaster1/3ds-Google-Maps
icon: https://raw.githubusercontent.com/Oldhimaster1/3ds-Google-Maps/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/Oldhimaster1/3ds-Google-Maps/refs/heads/main/banner.png
image_length: 42667
layout: app
license: mit
license_name: MIT License
llm_generation: unknown
source: https://github.com/Oldhimaster1/3ds-Google-Maps
stars: 18
systems:
- 3DS
title: 3ds Google Maps
update_notes: '<h2 dir="auto">What’s new</h2>

  <ul dir="auto">

  <li>Nine interface languages, including Arabic, with 537 translated messages and
  mixed-script font support.</li>

  <li>Optional original ambient music, saved volume controls, mute, audio errors and
  retry.</li>

  <li>Expanded StreetGuess: 113 curated panoramas across 33 countries.</li>

  <li>Progressive panorama detail: loads visible high-resolution tiles as you zoom,
  using about 2 MiB for detail textures.</li>

  </ul>

  <h2 dir="auto">Installation</h2>

  <p dir="auto">Install the CIA using FBI, or copy the 3DSX to:<br>

  sdmc:/3ds/3ds_google_maps/3ds_google_maps.3dsx</p>

  <p dir="auto">Back up application data before upgrading. Verify downloads against
  SHA256SUMS.</p>

  <h2 dir="auto">Testing</h2>

  <p dir="auto">35 host suite entries passed. CIA installation, all nine languages,
  volume controls and saved settings were checked in Azahar.</p>

  <p dir="auto">Physical-console audio and performance remain unverified. Live imagery
  availability varies. Tiled HD currently applies to the Google provider; Panoramax
  retains SD imagery. Friend codes require matching dataset versions.</p>'
updated: '2026-11-17T01:51:26Z'
version: v2.3.1
version_title: Maps for Nintendo 3DS v2.3.1 — Languages, Music & Expanded StreetGuess
---
Interactive map viewer for Nintendo 3DS. Browse OpenStreetMap street tiles and Esri satellite imagery, track your GPS location through your phone, search for places, plan routes, and save favorites.

**Features:**
- Pan and zoom maps on both screens (touch, D-pad, Circle Pad, L/R)
- Three tile sources: OpenStreetMap, Esri Satellite, Esri Street Map
- Offline tile caching — download regions on your PC and transfer as a single .tilepack file
- GPS tracking via phone browser (3DS runs an HTTPS server, phone sends coordinates)
- Place search, route planning, reverse geocoding, favorites
- Night mode, tile prefetching, SD card tile cache

**Offline caching (new in v2.0):**
Use the included Python tool to bulk-download tiles for any region. Transfers as one file instead of thousands of PNGs. Works completely without WiFi.

**GPS phone bridge:**
The 3DS starts a TLS server and shows a QR code. Scan it with your phone, allow location access, and your position streams to the 3DS in real time. On iPhone, use Chrome instead of Safari.

Requires WiFi for live tile downloads and GPS. Offline tilepacks work without any network.