#set page(margin: 1in)
#set text(font: "Inter", size: 10.5pt, fill: rgb("#374151"))
#set par(leading: 0.65em)

// Global Styling for elegance
#show strong: set text(weight: "semibold", fill: rgb("#111827"))
#show list: set block(spacing: 0.75em)
#set list(marker: [•], indent: 1em)

#align(left)[
  #text(size: 28pt, weight: "semibold", tracking: -0.5pt, fill: rgb("#0f172a"))[[[NAME]]] \
  #v(2pt)
  #text(size: 13pt, weight: "medium", fill: rgb("#4b5563"))[[[TITLE]]] \
  #v(6pt)
  #text(size: 9.5pt, fill: rgb("#6b7280"))[[[CONTACT_INFO]]]
]

#v(18pt)

#let section_heading(title) = [
  #text(size: 13pt, weight: "semibold", tracking: 0.5pt, fill: rgb("#111827"))[#title]
  #v(-4pt)
  #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
  #v(4pt)
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
#section_heading("Skills & Technologies")
[[SKILLS]]

#v(16pt)
[[PROJECTS_SECTION]]