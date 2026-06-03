#set page(margin: 1.2in)
#set text(font: "Lora", size: 11pt, fill: rgb("#27272a"))
#set par(leading: 0.65em)

#show strong: set text(weight: "semibold", fill: rgb("#18181b"))
#show list: set block(spacing: 0.65em)
#set list(marker: [•], indent: 1.2em)

#align(center)[
  #text(size: 26pt, weight: "semibold", fill: rgb("#18181b"))[[[NAME]]] \
  #v(2pt)
  #text(size: 12.5pt, style: "italic", fill: rgb("#52525b"))[[[TITLE]]] \
  #v(6pt)
  #text(size: 10pt, fill: rgb("#52525b"))[[[CONTACT_INFO]]]
]

#v(12pt)
#line(length: 100%, stroke: 0.5pt + rgb("#d4d4d8"))
#v(14pt)

#let section_heading(title) = [
  #text(size: 12.5pt, weight: "semibold", fill: rgb("#18181b"))[#title]
  #v(4pt)
]

#section_heading("SUMMARY")
[[SUMMARY]]

#v(14pt)
#section_heading("EXPERIENCE")
[[EXPERIENCE]]

#v(14pt)
#section_heading("EDUCATION")
[[EDUCATION]]

#v(14pt)
#section_heading("SKILLS")
[[SKILLS]]

#v(14pt)
[[PROJECTS_SECTION]]