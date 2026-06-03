#set page(margin: 0.8in)
#set text(font: "Inter", size: 9.5pt, fill: rgb("#334155"))
#set par(leading: 0.6em)
#show strong: set text(weight: "semibold", fill: rgb("#0f172a"))

// A striking header with a soft slate background box
#rect(width: 100%, fill: rgb("#f8fafc"), inset: 20pt, radius: 4pt)[
  #text(size: 26pt, font: "Montserrat", weight: "bold", fill: rgb("#0f172a"))[[[NAME]]] \
  #v(2pt)
  #text(size: 12pt, font: "Inter", weight: "medium", fill: rgb("#3b82f6"))[[[TITLE]]] \
  #v(6pt)
  #text(size: 9pt, fill: rgb("#64748b"))[[[CONTACT_INFO]]]
]

#v(15pt)

// The Two-Column Grid Layout
#grid(
  columns: (1.2fr, 2.5fr), 
  gutter: 25pt,
  [
    // ================= LEFT COLUMN =================
    #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[SKILLS]
    #v(4pt)
    #block[
      #show " • ": linebreak()
      #set par(spacing: 0.8em)
      [[SKILLS]]
    ]
    
    #v(15pt)

    #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[EDUCATION]
    #v(4pt)
    #block[
      // Catches every Streamlit newline and converts it to a hard break + 8pt vertical space
      #show regex("\n+"): it => [ \ #v(8pt) ]
      [[EDUCATION]]
    ]
  ],
  [
    // ================= RIGHT COLUMN =================
    
    // FIX: Using #block[ ] so Typst knows this is a styling container, not text to print!
    #block[
      #set par(justify: true)
      
      #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[SUMMARY]
      #v(4pt)
      [[SUMMARY]]
      
      #v(15pt)

      #text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[EXPERIENCE]
      #v(4pt)
      // Preserves newlines in the experience section bullet points
      #show regex("\n+"): it => [ \ #v(2pt) ]
      [[EXPERIENCE]]
    ]

    #v(15pt)

    // A separate block for Projects where we ensure justification is strictly turned OFF
    #block(width: 100%)[
      #set par(justify: false)
      
      #show "Featured Technical Projects": text(size: 11pt, font: "Montserrat", weight: "semibold", fill: rgb("#0f172a"))[FEATURED TECHNICAL PROJECTS]
      #show line: none
      
      [[PROJECTS_SECTION]]
    ]
  ]
)