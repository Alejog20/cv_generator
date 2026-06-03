#set page(margin: 0.8in)
#set text(font: "Inter", size: 9.5pt, fill: rgb("#334155"))
#set par(leading: 0.6em)
#show strong: set text(weight: "semibold", fill: rgb("#0f172a"))

// A striking header with a soft slate background box
#rect(width: 100%, fill: rgb("#f8fafc"), inset: 20pt, radius: 4pt)[
  #text(size: 26pt, font: "Montserrat", weight: "bold", fill: rgb("#0f172a"))[[[NAME]]] \
  #v(2pt)
  #text(size: 12pt, weight: "medium", fill: rgb("#3b82f6"))[[[TITLE]]] \
  #v(6pt)
  #text(size: 9pt, fill: rgb("#64748b"))[[[CONTACT_INFO]]]
]

#v(15pt)

// The Two-Column Grid Layout
#grid(
  columns: (1fr, 2.5fr),
  gutter: 20pt,
  [
    // Left Column
    #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[SKILLS]
    #v(4pt)
    // We use a Typst trick to force the skills to stack vertically on the sidebar!
    #show " • ": linebreak()
    [[SKILLS]]
    #v(15pt)

    #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[EDUCATION]
    #v(4pt)
    [[EDUCATION]]
  ],
  [
    // Right Column
    #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[SUMMARY]
    #v(4pt)
    [[SUMMARY]]
    #v(15pt)

    #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[EXPERIENCE]
    #v(4pt)
    [[EXPERIENCE]]
    #v(15pt)

    [[PROJECTS_SECTION]]
  ]
)
