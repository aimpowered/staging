#!/bin/bash
# This script is forked from the original version in the Notes app.

set -ex

function generate() {
	pelican Pelican/content -s Pelican/pelicanconf.py -o docs -d
	rm docs/index.html
	ln -s pages/about-us.html docs/index.html
}

function deploy() {
	git checkout main
	git add --all
	git commit -m "updating pelican outputs"
	git push origin main
}

function main() {
	generate
	# deploy
}

main "$@"
