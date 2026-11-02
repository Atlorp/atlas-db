---
author: mockmodular
avatar: https://avatars.githubusercontent.com/u/85780766?v=4
categories:
- app
- media
color: '#425254'
color_bg: '#425254'
created: '2026-04-08T13:03:39Z'
description: ' topos — True SBS 3D (and normal 2D) Video Player for 3DS | RGB888,
  MVD Hardware Decode, Smooth & Clean '
download_filter: (3dsx|cia)
download_page: https://github.com/mockmodular/topos_3ds-video-player/releases
downloads:
  topos.cia:
    size: 9974720
    size_str: 9 MiB
    url: https://github.com/mockmodular/topos_3ds-video-player/releases/download/0.12.3.3/topos.cia
github: mockmodular/topos_3ds-video-player
icon: https://raw.githubusercontent.com/mockmodular/topos_3ds-video-player/main/resource/icon.png
image: https://raw.githubusercontent.com/mockmodular/topos_3ds-video-player/main/resource/icon.png
image_length: 5767
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  topos.cia: https://db.universal-team.net/assets/images/qr/topos-cia.png
source: https://github.com/mockmodular/topos_3ds-video-player
stars: 18
systems:
- 3DS
title: topos_3ds-video-player
update_notes: '<h2 dir="auto">Changes</h2>

  <h3 dir="auto">Remove redundant texture cache flushes across all playback paths</h3>

  <ul dir="auto">

  <li>Remove the remaining 12 per-texture cache flush calls across hardware decoding,
  software decoding, AV1, 2D, and SBS 3D playback.</li>

  <li>Remove the MPEG-2-specific condition from the Y2R x2 SBS path so all codecs
  on that path use the same behavior.</li>

  <li>Retain the final whole-linear-memory cache flush before GPU execution and the
  existing intermediate DMA cache handling.</li>

  </ul>

  <h3 dir="auto">Check MVD availability before hardware initialization</h3>

  <ul dir="auto">

  <li>Check whether the actual <code class="notranslate">mvd:STD</code> service is
  registered before allocating MVD buffers or requesting the service, including during
  initialization after a seek.</li>

  <li>If the service is absent or the availability query fails, return immediately
  and let the existing logic fall back to software decoding. This prevents an Old
  3DS with fake model mode enabled from waiting indefinitely for a New 3DS-only service.</li>

  <li>Preserve the <code class="notranslate">sw</code> / <code class="notranslate">hw(auto)</code>
  selection and fake model settings.</li>

  </ul>

  <h3 dir="auto">Lowercase UI text and improve status readability</h3>

  <ul dir="auto">

  <li>Use lowercase menu options and hard-coded UI/status labels.</li>

  <li>Display FFmpeg''s short video/audio codec names instead of their long names,
  and use <code class="notranslate">k</code> for memory readings.</li>

  <li>Display the complete <code class="notranslate">sbs:0/1</code> and <code class="notranslate">3d:0/1</code>
  indicators in the same white as the resolution and frame rate.</li>

  </ul>

  <h2 dir="auto">Download</h2>

  <p dir="auto">The only attached binary is <strong>topos.cia</strong>. Source archives
  are available from GitHub for this release tag.</p>

  <h2 dir="auto">Validation</h2>

  <ul dir="auto">

  <li>Full build and CIA packaging checks passed.</li>

  <li>Targeted MVD initialization tests passed for an absent service, query failures,
  repeated initialization attempts, and an available service.</li>

  <li>On-device playback validation is still pending for this build.</li>

  </ul>'
updated: '2026-11-02T17:54:12Z'
version: 0.12.3.3
version_title: topos 0.12.3.3
---
