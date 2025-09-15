echo "---
title: "The Little Book of Linear Algebra"
author: "Duc-Tam Nguyen"
date: \today
documentclass: ctexart
CJKmainfont: PingFang SC
geometry: margin=2.5cm
fontsize: 12pt
---" > temp.md

cat $(ls src/chapter_*.md | sort -V) >> temp.md
pandoc temp.md -o all_in_one.html --mathjax --template=template.html