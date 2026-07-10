#!/bin/bash

# Add new languages here, space separated and using the ID for `crowdin pull`
LANGUAGES="bruh de es-ES fr he hu it ja ko no pl pt-BR ro ru tr uk zh-CN zh-TW"

ARG=''
for LANGUAGE in $LANGUAGES; do
	ARG+="-l $LANGUAGE "
done
crowdin pull $ARG
