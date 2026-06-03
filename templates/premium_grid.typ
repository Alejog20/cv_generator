#set page(margin: 1.1in)
#set text(font: "Inter", size: 9.5pt, fill: rgb("#374151"))
#set par(leading: 0.65em)
#show strong: set text(weight: "semibold", fill: rgb("#111827"))

#align(left)[
  #text(size: 32pt, font: "Montserrat", weight: "black", tracking: -1pt, fill: rgb("#111827"))[[[NAME]]] \
  #v(2pt)
  #text(size: 13pt, weight: "medium", fill: rgb("#6b7280"))[[[TITLE]]] \
  #v(6pt)
  #text(size: 9.5pt, fill: rgb("#6b7280"))[[[CONTACT_INFO]]]
]
#v(24pt)

// Macro to force the title to the left, and content to the right
#let grid_section(title, body) = [
  #grid(
    columns: (1fr, 3fr),
    gutter: 20pt,
    [
      #set align(right)
      #text(size: 10pt, font: "Montserrat", weight: "bold", fill: rgb("#9ca3af"))[#upper(title)]
    ],
    [#body]
  )
  #v(14pt)
]

#grid_section("Summary", [[[SUMMARY]]])
#grid_section("Experience", [[[EXPERIENCE]]])
#grid_section("Education", [[[EDUCATION]]])
#grid_section("Skills", [[[SKILLS]]])

// We use Typst 'show' rules to magically hide the hardcoded Python Titles 
// so the Projects section visually aligns perfectly with our grid!
#grid(
  columns: (1fr, 3fr),
  gutter: 20pt,
  [
    #set align(right)
    #text(size: 10pt, font: "Montserrat", weight: "bold", fill: rgb("#9ca3af"))[PROJECTS]
  ],
  [
    #show "Featured Technical Projects": none 
    #show line: none 
    [[PROJECTS_SECTION]]
  ]
)
