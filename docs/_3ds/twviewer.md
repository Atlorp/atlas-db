---
author: gamerboyrts-a11y
avatar: https://avatars.githubusercontent.com/u/251371750?v=4
categories:
- app
- media
color: '#2d1534'
color_bg: '#2d1534'
created: '2026-06-24T15:16:05Z'
description: Unofficial homebrew Twitch viewer for the Nintendo New3DS. Watch Twitch
  streams directly on your console.
download_page: https://github.com/gamerboyrts-a11y/twviewer/releases
downloads:
  twviewer.3dsx:
    size: 7675588
    size_str: 7 MiB
    url: https://github.com/gamerboyrts-a11y/twviewer/releases/download/v0.4.0/twviewer.3dsx
github: gamerboyrts-a11y/twviewer
icon: https://raw.githubusercontent.com/gamerboyrts-a11y/twviewer/main/icon.png
image: https://raw.githubusercontent.com/gamerboyrts-a11y/twviewer/main/icon.png
image_length: 32618
layout: app
llm_generation: unknown
source: https://github.com/gamerboyrts-a11y/twviewer
stars: 1
systems:
- 3DS
title: twviewer
update_notes: '<p dir="auto"><strong>Install:</strong> copy <code class="notranslate">twviewer.3dsx</code>
  to <code class="notranslate">sd:/3ds/</code> and launch from the Homebrew Launcher.
  New 3DS / New 2DS XL only.</p>

  <h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li><strong>Video quality selection</strong> — choose 160p or 360p in the Settings
  tab.</li>

  <li><strong>Fixed: crash after switching channels repeatedly</strong> — segment
  buffers are now pooled; heavy channel-switching is stable, including at 360p.</li>

  </ul>

  <h2 dir="auto">Good to know</h2>

  <ul dir="auto">

  <li><strong>Expected behavior:</strong> After watching a channel for 10+ minutes,
  switching to a different channel can cause the 3DS to become unresponsive for a
  minute or more. This appears to happen because the system is attempting to safely
  close MVD before completing the channel switch. Previously, this issue caused the
  3DS to crash outright; it now results in temporary unresponsiveness instead. The
  issue only occurs after extended viewing time on a single channel.</li>

  <li><strong>Video may pause mid-stream:</strong> if the picture stops, just wait
  — it resumes automatically after a bit. This is normal (usually server-side ads
  or a short network hiccup); no need to restart the app.</li>

  <li><strong>Getting your login code:</strong> tap the red/green <strong>Login</strong>
  button — that starts device login and shows the code you enter at twitch.tv/activate.
  The "login at twitch.tv/activate" text in the bottom bar is only a reminder; it
  does not show the code.</li>

  <li><strong>Quality buttons may need a few taps:</strong> when switching between
  160p and 360p, keep tapping until the button highlights and the stream restarts.</li>

  </ul>

  <h2 dir="auto">Known issues</h2>

  <ul dir="auto">

  <li><strong>Some channels don''t render correctly:</strong> channels whose picture
  is mostly a static overlay with little motion (e.g. GamesDoneQuick) may display
  incorrectly. Most channels are unaffected — under investigation.</li>

  <li><strong>System chat bug:</strong> if system messages appear in chat incorrectly,
  log out and back in via Device Code to reset the IRC connection.</li>

  </ul>'
updated: '2026-07-07T04:01:45Z'
version: v0.4.0
version_title: TwViewer v0.4.0
---
