#set page(margin: 1in)
#set text(font: "Helvetica", size: 11pt, fill: rgb("#333333"))

// Header Section
#align(center)[
  #text(size: 24pt, weight: "bold", fill: rgb("#111827"))[[[NAME]]] \
  #v(5pt)
  #text(size: 14pt, fill: rgb("#2563eb"))[[[TITLE]]] \
  #v(5pt)
  #text(size: 10pt, fill: rgb("#6b7280"))[[[CONTACT_INFO]]]
]

#v(10pt)
#line(length: 100%, stroke: 2pt + rgb("#2563eb"))
#v(10pt)

// Summary Section
#text(size: 14pt, weight: "bold", fill: rgb("#111827"))[Professional Summary]
#line(length: 100%, stroke: 0.5pt + rgb("#e5e7eb"))
[[SUMMARY]]

#v(15pt)

// Experience Section
#text(size: 14pt, weight: "bold", fill: rgb("#111827"))[Experience]
#line(length: 100%, stroke: 0.5pt + rgb("#e5e7eb"))
[[EXPERIENCE]]

#v(15pt)

// Education Section
#text(size: 14pt, weight: "bold", fill: rgb("#111827"))[Education]
#line(length: 100%, stroke: 0.5pt + rgb("#e5e7eb"))
[[EDUCATION]]

#v(15pt)

// Skills Section
#text(size: 14pt, weight: "bold", fill: rgb("#111827"))[Skills & Technologies]
#line(length: 100%, stroke: 0.5pt + rgb("#e5e7eb"))
[[SKILLS]]

#v(15pt)

// Projects Section (Python will dynamically build this!)
[[PROJECTS_SECTION]]