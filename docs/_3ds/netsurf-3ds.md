---
author: Coderman64
avatar: https://avatars.githubusercontent.com/u/12971494?v=4
categories:
- utility
- app
color: '#64aae4'
color_bg: '#385f80'
created: '2024-02-09T20:16:17Z'
description: homebrew web browser port for the Nintendo 3DS
download_page: https://github.com/coderman64/netsurf-3ds/releases
downloads:
  nsfb.3dsx:
    size: 20878700
    size_str: 19 MiB
    url: https://github.com/coderman64/netsurf-3ds/releases/download/v0.03/nsfb.3dsx
  nsfb.cia:
    size: 19661760
    size_str: 18 MiB
    url: https://github.com/coderman64/netsurf-3ds/releases/download/v0.03/nsfb.cia
  nsfb_himem.cia:
    size: 19661760
    size_str: 18 MiB
    url: https://github.com/coderman64/netsurf-3ds/releases/download/v0.03/nsfb_himem.cia
github: coderman64/netsurf-3ds
icon: https://raw.githubusercontent.com/coderman64/netsurf-3ds/9934ab977eb9edf51324ba498b979511925d7a4d/netsurf/Logo.png
image: https://raw.githubusercontent.com/coderman64/netsurf-3ds/refs/heads/main/netsurf/banner_image.png
image_length: 17224
layout: app
license: none
llm_generation: 'no'
qr:
  nsfb.cia: https://db.universal-team.net/assets/images/qr/nsfb-cia.png
  nsfb_himem.cia: https://db.universal-team.net/assets/images/qr/nsfb_himem-cia.png
script_message: this web browser will run slow for most websites but better than the
  normal 3ds browser.
source: https://github.com/coderman64/netsurf-3ds
stars: 187
systems:
- 3DS
title: netsurf-3ds
unique_ids:
- '0xFD3FF'
update_notes: '<h2 dir="auto">Changelog</h2>

  <p dir="auto">There are a few updates in this release:</p>

  <ol dir="auto">

  <li><strong>RomFS Support</strong> - resources will now be loaded from the app''s
  own RomFS instead of from <code class="notranslate">/share/netsurf</code> on your
  SD card, meaning no more confusing zipfile extraction!</li>

  <li><strong>CIA support</strong> - NetSurf now has two CIA builds - <code class="notranslate">nsfb.cia</code>
  is the normal browser, while <code class="notranslate">nsfb_himem.cia</code> uses
  the 3DS''s extended memory mode, allowing NetSurf to use 80MB of memory instead
  of 64MB, at the cost of longer boot times.</li>

  </ol>

  <h2 dir="auto">QR Download Link</h2>

  <p dir="auto">Use this QR code to install via FBI:</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/eb57f5ed-98b4-475a-970f-fb1e74674a49"><img
  width="220" height="220" alt="nsfb_cia_download_qr" src="https://github.com/user-attachments/assets/eb57f5ed-98b4-475a-970f-fb1e74674a49"
  style="max-width: 100%; height: auto; max-height: 220px;; aspect-ratio: 220 / 220;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>'
updated: '2025-12-23T18:56:22Z'
version: v0.03
version_title: CIA and RomFS support
---
Netsurf 3DS
Work in progress homebrew 3DS port of the lightweight NetSurf web browser.