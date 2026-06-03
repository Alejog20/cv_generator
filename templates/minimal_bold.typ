#set page(margin: 1.1in)
#set text(font: "Montserrat", size: 9.5pt, fill: rgb("#374151"))
#set par(leading: 0.7em)

// Global styling to ensure bolded text pops without being too thick
#show strong: set text(weight: "semibold", fill: rgb("#111827"))
#show list: set block(spacing: 0.8em)
#set list(marker: [•], indent: 1em)

#align(left)[
  #text(size: 28pt, weight: "semibold", tracking: 0.5pt, fill: rgb("#111827"))[[[NAME]]] \
  #v(2pt)
  #text(size: 12pt, weight: "medium", tracking: 0.5pt, fill: rgb("#4b5563"))[[[TITLE]]] \
  #v(6pt)
  #text(size: 9.5pt, fill: rgb("#6b7280"))[[[CONTACT_INFO]]]
]

#v(18pt)

// The macro automatically converts titles to UPPERCASE for a crisp, monolithic look
#let section_heading(title) = [
  #text(size: 12pt, weight: "semibold", tracking: 1pt, fill: rgb("#111827"))[#upper(title)]
  #v(-6pt)
  #line(length: 100%, stroke: 1.5pt + rgb("#111827"))
  #v(6pt)
]

#section_heading("Professional Summary")
[[SUMMARY]]

#v(16pt)
#section_heading("Experience")
[[EXPERIENCE]]

#v(16pt)
#section_heading("Education")
[[EDUCATION]]

#v(16pt)
#section_heading("Core Skills")
[[SKILLS]]

#v(16pt)
[[PROJECTS_SECTION]]