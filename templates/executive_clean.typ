#set page(margin: 1.1in)
#set text(font: "Montserrat", size: 9.5pt, fill: rgb("#333333"))
#set par(leading: 0.7em)

#show strong: set text(weight: "semibold", fill: rgb("#000000"))
#show list: set block(spacing: 0.8em)
#set list(marker: [−], indent: 1em)

#align(center)[
  #text(size: 26pt, weight: "semibold", tracking: 1.5pt, fill: rgb("#111827"))[[[NAME]]] \
  #v(2pt)
  #text(size: 11.5pt, weight: "medium", tracking: 0.5pt, fill: rgb("#4b5563"))[[[TITLE]]] \
  #v(8pt)
  #text(size: 9pt, fill: rgb("#6b7280"))[[[CONTACT_INFO]]]
]

#v(20pt)

#let section_heading(title) = [
  #text(size: 11pt, weight: "semibold", tracking: 1pt, fill: rgb("#111827"))[#title]
  #v(-6pt)
  #line(length: 100%, stroke: 1.5pt + rgb("#111827"))
  #v(6pt)
]

#section_heading("PROFESSIONAL SUMMARY")
[[SUMMARY]]

#v(16pt)
#section_heading("EXPERIENCE")
[[EXPERIENCE]]

#v(16pt)
#section_heading("EDUCATION")
[[EDUCATION]]

#v(16pt)
#section_heading("CORE SKILLS")
[[SKILLS]]

#v(16pt)
[[PROJECTS_SECTION]]