---
categories:
- utility
description: Removes VenDB
layout: app
llm_generation: unknown
script:
- file: sdmc:/3ds/Universal-Updater/stores/vendb.unistore
  type: deleteFile
- file: sdmc:/3ds/Universal-Updater/stores/vendb-0.t3x
  type: deleteFile
- file: sdmc:/3ds/Universal-Updater/stores/vendb-1.t3x
  type: deleteFile
stars: 0
systems:
- 3DS
title: Remove VenDB
updated: '---'
version: 1.0.0
---
